from PySide import QtGui
from PySide import QtCore
import sys

class MayaShow(QtGui.QWidget):
    def __init__(self):
        super(MayaShow, self).__init__()
        #QtGui.QWidget.__init__(self,parent)

        button = QtGui.QPushButton("Hello Kitty!")

        self.layout1 = QtGui.QVBoxLayout()
        self.layout1.addWidget(button)
        self.setLayout(self.layout1)

        button.clicked.connect(QtCore.QCoreApplication.instance().quit)


app = QtGui.QApplication(sys.argv)
B = MayaShow()
B.show()
sys.exit(app.exec_())
