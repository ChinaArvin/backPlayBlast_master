# -*- coding:utf-8 -*-
from PySide import QtCore,QtGui
import sys
import  os

class OpenFlim(QtGui.QDialog):
    def __init__(self):
        super(OpenFlim, self).__init__()


        Openfilm_button = QtGui.QPushButton("Save as")
        self.CurrentFileEdit = QtGui.QLineEdit()
        button1 = QtGui.QPushButton("test")

        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.CurrentFileEdit)
        layout.addWidget(Openfilm_button)
        layout.addWidget(button1)



        self.setLayout(layout)

        Openfilm_button.clicked.connect(self.openfilm)
        button1.clicked.connect(self.test)

    def openfilm(self):
        s = QtGui.QFileDialog.getSaveFileName(self,"save")
        # s = QtGui.QFileDialog.getOpenFileName(self,"open")
        # s = QtGui.QFileDialog.create(self,"creat")
        self.CurrentFileEdit.setText(s[0])
        print(type(s[0])),s[0]

    def test(self):
        print self.CurrentFileEdit.text()


app = QtGui.QApplication(sys.argv)
TheWindow = OpenFlim()
TheWindow.show()
sys.exit(app.exec_())
