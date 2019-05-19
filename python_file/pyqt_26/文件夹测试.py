# -*- coding:utf8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
'''
class openFile(QWidget):
    def __init__(self):
        super(openFile, self).__init__()

        self.label = QLabel(u"文件路径")
        self.FileLineEdit = QLineEdit()
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.FileLineEdit)
        self.setLayout(layout)
'''


class Folder(QWidget):
    def __init__(self):
        super(Folder, self).__init__()

        model = QFileSystemModel()
        model.setRootPath('')

        tree = QTreeView()
        list = QListView()
        list.setToolTip("ok")

        tree.setModel(model)
        list.setModel(model)

        list.setSelectionModel(tree.selectionModel())

        tree.doubleClicked.connect(list.setRootIndex)

        leftLayout = QHBoxLayout()
        leftLayout.addWidget(tree)
        rightLayout = QHBoxLayout()
        rightLayout.addWidget(list)
        layout = QGridLayout()
        mainLayout = QGridLayout()
        mainLayout.addLayout(leftLayout,0,0)
        mainLayout.addLayout(rightLayout,0,1)
        mainLayout.addLayout(layout, 0, 2,4,4)
        self.setLayout(mainLayout)

# ______________________top_button________________________
        button1 = QPushButton(u"文件")
        button2 = QPushButton(u"计算机")
        button3 = QPushButton(u"查看")
        button4 = QPushButton(u"帮助")
        button5 = QPushButton(u"前进")
        button6 = QPushButton(u"后退")
        button7 = QPushButton(u"上移")
        button8 = QPushButton(u"搜索")

        label1 = QLineEdit()
        label2 = QLineEdit()

        layout.addWidget(button1, 0, 0)
        layout.addWidget(button2, 0, 1)
        layout.addWidget(button3, 0, 2)
        layout.addWidget(button4, 0, 3)
        layout.addWidget(button5, 4, 0)
        layout.addWidget(button6, 4, 1)
        layout.addWidget(button7, 4, 2)
        layout.addWidget(label1, 4, 3)
        layout.addWidget(label2, 4, 4)
        layout.addWidget(button8, 4, 5)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    folder = Folder()
    folder.show()
    sys.exit(app.exec_())
