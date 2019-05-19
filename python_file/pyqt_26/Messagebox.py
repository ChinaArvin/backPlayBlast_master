# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class MessageBoxDIg(QDialog):
    def __init__(self,parent = None):
        super(MessageBoxDIg, self).__init__(parent)
        self.setWindowTitle("Messagebox")
        self.label = QLabel("About Qt Messagebox")
        questionButton = QPushButton("Question")
        informationButton = QPushButton("Information")
        warningButton = QPushButton("Warning")
        criticalButton = QPushButton("Critical")
        aboutButton = QPushButton("About")
        aboutqtButton = QPushButton("Aboutqt")
        customButton = QPushButton("Custom")

        gridLayout = QGridLayout(self)
        gridLayout.addWidget(self.label,0,0,1,2)
        gridLayout.addWidget(questionButton,1,0)
        gridLayout.addWidget(informationButton,1,1)
        gridLayout.addWidget(warningButton,2,0)
        gridLayout.addWidget(criticalButton,2,1)
        gridLayout.addWidget(aboutButton,3,0)
        gridLayout.addWidget(aboutqtButton,3,1)
        gridLayout.addWidget(customButton,4,0)

        self.connect(questionButton,SIGNAL("clicked()"),self.slotQuestion)
        self.connect(informationButton,SIGNAL("clicked()"),self.slotInformation)
        self.connect(warningButton,SIGNAL("clicked()"),self.slotWarning)
        self.connect(criticalButton,SIGNAL("clicked()"),self.slotCritical)
        self.connect(aboutButton,SIGNAL("clicked()"),self.slotAbout)
        self.connect(aboutqtButton,SIGNAL("clicked()"),self.slotAboutQt)
        self.connect(customButton,SIGNAL("clicked()"),self.slotCustom)

    def slotQuestion(self):
        button = QMessageBox.question(self,"Question",
                                          self.tr("已经到达文档结尾,是否从头查找?"),
                                          QMessageBox.Ok|QMessageBox.Cancel,
                                          QMessageBox.Ok)
        if button == QMessageBox.Ok:
            self.label.setText("Question button/Ok")
        elif button == QMessageBox.Cancel:
            self.label.setText("Queston button/Cancel")
        else:
            return

    def slotInformation(self):
        QMessageBox.information(self,"Information",
                                self.tr("填写任意想告诉用户的信息"))
        self.label.setText("Information MessageBox")

    def slotWarning(self):
        button = QMessageBox.warning(self,"Warning",
                                     self.tr("是否保存对文档的修改?"),
                                     QMessageBox.Save|QMessageBox.Discard|QMessageBox.Cancel,
                                     QMessageBox.Save)
        if button == QMessageBox.Save:
            self.label.setText("Warning button/Save")
        elif button == QMessageBox.Discard:
            self.label.setText("Warning button/Discard")
        elif button == QMessageBox.Cancel:
            self.label.setText("Warning button/Cancel")
        else:
            return

    def slotCritical(self):
        QMessageBox.critical(self,"Critical",
                            self.tr("提醒用户一个致命的错误"))
        self.label.setText("Critical MessageBox")

    def slotAbout(self):
        QMessageBox.about(self,"About",self.tr("About事例"))
        self.label.setText("About Qt MessageBox")

    def slotAboutQt(self):
        QMessageBox.aboutQt(self,"About Qt")
        self.label.setText("About Qt MessageBox")

    def slotCustom(self):
        customMsgBox = QMessageBox(self)
        customMsgBox.setWindowTitle("Custom message box")
        lockButton = customMsgBox.addButton(self.tr("锁定"),
                                                QMessageBox.ActionRole)
        unlockButton = customMsgBox.addButton(self.tr("解锁"),
                                                  QMessageBox.ActionRole)
        cancelButton = customMsgBox.addButton("cancle",QMessageBox.ActionRole)

        customMsgBox.setText(self.tr("这是一个自定义消息框"))
        customMsgBox.exec_()

        button = customMsgBox.clickedButton()
        if button == lockButton:
            self.label.setText("Custom MessageBox/Lock")
        elif button == unlockButton:
            self.label.setText("Custom MessageBox/Unlock")
        elif button == cancelButton:
            self.label.setText("Custom MessageBox/Cancel")


app = QApplication(sys.argv)
MessageBox = MessageBoxDIg()
MessageBox.show()
app.exec_()

