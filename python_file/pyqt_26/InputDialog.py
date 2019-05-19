# -*- coding: utf-8 -*-
from  PyQt4.QtCore import *
from  PyQt4.QtGui import *
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class InputDlg(QDialog):
    def __init__(self,parent = None):
        super(InputDlg,self).__init__(parent)

        label1 = QLabel(self.tr("姓名"))
        label2 = QLabel(self.tr("性别"))
        label3 = QLabel(self.tr("年龄"))
        label4 = QLabel(self.tr("身高"))
        label5 = QLabel(self.tr("测试"))

        self.nameLabel = QLabel(self.tr("mr.李"))
        self.nameLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.sexLabel = QLabel(self.tr("男"))
        self.sexLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.ageLabel = QLabel("25")
        self.ageLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.statureLabel = QLabel("168")
        self.statureLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        self.testLabel = QLabel(self.tr("哈哈哈"))
        self.testLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        nameButton = QPushButton(self.tr("重新输入"))
        sexButton = QPushButton(self.tr("重新输入"))
        ageButton = QPushButton(self.tr("重新输入"))
        statureButton = QPushButton(self.tr("重新输入"))
        testButton = QPushButton(self.tr("重新输入"))

        self.connect(nameButton,SIGNAL("clicked()"),self.slotName)
        self.connect(sexButton,SIGNAL("clicked()"),self.slotSex)
        self.connect(ageButton,SIGNAL("clicked()"),self.slotAge)
        self.connect(statureButton,SIGNAL("clicked()"),self.slotStature)
        self.connect(testButton,SIGNAL("clicked()"),self.slotTest)

        layout = QGridLayout()
        layout.addWidget(label1,0,0)
        layout.addWidget(self.nameLabel,0,1)
        layout.addWidget(nameButton,0,2)
        layout.addWidget(label2,1,0)
        layout.addWidget(self.sexLabel,1,1)
        layout.addWidget(sexButton,1,2)
        layout.addWidget(label3,2,0)
        layout.addWidget(self.ageLabel,2,1)
        layout.addWidget(ageButton,2,2)
        layout.addWidget(label4,3,0)
        layout.addWidget(self.statureLabel,3,1)
        layout.addWidget(statureButton,3,2)
        layout.addWidget(label5,4,0)
        layout.addWidget(self.testLabel,4,1)
        layout.addWidget(testButton,4,2)

        self.setLayout(layout)

        self.setWindowTitle(self.tr("资料收集"))
    def slotTest(self):
        test,ok = QInputDialog.getText(self,self.tr('测试'),
                                       self.tr("随便输"),
                                       QLineEdit.Normal,self.testLabel.text())
        if ok :
            self.testLabel.setText(test)

    def slotName(self):
        name,ok = QInputDialog.getText(self,self.tr("用户名"),
                                       self.tr("请输入名字:"),
                                       QLineEdit.Normal,self.nameLabel.text())
        if ok and (not name.isEmpty()):
            self.nameLabel.setText(name)

    def slotSex(self):
        list = QStringList()
        list.append(self.tr("男"))
        list.append(self.tr("女"))
        sex,ok = QInputDialog.getItem(self,self.tr("性别"),self.tr("请选择性别"),list)

        if ok:
            self.sexLabel.setText(sex)

    def slotAge(self):
        age,ok = QInputDialog.getInteger(self,self.tr("年龄"),
                                         self.tr("请输入年龄:"),
                                         int(self.ageLabel.text()),0,150)
        if ok :
            self.ageLabel.setText(str(age))

    def slotStature(self):
        stature,ok = QInputDialog.getDouble(self,self.tr("身高"),
                                            self.tr("请输入身高"),
                                            float(self.statureLabel.text()),0,2300.00)
        if ok:
            self.statureLabel.setText(str(stature))

app = QApplication(sys.argv)
form = InputDlg()
form.show()
app.exec_()

