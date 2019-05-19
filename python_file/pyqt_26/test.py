#-*-coding:utf-8-*-
import sys
from PyQt4 import QtGui,QtCore
QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName('utf8'))

class FirstPage(QtGui.QDialog):
    """
    主对话框
    """
    def __init__(self,fruit):
        super(FirstPage,self).__init__()
        self.fruit = fruit
        self.fruits = QtGui.QListWidget()
        #self.fruits.addItems(fruit)

        btn_add = QtGui.QPushButton("Add")
        btn_remove = QtGui.QPushButton("Remove")

        vbox = QtGui.QHBoxLayout()
        vbox.addWidget(btn_add)
        vbox.addWidget(btn_remove)
        #vbox.addStretch()
        hbox = QtGui.QVBoxLayout()
        hbox.addWidget(self.fruits)
        hbox.addLayout(vbox)

        self.setLayout(hbox)
        self.setGeometry(400,400,360,400)
        self.setWindowTitle(self.tr("listWidget"))

        btn_add.clicked.connect(self.add)
        btn_remove.clicked.connect(self.remove)



    def add(self):# 添加


        add = FruitDlg("input",self)
        if add.exec_():
            fruit_added = add.fruit
            self.fruits.addItem(fruit_added)
            print (fruit_added)


    def remove(self):
        if QtGui.QMessageBox.warning(self,u"确认",u"确认要删除？",QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel) ==QtGui.QMessageBox.Ok:
            item_deleted = self.fruits.takeItem(self.fruits.currentRow())
            #将读取的值设置为None
            item_deleted = None



class FruitDlg(QtGui.QDialog):
    def __init__(self,title,fruit = None):
        super(FruitDlg,self).__init__()
        #self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        label_0 = QtGui.QLabel(title)
        label_0.setWordWrap(True)
        self.fruit_edit = QtGui.QLineEdit(fruit)
        btns = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)

        #validator = QtCore.QRegExp(r"[^\s][\w\s]+")#正则表达式
        #self.fruit_edit.setValidator(QtGui.QRegExpValidator(validator,self))

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

class SecondPage(QtGui.QDialog):
    def __init__(self, parent=None):
        super(SecondPage, self).__init__(parent)
       # self.setStyleSheet("background: red")


class TabWidget(QtGui.QTabWidget):
    def __init__(self,parent = None):
        super(TabWidget, self).__init__(parent)
        self.setWindowTitle(self.tr("翻页"))
        self.resize(400,300)
        self.addTab(FirstPage(fruit),self.tr("第一页"))
        self.addTab(SecondPage(),self.tr("第二页"))


app = QtGui.QApplication(sys.argv)
fruit =  []
ez= TabWidget()
ez.show()
app.exec_()



