# -*- coding:utf8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import os


class FolderList(QMainWindow):
    def __init__(self):
        super(FolderList, self).__init__()
        self.createMenus()

        model = QFileSystemModel()                      # 提供本地文件系统的数据模型。
        model.setRootPath(QDir.currentPath())

        topWindow = TopWindow()

        tree = QTreeView()
        list = QListView()

        tree.setModel(model)
        list.setModel(model)

        list.setSelectionModel(tree.selectionModel())
        tree.doubleClicked.connect(list.setRootIndex)

# --------------------------文件显示布局----------------------------------

        TLSplitter = QSplitter(Qt.Horizontal,self)
        TLSplitter.addWidget(tree)
        TLSplitter.addWidget(list)

        mainSplitter = QSplitter(Qt.Vertical,self)
        mainSplitter.addWidget(topWindow)
        mainSplitter.addWidget( TLSplitter)

        self.setCentralWidget(mainSplitter)
        mainSplitter.show()
# ----------------------------------菜单栏---------------------------------
    def createMenus(self):
        self.fileNewAction = QAction(QIcon(":/filenew.png"), u"新建", self)
        self.fileNewAction.setShortcut("Ctrl+N")
        self.fileNewAction.setStatusTip(u"新建一个文件")
        self.connect(self.fileNewAction, SIGNAL("triggered()"), self.slotNewFile)

        self.exitAction = QAction(QIcon(":/filequit.png"), u"退出", self)
        self.exitAction.setShortcut("Ctrl+Q")
        self.setStatusTip(u"退出")
        self.connect(self.exitAction, SIGNAL("triggered()"), self.close)


        fileMenu = self.menuBar().addMenu(u"文件")
        fileMenu.addAction(self.fileNewAction)
        fileMenu.addAction(self.exitAction)

        editMenu = self.menuBar().addMenu(u"编辑")
        aboutMenu = self.menuBar().addMenu(u"帮助")

    def slotNewFile(self):
        newWin = FolderList()
        newWin.show()
        newWin.exec_()


# --------------------------------按钮及文本框------------------------------
class TopWindow(QDialog):
    def __init__(self):
        super(TopWindow, self).__init__()

        button5 = QPushButton(u"前进")
        button6 = QPushButton(u"后退")
        button7 = QPushButton(u"上移")
        button8 = QPushButton(u"搜索")

        self.label1 = QLineEdit()
        self.label1.setMaximumWidth(600)
        self.label2 = QLineEdit()
        self.label2.setFocus()
        self.label2.setStyleSheet(
            "QLineEdit{background-color:yellow;font-size:12px;}")
        self.label2.setMaximumWidth(100)

        layout = QGridLayout()
        layout.addWidget(button5, 0, 0)
        layout.addWidget(button6, 0, 1)
        layout.addWidget(button7, 0, 2)
        layout.addWidget(self.label1, 0, 3)
        layout.addWidget(self.label2, 0, 5)
        layout.addWidget(button8, 0,6)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    folder = FolderList()
    folder.show()
    sys.exit(app.exec_())
