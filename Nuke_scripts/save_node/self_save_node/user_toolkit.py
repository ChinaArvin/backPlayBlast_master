import sys
import os
import getpass
import nuke
from  PySide import QtGui,QtCore
user_name = getpass.getuser()
TOOLKIT_ROOT = "E:/pycharm_Code/TD_scripts/toolkit"

def add_template(template_name):
    root_menu = nuke.menu("Nuke")
    template_menu = 'Toolkit/{}/{}'.format(user_name,template_name)
    if not root_menu.findItem(template_name):
        if not os.path.isdir("{}/{}".format(TOOLKIT_ROOT,user_name)):
            os.mkdir("{}/{}".format(TOOLKIT_ROOT,user_name))
        nuke.nodeCopy()

class AddScriptPannel(QtGui.QDialog):
    def __init__(self,parent=None):
        super(AddScriptPannel, self).__init__(parent)
        self.setLayout(QtGui.QVBoxLayout())
        self.setMaximumHeight(100)
        self.setMinimumWidth(400)

        self.name_layout = QtGui.QHBoxLayout()
        self.tool_name_label = QtGui.QLabel("Template name")
        self.tool_name_edit = QtGui.QLineEdit()
        self.name_layout.addWidget(self.tool_name_label)
        self.name_layout.addWidget(self.tool_name_edit)

        self.button_layout = QtGui.QHBoxLayout()
        self.add_button = QtGui.QPushButton("Add")
        self.cancel_button = QtGui.QPushButton("Cancel")
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.cancel_button)

        self.layout().addLayout(self.name_layout)
        self.layout().addLayout(self.button_layout)

        self.user_name = getpass.getuser()
        self.add_button.clicked.connect(self.add_template)
        self.cancel_button.clicked.connect(self.reject)

    def add_template(self):
        nodes = nuke.selectNodes()
        if not nodes:
            nuke.message("No nodes been selected")
            self.reject()
        template_name = self.tool_name_edit.text()
        if not template_name:
            nuke.message("you should input a template name")
        else:
            add_template(template_name)
            self.tool_name_edit.clear()
            self.accept()


app = QtGui.QApplication(sys.argv)
ui = AddScriptPannel()
ui.show()
sys.exit(app.exec_())