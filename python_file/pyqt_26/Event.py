# coding:utf-8

import sys
import random
from PySide.QtGui import *
from PySide.QtCore import *

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))


class Class2(QWidget):
    def __init__(self, *args, **kwargs):
        super(Class2,self).__init__(*args,**kwargs)
        self.__init_ui()
        self.setWindowTitle("hello")




    def __init_ui(self):
        self.test = Test(self)
        self.test.setText(u'000')
        self.test.move(170,80)
        self.yes_pb = YesPb(self)
        self.yes_pb.setText(u'yse')
        self.yes_pb.move(100,200)
        self.no_pb = NoPb(self)
        self.no_pb.setText(u'no')
        self.no_pb.move(300,200)
        self.setMinimumSize(500,430)
        self.setMaximumSize(500,430)

    def main(self):
        self.show()

class Test(QPushButton):
    pass

class YesPb(QPushButton):
    def __init__(self,*args,**kwargs):
        super(YesPb, self).__init__(*args,**kwargs)

    def mousePressEvent(self, *args, **kwargs):
        self.setText(u'push')

    def mouseReleaseEvent(self, *args, **kwargs):
        self.setText(u'I like you too')
        self.adjustSize()

class NoPb(QPushButton):
    def __init__(self,*args,**kwargs):
        super(NoPb, self).__init__(*args,**kwargs)

    def enterEvent(self,e):
        self.move(random.uniform(0,500),random.uniform(0,430))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    class_2 = Class2()
    class_2.main()
    sys.exit(app.exec_())

