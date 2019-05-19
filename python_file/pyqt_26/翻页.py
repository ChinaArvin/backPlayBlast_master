#-*-coding:utf-8-*-
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
QTextCodec.setCodecForTr(QTextCodec.codecForName('utf8'))


class FirstPage(QDialog):
    def __init__(self):
        super(FirstPage,self).__init__()
        self.fruits =QListWidget()

        btn_add = QPushButton("Add")
        btn_remove = QPushButton("Remove")

        vbox = QHBoxLayout()
        vbox.addWidget(btn_add)
        vbox.addWidget(btn_remove)

        hbox = QVBoxLayout()
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
        if QMessageBox.warning(self,u"确认",u"确认要删除？",
                                     QMessageBox.Ok | QMessageBox.Cancel) == QMessageBox.Ok:
            item_deleted = self.fruits.takeItem(self.fruits.currentRow())
            #将读取的值设置为None
            item_deleted = None

class FruitDlg(QDialog):
    def __init__(self,title,fruit = None):
        super(FruitDlg,self).__init__()

        label_0 = QLabel(title)
        #label_0.setWordWrap(True)
        self.fruit_edit = QLineEdit(fruit)
        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)

        vbox = QVBoxLayout()
        vbox.addWidget(label_0)
        vbox.addWidget(self.fruit_edit)
        vbox.addWidget(btns)
        self.setLayout(vbox)

    def accept(self):

        self.fruit = unicode(self.fruit_edit.text())
        QDialog.accept(self)

    def reject(self):

        QDialog.reject(self)

class SecondPage(QDialog):

    def __init__(self, parent=None):
        super(SecondPage, self).__init__(parent)
        self.MyTable = QTableWidget(5, 4)
        self.MyTable.setHorizontalHeaderLabels([u'姓名',u'身高', u'体重'])

        newItem = QTableWidgetItem(u"崔")
        self.MyTable.setItem(0, 0, newItem)

        newItem = QTableWidgetItem(u"160cm")
        self.MyTable.setItem(0, 1, newItem)

        newItem = QTableWidgetItem(u"45kg")
        self.MyTable.setItem(0, 2, newItem)

        self.MyCombo0 = QComboBox()
        self.MyCombo1 = QComboBox()
        self.MyCombo2 = QComboBox()
        self.MyCombo0.addItem(u"张")
        self.MyCombo0.addItem(u"李")
        self.MyCombo0.addItem(u"王")

        self.MyCombo1.addItem(u"张")
        self.MyCombo1.addItem(u"李")
        self.MyCombo1.addItem(u"王")

        self.MyCombo2.addItem(u"张")
        self.MyCombo2.addItem(u"李")
        self.MyCombo2.addItem(u"王")
        self.MyTable.setCellWidget(1, 0, self.MyCombo0)
        self.MyTable.setCellWidget(2, 0,self.MyCombo1)
        self.MyTable.setCellWidget(3, 0, self.MyCombo2)

        layout = QHBoxLayout()
        layout.addWidget(self.MyTable)
        self.setLayout(layout)

        #主框
class TabWidget(QTabWidget):
    def __init__(self,parent = None):
        super(TabWidget, self).__init__(parent)
        self.setWindowTitle(self.tr("翻页"))
        self.resize(400,300)
        self.addTab(FirstPage(),u"第一页")
        self.addTab(SecondPage(),u"第二页")


app = QApplication(sys.argv)
fruit =  []
ez= TabWidget()
ez.show()
app.exec_()



