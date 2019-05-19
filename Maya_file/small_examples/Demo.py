# -*- coding:utf-8 -*-


from PySide.QtGui import *
from PySide.QtCore import *
import math

QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))

class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)
        self.resize(430, 300)
        self.setWindowTitle(self.tr('总结'))
        self.mylayout =MyLayout()
        self.mytable = Mytable()
        self.addTab(self.mylayout, u"布局")
        self.addTab(self.mytable, u"表格")

class MyLayout(QDialog):
    def __init__(self,parent=None):
        super(MyLayout, self).__init__(parent)

        font=QFont(self.tr('楷体'),12)
        self.label1=QLabel(self.tr('内容'))
        self.label1.setFont(font)
        self.listWidget=QListWidget()

        uplayout=QVBoxLayout()
        uplayout.addWidget(self.label1)
        self.label1.setAlignment(Qt.AlignCenter)  #让标题居中
        uplayout.addWidget(self.listWidget)

        bottomlayout=QHBoxLayout()
        self.label2=QLineEdit()

        addButton=QPushButton()
        addButton.setText('Add')
        addButton.setShortcut('Enter')

        removeButton=QPushButton()
        removeButton.setText('Remove')
        removeButton.setShortcut('Delete')

        bottomlayout.addWidget(addButton)
        bottomlayout.addWidget(self.label2)
        bottomlayout.addWidget(removeButton)

        mainLayout=QGridLayout(self)
        mainLayout.addLayout(uplayout,0,0)
        mainLayout.addLayout(bottomlayout,1,0)


        self.connect(addButton,SIGNAL('clicked()'),self.slotaddText)
        self.connect(removeButton,SIGNAL('clicked()'),self.slotremoveText)

    def slotaddText(self):
        messtext=self.label2.text()
        self.listWidget.addItem(messtext)
        self.label2.setText('')

    def slotremoveText(self):
        messtext = self.label2.text()
        count = self.listWidget.count()

        for x in range(count):
            row = self.listWidget.item(x).text()

            print row

            if messtext == row:
                self.listWidget.removeItemWidget(self.listWidget.takeItem(x))
                # self.label2.setText('')


class Mytable(QTableWidget):
    def __init__(self,parent=None):
        super(Mytable, self).__init__(parent)
        self.setColumnCount(4)
        self.setRowCount(5)
        self.setItem(0,0,QTableWidgetItem(self.tr('姓名')))
        self.setItem(0,1,QTableWidgetItem(self.tr('性别')))
        self.setItem(0,2,QTableWidgetItem(self.tr('年龄')))
        self.setItem(0,3,QTableWidgetItem(self.tr('班级')))
        name1=QTableWidgetItem(self.tr('刘志伟'))
        age1=QTableWidgetItem('18')
        name2=QTableWidgetItem(self.tr('李蒙恩'))
        age2=QTableWidgetItem('18')
        name3=QTableWidgetItem(self.tr('秦家鑫'))
        age3=QTableWidgetItem('18')
        name4=QTableWidgetItem(self.tr('何同刚'))
        age4=QTableWidgetItem('18')
        self.setItem(1,0,name1)
        self.setItem(2,0,name2)
        self.setItem(3,0,name3)
        self.setItem(4,0,name4)

        sex1=QComboBox()
        sex1.addItem(self.tr('男'))
        sex1.addItem(self.tr('女'))
        sex2=QComboBox()
        sex2.addItem(self.tr('男'))
        sex2.addItem(self.tr('女'))
        sex3=QComboBox()
        sex3.addItem(self.tr('男'))
        sex3.addItem(self.tr('女'))
        sex4=QComboBox()
        sex4.addItem(self.tr('男'))
        sex4.addItem(self.tr('女'))
        self.setCellWidget(1,1,sex1)
        self.setCellWidget(2,1,sex2)
        self.setCellWidget(3,1,sex3)
        self.setCellWidget(4,1,sex4)

        self.setItem(1,2,age1)
        self.setItem(2,2,age2)
        self.setItem(3,2,age3)
        self.setItem(4,2,age4)

        Class1=QComboBox()
        Class1.addItem(self.tr('数媒二班'))
        Class1.addItem(self.tr('数媒一班'))
        Class2=QComboBox()
        Class2.addItem(self.tr('数媒一班'))
        Class2.addItem(self.tr('数媒二班'))
        Class3=QComboBox()
        Class3.addItem(self.tr('数媒二班'))
        Class3.addItem(self.tr('数媒一班'))
        Class4=QComboBox()
        Class4.addItem(self.tr('数媒一班'))
        Class4.addItem(self.tr('数媒二班'))
        self.setCellWidget(1,3,Class1)
        self.setCellWidget(2,3,Class2)
        self.setCellWidget(3,3,Class3)
        self.setCellWidget(4,3,Class4)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    t = TabWidget()
    t.show()
    app.exec_()
