# coding:utf-8
import sys
import os
from PySide import QtGui, QtCore

class base_UI(QtGui.QWidget):
    def __init__(self):
        super(base_UI, self).__init__()
        self.setWindowTitle("Set Frame")
        self.resize(400,200)

        self.ok_button = QtGui.QPushButton("OK")
        self.cancel_button = QtGui.QPushButton("Cancle")

        self.tip_button = QtGui.QPushButton(u"请输入起始/结束帧")


        self.start_label = QtGui.QLabel("start")
        self.end_label = QtGui.QLabel("end")

        self.start_line = QtGui.QLineEdit()
        self.end_line = QtGui.QLineEdit()

        button_layout = QtGui.QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.ok_button)
        button_layout.addStretch(3)
        button_layout.addWidget(self.cancel_button)
        button_layout.addStretch(1)

        line_layout = QtGui.QHBoxLayout()
        line_layout.addStretch(1)
        line_layout.addWidget(self.start_label)
        line_layout.addWidget(self.start_line)
        line_layout.addStretch(1)
        line_layout.addWidget(self.end_label)

        line_layout.addWidget(self.end_line)
        line_layout.addStretch(1)

        mainlayout = QtGui.QVBoxLayout()
        mainlayout.addWidget(self.tip_button)
        mainlayout.addItem(line_layout)
        mainlayout.addStretch(1)
        mainlayout.addItem(button_layout)
        self.setLayout(mainlayout)

        self.cancel_button.clicked.connect(self.close)

    def setSE(self):
        star_uni = self.start_line.displayText()
        end_uni = self.end_line.displayText()
        star = int(star_uni)
        end = int(end_uni)
        cmds.playbackOptions(min=star, max=end)




app = QtGui.QApplication(sys.argv)
ui= base_UI()
ui.show()
app.exec_()
