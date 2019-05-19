from PyQt4 import QtCore, QtGui
import sys

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.resize(720, 480)
        central_widget = QtGui.QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QtGui.QHBoxLayout(central_widget)

        self.text_edit = QtGui.QTextEdit(central_widget)
        layout.addWidget(self.text_edit)

        self.drop_list = QtGui.QListWidget(central_widget)

        self.drop_list.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.drop_list.addItems(['one', 'two', 'three', 'four'])
        layout.addWidget(self.drop_list)
        self.show()

        self.button1=QtGui.QPushButton("Hide-Unhide Items")
        self.button1.clicked.connect(self.hideUnhideItems)
        layout.addWidget(self.button1)

        self.button2=QtGui.QPushButton("Print Selected")
        self.button2.clicked.connect(self.getSelected)
        layout.addWidget(self.button2)

    def getSelected(self):
        self.text_edit.clear()
        self.text_edit.setText((self.drop_list.selectedItems()))

    def hideUnhideItems(self):
        for i in range(self.drop_list.count()):
            item=self.drop_list.item(i)
            if not item.isHidden():
                item.setHidden(True)
            else:
                item.setHidden(False)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    frame = MainWindow()
    sys.exit(app.exec_())