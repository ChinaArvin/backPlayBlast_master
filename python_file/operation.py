# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui

class Button(QtGui.QPushButton):
    def __init__(self, title, parent = None):
        super(Button, self).__init__(title, parent)
        self.title = title
        self.parent = parent
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self,c):
        
        self.setText(self.title)
        self.setText(c.mimeData().text())
        self.parent.edit.clear()

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.mainLayout = QtGui.QVBoxLayout()
        self.edit = QtGui.QLineEdit(self)
        self.edit.setDragEnabled(True)
        button = Button('Button')
        self.button1 = Button('haha')
        self.mainLayout.addWidget(self.edit)
        self.mainLayout.addWidget(button)
        self.mainLayout.addWidget(self.button1)
        self.setLayout(self.mainLayout)
        self.setWindowTitle('Drag&Drop')
        self.setGeometry(300, 300, 300, 150)

        button.clicked.connect(self.Del)
        
    def Del(self):
        self.mainLayout.removeWidget(self.button1)
        self.button1.deleteLater()
        
app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())


