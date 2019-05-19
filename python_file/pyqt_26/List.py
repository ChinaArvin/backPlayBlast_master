# -*- coding: utf-8 -*-
import sys
from PySide2 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        qbtn = QtGui.QPushButton('Quit', self) # 创建一个Quit按钮
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit) # 此处是利用Qt的信号槽机制,当你点击Quit button
        #  时会产生一个信号,而该信号会触发QtCore.QCoreApplication.instance().quit来退出当前窗口,
        # 也即是 通过Qt的信号槽机制,将QPushButton对象的clicked信号和
        # QtCore.QCoreApplication.instance().quit联系(connect())在一起
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()