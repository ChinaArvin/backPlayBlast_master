# -*- coding:utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class Geometry(QDialog):
    def __init__(self,parent = None):
        super(Geometry, self).__init__(parent)

        self.setWindowTitle("test")
        #对话框
        filePushButton = QPushButton(self.tr("对话框"))
        self.fileLineEdit = QLineEdit()

        Label1 = QLabel("x0:")
        self.xLabel = QLabel()

        Label2 = QLabel(self.tr("请输入用户名"))
        self.nameLabel = QLabel(self.tr("输入个鬼哦"))
        self.nameLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        nameButton = QPushButton("repair")

        layout = QGridLayout()
        layout.addWidget(filePushButton,0,0)
        layout.addWidget(self.fileLineEdit,0,1)
        layout.addWidget(Label1, 1, 0)
        layout.addWidget(self.xLabel, 1, 1)
        layout.addWidget(Label2,2,0)
        layout.addWidget(self.nameLabel,2,1)
        layout.addWidget(nameButton,2,2)

        self.updateLabel()

        self.setLayout(layout)

        self.connect(filePushButton,SIGNAL("clicked()"),self.openFile)
        self.connect(nameButton,SIGNAL("clicked()"),self.slotName)

    def moveEvent(self,event):
        self.updateLabel()
    def resizeEvent(self,event):
        self.updateLabel()
    def updateLabel(self):
        temp = QString()

        self.xLabel.setText(temp.setNum(self.x()))


    def openFile(self):

        s = QFileDialog.getOpenFileNames(self,"Open file dialog","/","Python files(*.py)")
        print s
        self.fileLineEdit.setText(str(s))

    def slotName(self):

        name,ok = QInputDialog.getText(self,self.tr("用户名"),
                                       self.tr("请输入新的名字:"),
                                       QLineEdit.Normal,self.nameLabel.text())
        if ok and(not name.isEmpty()):
            self.nameLabel.setText(name)




app = QApplication(sys.argv)
form = Geometry()
form.show()
app.exec_()