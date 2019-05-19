#-*-coding:utf-8-*-
import sys
from PyQt4 import QtGui,QtCore

class StringListDlg(QtGui.QDialog):
    """
    主对话框
    """
    def __init__(self,fruit):
        super(StringListDlg,self).__init__()
        self.fruit = fruit

        self.fruits = QtGui.QListWidget()
        self.fruits.addItems(fruit)

        btn_add = QtGui.QPushButton("&Add")
        btn_edit = QtGui.QPushButton("&Edit")
        btn_remove = QtGui.QPushButton("&Remove")
        btn_up = QtGui.QPushButton("&UP")
        btn_down = QtGui.QPushButton("&Down")
        btn_sort = QtGui.QPushButton("&Sort")
        btn_close = QtGui.QPushButton("&Close")

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(btn_add)
        vbox.addWidget(btn_edit)
        vbox.addWidget(btn_remove)
        vbox.addWidget(btn_up)
        vbox.addWidget(btn_down)
        vbox.addWidget(btn_sort)
        vbox.addStretch(1)
        vbox.addWidget(btn_close)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.fruits)
        hbox.addLayout(vbox)

        self.setLayout(hbox)
        self.setGeometry(400,400,360,400)
        self.setWindowTitle(u"水果listWidget")

        btn_add.clicked.connect(self.add)
        btn_edit.clicked.connect(self.edit)
        btn_remove.clicked.connect(self.remove)
        btn_up.clicked.connect(self.up)
        btn_down.clicked.connect(self.down)
        btn_sort.clicked.connect(self.sort)
        btn_close.clicked.connect(self.close)



    def add(self):# 添加


        add = FruitDlg("Add fruit",self)
        if add.exec_():
            fruit_added = add.fruit
            self.fruits.addItem(fruit_added)
            print (fruit_added)

    def edit(self):

        row = self.fruits.currentRow()
        fruit = self.fruits.takeItem(row)
        edit = FruitDlg('Edit fruit', fruit.text())
        if edit.exec_():
            print (edit.fruit)
            self.fruits.addItem(edit.fruit)

    def remove(self):
        if QtGui.QMessageBox.warning(self,u"确认",u"确认要删除？",QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel) ==QtGui.QMessageBox.Ok:
            item_deleted = self.fruits.takeItem(self.fruits.currentRow())
            #将读取的值设置为None
            item_deleted = None


    def up(self):

        index = self.fruits.currentRow()

        if index > 0:

            index_new = index - 1

            self.fruits.insertItem(index_new,self.fruits.takeItem(self.fruits.currentRow()))
            self.fruits.setCurrentRow(index_new)

    def down(self):

        index = self.fruits.currentRow()
        if index < self.fruits.count():
            index_new = index + 1
            self.fruits.insertItem(index_new,self.fruits.takeItem(self.fruits.currentRow()))
            self.fruits.setCurrentRow(index_new)

    def sort(self):#排序

        self.fruits.sortItems(QtCore.Qt.AscendingOrder)

    def close(self):
        self.done(0)


class FruitDlg(QtGui.QDialog):
    def __init__(self,title,fruit = None):
        super(FruitDlg,self).__init__()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        label_0 = QtGui.QLabel(title)
        label_0.setWordWrap(True)
        self.fruit_edit = QtGui.QLineEdit(fruit)
        btns = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)

        validator = QtCore.QRegExp(r"[^\s][\w\s]+")#正则表达式
        self.fruit_edit.setValidator(QtGui.QRegExpValidator(validator,self))

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(label_0)
        vbox.addWidget(self.fruit_edit)
        vbox.addWidget(btns)
        self.setLayout(vbox)

        self.fruit = None

    def accept(self):
        self.fruit = unicode(self.fruit_edit.text())

        QtGui.QDialog.accept(self)

    def reject(self):

        QtGui.QDialog.reject(self)


if __name__ =="__main__":
    app = QtGui.QApplication(sys.argv)
    fruit =  ["Banana", "Apple", "Elderberry", "Clementine", "Fig", "Guava", "Mango", "Honeydew Melon",
             "Date", "Watermelon", "Tangerine", "Ugli Fruit", "Juniperberry", "Kiwi",
             "Lemon", "Nectarine", "Plum", "Raspberry", "Strawberry", "Orange"]

    ez= StringListDlg(fruit)
    ez.show()
    app.exec_()



