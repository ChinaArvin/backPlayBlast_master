# -*- coding:utf-8 -*-
from PySide import QtGui
from PySide import QtCore
import sys


class VersionComboBox(QtGui.QComboBox):
    versionChanged = QtCore.Signal(dict)
    def __init__(self, parent=None):
        QtGui.QComboBox.__init__(self, parent)

    def set_value(self, row, task,i):
        self._i = i
        self._row = row
        self._task = task
        self.activated.connect(self.itemChanged)

    def itemChanged(self):
        info = {
            'i':self._i,
            'task': self._task,
            'version': self.currentText(),
            'row': self._row
        }
        self.versionChanged.emit(info)

class MyTable(QtGui.QTableWidget):
    def __init__(self,parent = None):
        super(MyTable, self).__init__(parent)
        self.setColumnCount(5)
        self.setRowCount(0)
        num = 0
        for i in range(4):
            self.insertRow(num)
            num += 1

        self.button = QtGui.QPushButton('print')
        self.button.clicked.connect(self.show_item)

        self.setItem(0,0,QtGui.QTableWidgetItem(u"性别"))
        self.setItem(0,1,QtGui.QTableWidgetItem(u"姓名"))
        self.setItem(0,2,QtGui.QTableWidgetItem(u"出生日期"))
        self.setItem(0,3,QtGui.QTableWidgetItem(u"职业"))
        self.setItem(0,4,QtGui.QTableWidgetItem(u"收入"))
        lbp1 = QtGui.QLabel()
        lbp1.setPixmap(QtGui.QPixmap("E:\pycham\lovely.png"))
        self.setCellWidget(1,0,lbp1)
        # twi1 = QtGui.QTableWidgetItem("Tom")
        self.setCellWidget(1,1,self.button)
        dte1 = QtGui.QDateTimeEdit()
        dte1.setDateTime(QtCore.QDateTime.currentDateTime())
        dte1.setDisplayFormat("yy/mm/dd")
        dte1.setCalendarPopup(True)
        self.setCellWidget(1,2,dte1)


        for i in range(3):
            cbw = VersionComboBox()
            cbw.set_value(task="task",row="row",i=i+1)
            list = ['anim-final', 'comp-slap']
            cbw.addItems(list)
            self.setCellWidget(i+1,3,cbw)
            cbw.versionChanged.connect(self.emitsomethins)


    def emitsomethins(self,info):
        string = info['version']
        comb = VersionComboBox()
        self.lisw = QtGui.QListWidget()
        self.lisw.itemSelectionChanged.connect(self.printeg)
        self.lisw.addItem(string)
        self.lisw.addItem('test1')
        comb.addItem(string)
        # item = QtGui.QTableWidgetItem(string)
        self.setCellWidget(info['i'],4,self.lisw)
        # self.setItem(info['i'],4,item)

    def printeg(self):
        self.item = repr(self.lisw.selectedItems()[0].text().encode('utf-8'))
        print self.item

    def show_item(self):
        print self.item

app = QtGui.QApplication(sys.argv)
myqq = MyTable()
myqq.setWindowTitle("MyQQ")
myqq.show()
app.exec_()


