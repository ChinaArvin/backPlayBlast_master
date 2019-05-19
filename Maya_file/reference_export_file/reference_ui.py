# -*- coding:utf-8 -*-
import sys
from PySide2 import QtWidgets as QtGui
path = 'E:\pycharm_Code\Maya_file/reference_export_file'
path in sys.path or sys.path.append(path)
import reference_export
reload(reference_export)


class Base_ui(QtGui.QWidget):
    def __init__(self):
        super(Base_ui, self).__init__()
        self.setWindowTitle('Reference Export')
        self.resize(300,100)

        self.savepathButton = QtGui.QPushButton('choice save path')
        self.saveButton = QtGui.QPushButton('Save')
        self.saveLine = QtGui.QLineEdit()

        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.savepathButton)
        layout.addWidget(self.saveLine)
        layout.addWidget(self.saveButton)
        self.setLayout(layout)

        self.savepathButton.clicked.connect(self.open_filepath)
        self.saveButton.clicked.connect(self.chuancan)

    def open_filepath(self):
        dir_path = QtGui.QFileDialog.getExistingDirectory(self, "choose directory", "C:\Users\Administrator\Desktop")
        # dir_path = QtGui.QFileDialog.getSaveFileName(self,r"Save path",r"C:\Users\Administrator\Desktop",r"Maya file(*.ma*.mb)")
        self.saveLine.setText(dir_path)

    def chuancan(self):
        savepath = self.saveLine.text().encode('gb2312')
        reference_export.creat_newpath(savepath.replace('/', '\\'))
        

# app = QtGui.QApplication(sys.argv)
ui = Base_ui()
ui.show()
# sys.exit(app.exec_())