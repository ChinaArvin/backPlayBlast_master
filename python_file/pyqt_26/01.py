# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os, sys, fnmatch
import time


class MainWidgetUI(QDialog):
    def __init__(self, parent=None):
        super(MainWidgetUI, self).__init__(parent)
        self.setWindowIcon(QIcon("favicon.ico"))
        self.setWindowOpacity(0.85)  # 透明度
        self.setWindowTitle(u'查询文件')
        self.directory = ''  # 跟目录
        self.mainLayout = QVBoxLayout()  # 水平布局
        # Find 文件布局
        self.topgroupBox = QGroupBox(u"任意右键选择查询目录")
        self.topLayout = QHBoxLayout(self.topgroupBox)
        self.lineEdit = QLineEdit('', self.topgroupBox)
        self.lineEdit.setPlaceholderText(u'如：chrome.exe, 多个 ; 分割')
        self.searchBtn = QPushButton(QIcon(u"favicon.ico"), '查询', self.topgroupBox)
        self.topLayout.addWidget(self.lineEdit)
        self.topLayout.addWidget(self.searchBtn)


        # 输出文件路径布局
        self.bottgroupBox = QGroupBox(u'文件路径')
        self.bottLayout = QVBoxLayout(self.bottgroupBox)  # 水平布局
        self.ListWidget = QListWidget(self.bottgroupBox)
        self.bottLayout.addWidget(self.ListWidget)

        # mainLayout 布局
        self.mainLayout.addWidget(self.topgroupBox)
        self.mainLayout.addWidget(self.bottgroupBox)
        self.setLayout(self.mainLayout)

        self.searchBtn.clicked.connect(self.searchDef)  # 查询事件
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightHandButton)  # 任意地方右键 选择跟目录
        self.ListWidget.itemDoubleClicked.connect(self.doubleClickListPath)  # List路径列表双击事件
        self.lineEdit.setFocus()  # 得到焦点
        # 搜索框样式
        self.lineEdit.setStyleSheet(
            "QLineEdit{background-color:green;color:menubar;font-size:12px;background-image:url(search.png);}")

        self.Theading2 = TheadingSearchBtnNet(u"查询")
        self.Theading2.resultSearchBtnNetSignal.connect(self.searchBtnText)  # 连接信号。 TheadingFindFile在线程状态结果后emit发射信号


        # self.lineEdit.setText('chrome.exe;readme.txt')
        # self.ListWidget.addItem("C:\\Program Files\\7-Zip/7z.exe")
        # self.ListWidget.addItem("bb")
        # self.ListWidget.addItem("E:\\Program Files/java")

    # 显示查询按钮点点点效果
    def searchBtnText(self, strings):
        self.searchBtn.setText("查询" + str(strings))

    # List路径列表双击事件
    def doubleClickListPath(self):
        text = self.ListWidget.currentItem().text()  # 获取当前Item的text
        text = text.replace('/', '\\')
        if text != '无查询结果':
            os.system(r'explorer /select,' + str(text))  # 打开文件并选中文件

    # 任意地方右键
    def rightHandButton(self):
        self.directory = QFileDialog.getExistingDirectory(self, "请选择根目录", 'c:\\')
        self.topgroupBox.setTitle("查询根目录：" + str(self.directory))

    # 查询BTN 按钮
    def searchDef(self):
        self.ListWidget.clear()  # 清空ListWidget数据
        inputs = self.lineEdit.text()
        if inputs == '':
            QMessageBox.warning(self, '查询提示', '输入的查询文件名关键字不能为空', QMessageBox.Yes)
            return False
        if self.directory == '':
            QMessageBox.warning(self, '查询提示', '请任意右键选择查询的跟目录', QMessageBox.Yes)
            return False
        self.searchBtn.setDisabled(True)
        self.Theading2.setVal(1)  # 查询点点点效果线程开始
        try:
            # 在实例化类与connect、start 直接不能打印任何东西，不然会报错
            senderData = (self.directory, self.lineEdit.text())
            self.Theading = TheadingFindFile(senderData)
            self.Theading.resultSearchSignal.connect(self.updateResult)  # 连接信号。 TheadingFindFile在线程状态结果后emit发射信号
            self.Theading.start()  # 线程开始

        except Exception as e:
            print(e)

    # 返回响应的参数
    def updateResult(self, resultData):
        self.searchBtn.setDisabled(False)
        self.searchBtn.setText('查询')
        self.Theading2.setVal(0)  # 停止执行
        for data in resultData:
            self.ListWidget.addItem(data)


# 线程查询类
class TheadingFindFile(QThread):
    resultSearchSignal = pyqtSignal(list)  # 声明一个带列表结果的参数信号

    def __init__(self, tuple):
        super(TheadingFindFile, self).__init__()
        self.searchTuple = tuple  # 元组？

    def run(self):
        result = []  # 列表
        files = self.search_files(self.searchTuple[0], self.searchTuple[1], False, False)
        for file in files:
            result.append(file)
        if not result:
            result = ['无查询结果']
        try:
            self.resultSearchSignal.emit(result)  # 发射信号
        except Exception as e:
            print(e)

    # 检查一个目录，后者某个包含子目录的目录树，并根据某种模式迭代所有文件
    # patterns如：*.html,若大小写敏感可写*.[Hh][Tt][Mm][Ll]
    # single_level 为True表示只检查第一层
    # yield_folders 表示是否显示子目录，为False只遍历子目录中的文件，
    # 但不返回字母名
    def search_files(self, directory, patterns='*', single_level=False, yield_folders=False):
        # 将模式从字符串中取出放入列表中
        patterns = patterns.split(';')
        for path, subdirs, files in os.walk(directory,followlinks=False):
            if yield_folders:
                files.extend(subdirs)
            files.sort()
            for name in files:
                for pattern in patterns:
                    if fnmatch.fnmatch(name, pattern):
                        yield os.path.join(path, name)
                        break
            if single_level:
                break


# 线程查询效果类
class TheadingSearchBtnNet(QThread):
    resultSearchBtnNetSignal = pyqtSignal(str)  # 声明一个带列表结果的参数信号
    def __init__(self, str):
        super(TheadingSearchBtnNet, self).__init__()
        self.searchTuple = str

    # 设置status 的状态值， 1 为可执行，0：停止执行
    def setVal(self, st):
        self.st = st
        self.start()

    def run(self):
        i = 5
        while True:
            Dot = ''
            if i <= 5:
                for l in range(0, 5):
                    time.sleep(1)
                    Dot += str('.')
                    if self.st == 1:  # 可执行
                        self.resultSearchBtnNetSignal.emit(str(Dot))  # 发射信号
                i += 1
            else:
                i = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_widget = MainWidgetUI()
    main_widget.show()
    sys.exit(app.exec_())