import sys
import os
from PyQt4 import QtGui, QtCore


class Win(QtGui.QDialog):
    def __init__(self):
        super(Win, self).__init__()
        self.a()

    def a(self):
        self.view1 = TestListView()
        self.view2 = QtGui.QLineEdit()
        self.mainlayout = QtGui.QVBoxLayout()
        self.mainlayout.addWidget(self.view1)
        self.mainlayout.addWidget(self.view2)
        ll = QtGui.QVBoxLayout()
        ll.addLayout(self.mainlayout)
        self.setLayout(ll)


class TestListView(QtGui.QListWidget):
    def __init__(self, parent=None):
        super(TestListView, self).__init__(parent)
        self.setAcceptDrops(True)
        # self.win = MainForm()
        self.setIconSize(QtCore.QSize(72, 72))

    def dragEnterEvent(self, event):
        win = Win()
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                a = unicode(url.toLocalFile())

                dirs = os.listdir(unicode(url.toLocalFile()))
                for file in dirs:
                    self.addItem(file)
        else:
            event.ignore()
        win.view2.setText(a)


app = QtGui.QApplication(sys.argv)
win = Win()
win.show()
app.exec_()

