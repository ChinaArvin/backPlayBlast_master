# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os, sys, fnmatch              # 标准库fnmatch。这个库专门用来做文件名匹配
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
        self.searchBtn = QPushButton(QIcon("favicon.ico"), u'查询', self.topgroupBox)
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

        self.lineEdit.setFocus()  # 得到焦点
        # 搜索框样式
        self.lineEdit.setStyleSheet(
            "QLineEdit{background-color:green;color:menubar;font-size:12px;background-image:url(search.png);}")

# -----------将搜索的目录指定到某个盘或某个盘里面的某个文件夹。在UI中任意右键选择要搜索的目录---------------------
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightHandButton)  # 任意地方右键 选择跟目录

    def rightHandButton(self):
        self.directory = QFileDialog.getExistingDirectory(self, u"请选择根目录", 'c:\\')
        self.topgroupBox.setTitle(u"查询根目录：" + str(self.directory))

# -------------------------------这一步就用os.walk查询文件,我们把这个功能封装正一个方法：----------------------------
    def search_files(self, directory, patterns='*', single_level=False, yield_folders=False):
        # 将模式从字符串中取出放入列表中
        patterns = patterns.split(';')
        for path, subdirs, files in os.walk(directory,followlinks=False):
            if yield_folders:
                files.extend(subdirs)
            files.sort()
            for name in files:
                for pattern in patterns:
                    if fnmatch.fnmatch(name, pattern):           # fnmatch：判断文件名是否符合特定的模式
                        yield os.path.join(path, name)           # os.path.join()用于路径拼接文件的路径
                        break
            if single_level:
                break
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_widget = MainWidgetUI()
    main_widget.show()
    sys.exit(app.exec_())