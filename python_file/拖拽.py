# -*- coding: utf-8 -*-
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Button(QPushButton):
    def __init__(self, title, parent):
        print parent
        super(Button, self).__init__(title,parent)
        self.parent = parent
        self.setAcceptDrops(True)

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.LeftButton:

            mineDate = QMimeData()
            mineDate.setText(self.text())
            drag = QDrag(self)
            print mineDate
            drag.setMimeData(mineDate)
            drag.exec_(Qt.MoveAction)               # 拖放通过调用QDrag::exec()函数而启动

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat("text/plain"):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())
        self.parent.edit.clear()

    def mousePressEvent(self, e):
        QPushButton.mousePressEvent(self, e)
        if e.button() == Qt.LeftButton:
            print(self.text())


class BaseUi(QWidget):
    def __init__(self):
        super(BaseUi, self).__init__()
        self.initUI()

    def initUI(self):
        self.edit = QLineEdit("", self)
        self.edit.setDragEnabled(True)

        button = Button("Button", self)
        layout = QHBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(button)
        self.setLayout(layout)

        self.setWindowTitle("Drag & Drop")
        self.setGeometry(300, 300, 300, 150)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = BaseUi()
    sys.exit(app.exec_())