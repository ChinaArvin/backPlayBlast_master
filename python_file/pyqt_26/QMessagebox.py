#coding:utf-8
import sys
from PyQt4.QtCore import *
# from PyQt4.QtWidgets import *
from PyQt4.QtGui import *

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super(MyWindow, self).__init__(parent)

        self.setWindowTitle(u'QMessageBox例子')
        self.resize(300,100)

        self.mybutton=QPushButton(self)
        self.mybutton.move(5,5)
        self.mybutton.setText(u'点击消息弹出消息框')
        self.mybutton.clicked.connect(self.msg)
    def msg(self):
        reply4 = QMessageBox.about(self, u"标题", u"关于对话框消息正文")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    myshow=MyWindow()
    myshow.show()
    sys.exit(app.exec_())