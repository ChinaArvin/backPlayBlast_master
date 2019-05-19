# -*- encoding: utf-8 -*-
from PySide import QtGui as QtWidgets
from PySide import QtCore
from math import sin, cos
import sys

class BaseUI(QtWidgets.QDialog):
    def __init__(self):
        super(BaseUI, self).__init__()
        self.setWindowTitle(u"Sprial Circle")
        self.resize(300,200)

        self.height_label = QtWidgets.QLabel("height")
        self.lRadius_label = QtWidgets.QLabel("lRadius")
        self.uRadius_label = QtWidgets.QLabel("uRadius")
        self.frequency_label = QtWidgets.QLabel("frequency")

        self.height_line = QtWidgets.QLineEdit()
        self.height_line.setStyleSheet(
            "QLineEdit{background-color:white;}")
        self.lRadius_line = QtWidgets.QLineEdit()
        self.uRadius_line = QtWidgets.QLineEdit()
        self.frequency_line = QtWidgets.QLineEdit()

        self.ok_button = QtWidgets.QPushButton("OK")

        layout1 = QtWidgets.QGridLayout()
        layout1.addWidget(self.height_label,0,0)
        layout1.addWidget(self.height_line,0,1)

        layout1.addWidget(self.lRadius_label,1,0)
        layout1.addWidget(self.lRadius_line,1,1)

        layout1.addWidget(self.uRadius_label,2,0)
        layout1.addWidget(self.uRadius_line,2,1)

        layout1.addWidget(self.frequency_label,3,0)
        layout1.addWidget(self.frequency_line,3,1)

        mainlayout = QtWidgets.QVBoxLayout()
        mainlayout.addItem(layout1)
        mainlayout.addWidget(self.ok_button)

        self.setLayout(mainlayout)

        self.ok_button.clicked.connect(self.function)


    def function(self):
        geoNet = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)

        spiral = geoNet.pwd().createNode("curve")
        coordsParm = spiral.parm("coords")

        height =float(self.height_line.displayText())
        lRadius = float(self.lRadius_line.displayText())
        uRadius = float(self.uRadius_line.displayText())
        frequency = float(self.frequency_line.displayText())

        coordsStr = ''
        radius = lRadius
        step = (lRadius - uRadius) / (height * frequency)

        for i in range(int(height * frequency)):
            px = str(radius * sin(i))
            py = str(i * 1 / frequency)
            pz = str(radius * cos(i))

            coordsStr += px + ',' + py + ',' + pz + ' '
            radius -= step

        coordsParm.set(coordsStr)

app = QtWidgets.QApplication(sys.argv)
ui = BaseUI()
ui.show()
sys.exit(app.exec_())