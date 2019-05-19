# coding:utf-8
import sys
import os
from PyQt4 import QtGui, QtCore


class MyWindow(QtGui.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.mainlayout = QtGui.QVBoxLayout()
        self.view1 = QtGui.QLineEdit()
        self.view2 = TextEdit()
        self.mainlayout.addWidget(self.view2)
        self.mainlayout.addWidget(self.view1)
        self.setLayout(self.mainlayout)


class TextEdit(QtGui.QTextEdit):
    def __init__(self):
        super(TextEdit, self).__init__()
        self.setAcceptDrops(True)

    def canInsertFromMimeData(self, mimeData):
        if mimeData.hasUrls():
            return True

    def dragEnterEvent(self, event):
        win = MyWindow()
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(TextEdit, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        super(TextEdit, self).dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                path1 = unicode(url.toLocalFile())
                dirs = os.listdir(unicode(url.toLocalFile()))
                for file in dirs:
                    son_path = path1 + "/" + file
                    if  os.path.isdir(son_path):
                        dirs2 = os.listdir(son_path)
                        for file2 in dirs2:
                            self.append(file2)
                    else:
                        self.append(file)
        else:
            event.ignore()
        win.view1.setText(path1)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
