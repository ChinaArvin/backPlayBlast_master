# -*- coding:utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))

class FirstPage(QDialog):
    def __init__(self, parent = None):
        super(FirstPage, self).__init__(parent)
        #self.setStyleSheet("background: black")


        self.InputText = QListWidget()

        self.addButton = QPushButton("add")

        layout = QGridLayout()
        layout.addWidget(self.InputText,0,0)
        layout.addWidget(self.addButton,1,0)
        self.setLayout(layout)

        self.connect(self.addButton,SIGNAL("clicked()"),self.slotText)

    def slotText(self):
        text,ok = QInputDialog.getText(self,self.tr("用户"),
                                       self.tr("please input:"),
                                       QLineEdit.Normal,
                                       self.InputText.addItem('text'))
        if ok and (not text.isEmpty()):
            self.InputText.addItem()

class SecondPage(QDialog):
    def __init__(self, parent=None):
        super(SecondPage, self).__init__(parent)
       # self.setStyleSheet("background: red")


class TabWidget(QTabWidget):
    def __init__(self,parent = None):
        super(TabWidget, self).__init__(parent)
        self.setWindowTitle(self.tr("翻页"))
        self.resize(400,300)
        self.addTab(FirstPage(),u"第一页")
        self.addTab(SecondPage(),u"第二页")

app = QApplication(sys.argv)
t = TabWidget()
t.show()
app.exec_()