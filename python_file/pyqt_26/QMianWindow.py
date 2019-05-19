# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("QMainWindow")
        self.text = QTextEdit()
        self.setCentralWidget(self.text)

        self.createActions()
        self.createMenus()

        self.button1 = QPushButton("open")

    def createActions(self):
        self.fileOpenAction = QAction(QIcon(":/fileopen.png"),self.tr("打开"), self)
        self.fileOpenAction.setShortcut("Ctrl+O")
        self.fileOpenAction.setStatusTip(self.tr("打开一个文件"))
        self.connect(self.fileOpenAction, SIGNAL("triggered()"), self.slotOpenFile)

        self.fileNewAction = QAction(QIcon(":/filenew.png"), self.tr("新建"), self)
        self.fileNewAction.setShortcut("Ctrl+N")
        self.fileNewAction.setStatusTip(self.tr("新建一个文件"))
        self.connect(self.fileNewAction, SIGNAL("triggered()"), self.slotNewFile)

        self.fileSaveAction = QAction(QIcon(":/filesave.png"), self.tr("保存"), self)
        self.fileSaveAction.setShortcut("Ctrl+S")
        self.fileSaveAction.setStatusTip(self.tr("保存文件"))
        self.connect(self.fileSaveAction, SIGNAL("triggered()"), self.slotSaveFile)

        self.exitAction = QAction(QIcon(":/filequit.png"), self.tr("退出"), self)
        self.exitAction.setShortcut("Ctrl+Q")
        self.setStatusTip(self.tr("退出"))
        self.connect(self.exitAction, SIGNAL("triggered()"), self.close)

        self.cutAction = QAction(QIcon(":/editcut.png"), self.tr("剪切"), self)
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.setStatusTip(self.tr("剪切到粘贴板"))
        self.connect(self.cutAction, SIGNAL("triggered()"), self.text.cut)

        self.copyAction = QAction(QIcon(":/editcopy.png"), self.tr("复制"), self)
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.setStatusTip(self.tr("复制到粘贴板"))
        self.connect(self.copyAction, SIGNAL("triggered()"), self.text.copy)

        self.pasteAction = QAction(QIcon(":/editpaste.png"), self.tr("粘贴"), self)
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.setStatusTip(self.tr("粘贴内容到当前处"))
        self.connect(self.pasteAction, SIGNAL("triggered()"), self.text.paste)

        self.aboutAction = QAction(self.tr("关于"), self)
        self.connect(self.aboutAction, SIGNAL("triggered()"), self.slotAbout)

    def createMenus(self):
        fileMenu = self.menuBar().addMenu(self.tr("文件"))
        fileMenu.addAction(self.fileNewAction)
        fileMenu.addAction(self.fileOpenAction)
        fileMenu.addAction(self.fileSaveAction)
        fileMenu.addAction(self.exitAction)

        editMenu = self.menuBar().addMenu(self.tr("编辑"))
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.cutAction)
        editMenu.addAction(self.pasteAction)

        aboutMenu = self.menuBar().addMenu(self.tr("帮助"))
        aboutMenu.addAction(self.aboutAction)


    def slotNewFile(self):
        newWin = MainWindow()
        newWin.show()

    def slotOpenFile(self):
        fileName = QFileDialog.getOpenFileName(self)
        if fileName.isEmpty() == False:
            if self.text.document().isEmpty():
                self.loadFile(fileName)
            else:
                newWin = MainWindow()
                newWin.show()
                newWin.loadFile(fileName)

    def loadFile(self, fileName):
        file = QFile(fileName)
        if file.open(QIODevice.ReadOnly | QIODevice.Text):
            textStream = QTextStream(file)
            while textStream.atEnd() == False:
                self.text.append(textStream.readLine())

    def slotSaveFile(self):
        pass

    def slotAbout(self):
        QMessageBox.about(self,"about me", u"这是我们的第一个例子")


class TopWindow(QDialog):
    def __init__(self):
        super(TopWindow, self).__init__()

        button1 = QPushButton(u"文件")
        button2 = QPushButton(u"计算机")
        button3 = QPushButton(u"查看")
        button4 = QPushButton(u"帮助")
        button5 = QPushButton(u"前进")
        button6 = QPushButton(u"后退")
        button7 = QPushButton(u"上移")
        button8 = QPushButton(u"搜索")

        label1 = QLineEdit()
        label2 = QLineEdit()

        layout = QGridLayout()
        layout.addWidget(button1,0,0)
        layout.addWidget(button2, 0, 1)
        layout.addWidget(button3, 0, 2)
        layout.addWidget(button4, 0, 3)
        layout.addWidget(button5, 2, 0)
        layout.addWidget(button6, 2, 1)
        layout.addWidget(button7, 2, 2)
        layout.addWidget(label1, 2, 3)
        layout.addWidget(label2, 2, 4)
        layout.addWidget(button8, 2,5)
        self.setLayout(layout)


app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()