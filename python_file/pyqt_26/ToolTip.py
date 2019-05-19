import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class Tooltip(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Tooltip")

        # self.setToolTip("this is a<b>QWidget</b>widget")
        cc = QtGui.QPushButton("A QWidget widget")

        self.layout1 = QtGui.QVBoxLayout()
        self.layout1.addWidget(cc)

        self.setLayout(self.layout1)

        # QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish',10))

app = QtGui.QApplication(sys.argv)
tooltip = Tooltip()
tooltip.show()
sys.exit(app.exec_())
