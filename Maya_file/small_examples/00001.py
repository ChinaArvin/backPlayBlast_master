# coding:utf-8
import sys
import imp
import math

from PySide import QtGui
from PySide import QtCore

class Base_UI(QtGui.QDialog):
    def __init__(self):
        super(Base_UI, self).__init__()
        self.resize(300, 400)
        self.left_list = QtGui.QListWidget()
        self.right_list = QtGui.QListWidget()
        self.setWindowTitle('Decide elements')

        self.line = QtGui.QLineEdit()

        self.tip_label = QtGui.QLabel(u"显示渲染元素请点击Touch按钮")
        self.decide_button = QtGui.QPushButton(u"Touch")

        self.left_label = QtGui.QLabel(u"已添加的所有渲染元素")
        self.right_label = QtGui.QLabel(u"已启用的渲染元素")

        bottom_layout = QtGui.QHBoxLayout()
        bottom_layout.addWidget(self.left_list)
        bottom_layout.addWidget(self.right_list)

        top1_layout = QtGui.QHBoxLayout()
        top1_layout.addWidget(self.tip_label)
        top1_layout.addWidget(self.decide_button)

        top2_layout = QtGui.QHBoxLayout()
        top2_layout.addWidget(self.left_label)
        top2_layout.addWidget(self.right_label)

        mainlayout = QtGui.QVBoxLayout()
        mainlayout.addItem(top1_layout)
        mainlayout.addWidget(self.line)
        mainlayout.addItem(top2_layout)
        mainlayout.addItem(bottom_layout)
        self.setLayout(mainlayout)
        self.decide_button.clicked.connect(self.display)
    def display(self):
        lists = self.line.text()
        for list in lists:

            print str(list)

app = QtGui.QApplication(sys.argv)
ui = Base_UI()
ui.show()
app.exec_()
