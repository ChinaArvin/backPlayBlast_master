# -*- coding:utf-8 -*-
from PySide import QtGui,QtCore
import sys


class QDialoButton(QtGui.QDialog):
    def __init__(self):
        super(QDialoButton, self).__init__()

        findButton = QtGui.QPushButton("Find")
        findButton.setDefault(True)

        moreButton = QtGui.QPushButton("More")
        moreButton.setCheckable(True)

        moreButton.setAutoDefault(False)

        buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Vertical)
        buttonBox.addButton(findButton, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(moreButton, QtGui.QDialogButtonBox.ActionRole)

        layout = QtGui.QGridLayout()
        layout.addWidget(findButton,0,0)
        layout.addWidget(moreButton,0,1)
        self.setLayout(layout)

app = QtGui.QApplication(sys.argv)
QDB = QDialoButton()
QDB.show()
app.exec_()