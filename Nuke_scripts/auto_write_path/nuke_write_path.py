import os
import re
import sys

#import nuke
from PySide import QtGui
from PySide import QtCore


working_file_pattern = ("D:/NUKE_file/C1_NukeWorld/"
                        "(?P<project>[a-z0-9]{3})/(?P<sequence>[0-9]{3})/"
                        "(?P<shot>[0-9]{4})/(?P<task_type>[a-z]{4})/(?P<version>[a-z0-9]{4})/"
                        "(?P=project)_(?P=sequence)_(?P=shot)_(?P=task_type)_(?P=version).nk")

rootname = "D:/NUKE_file/C1_NukeWorld/td2/010/0010/comp/v003/td2_010_0010_comp_v003.nk"

class writePathPannel(QtGui.QDialog):
    def __init__(self,n,parent = None):
        super(writePathPannel, self).__init__(parent)
        self.setMaximumWidth(400)
        self.setMaximumHeight(100)
        self.rootname = n

        self.project_label = QtGui.QLabel("   Project:")
        self.sequence_label = QtGui.QLabel("Sequence:")
        self.shot_label = QtGui.QLabel("Shot:")
        self.tasktype_label = QtGui.QLabel(" Task Type:")
        self.version_label = QtGui.QLabel("Version:")
        self.filetype_label = QtGui.QLabel("File Type:")
        self.filename_label = QtGui.QLabel(" File Name:")
        self.writepath_label = QtGui.QLabel("Write Path:")

        self.project_line = QtGui.QLineEdit()
        self.project_line.setEnabled(False)
        self.sequence_line = QtGui.QLineEdit()
        self.shot_line = QtGui.QLineEdit()
        self.tasktype_line = QtGui.QLineEdit()
        self.version_line = QtGui.QLineEdit()
        self.filetype_combbox =QtGui.QComboBox()
        texts = ("exr","mov","jpg")
        self.filetype_combbox.addItems(texts)
        self.filename_line = QtGui.QLineEdit()
        self.writepath_line = QtGui.QLineEdit()

        self.okbubtton = QtGui.QPushButton('OK')
        self.cancelbutton = QtGui.QPushButton('Cancel')

        self.line1_layout = QtGui.QHBoxLayout()
        self.line1_layout.addWidget(self.project_label)
        self.line1_layout.addWidget(self.project_line)
        self.line1_layout.addWidget(self.sequence_label)
        self.line1_layout.addWidget(self.sequence_line)
        self.line1_layout.addWidget(self.shot_label)
        self.line1_layout.addWidget(self.shot_line)

        self.line2_layout = QtGui.QHBoxLayout()
        self.line2_layout.addWidget(self.tasktype_label)
        self.line2_layout.addWidget(self.tasktype_line)
        self.line2_layout.addWidget(self.version_label)
        self.line2_layout.addWidget(self.version_line)
        self.line2_layout.addWidget(self.filetype_label)
        self.line2_layout.addWidget(self.filetype_combbox)

        self.line3_layout = QtGui.QHBoxLayout()
        self.line3_layout.addWidget(self.filename_label)
        self.line3_layout.addWidget(self.filename_line)

        self.line4_layout = QtGui.QHBoxLayout()
        self.line4_layout.addWidget(self.writepath_label)
        self.line4_layout.addWidget(self.writepath_line)

        self.line5_layout = QtGui.QHBoxLayout()
        self.line5_layout.addWidget(self.okbubtton)
        self.line5_layout.addWidget(self.cancelbutton)

        self.main_layout = QtGui.QVBoxLayout()
        self.main_layout.addLayout(self.line1_layout)
        self.main_layout.addLayout(self.line2_layout)
        self.main_layout.addLayout(self.line3_layout)
        self.main_layout.addLayout(self.line4_layout)
        self.main_layout.addLayout(self.line5_layout)
        self.setLayout(self.main_layout)

        self.okbubtton.clicked.connect(self.showModalDialog)
        self.cancelbutton.clicked.connect(self.reject)
        self.filetype_combbox.currentIndexChanged.connect(self.combChange)

        self.info = {}
        self.parseParameters()
        self.combChange()
        # if self.match:
        #     self.combChange(str(self.filetype_combbox.currentText()))  # exr


    def parseParameters(self):
        match = re.match(working_file_pattern,self.rootname)

        if match:
            self.info = match.groupdict()
            self.project_line.setText(self.info['project'])
            self.sequence_line.setText(self.info['sequence'])
            self.shot_line.setText(self.info['shot'])
            self.tasktype_line.setText(self.info['task_type'])
            self.version_line.setText(self.info['version'])

            self.match = True
        else:
            nuke.message('Umatch')
            self.match = False

    def combChange(self):

        if not self.info:
            return
        if self.filetype_combbox.currentText() == "mov":
            # print "111"
            self.info['filename'] = os.path.basename(self.rootname).replace('.nk','.move')
            self.filename_line.setText(self.info['filename'])
        elif self.filetype_combbox.currentText() == "exr":
            # print "222"
            self.info['filename'] = os.path.basename(self.rootname).replace(".nk",".%04d.exr")
            self.filename_line.setText(self.info['filename'])
        elif self.filetype_combbox.currentText() == "jpg":
            self.info['filename'] = os.path.basename(self.rootname).replace(".nk",".%04d.jpg")
            self.filename_line.setText(self.info['filename'])

        writepath = ("D:/NUKE_file/C1_NukeWorld/" 
                    "{project}/{sequence}/{shot}/{task_type}/{version}/{filename}").format(**self.info)
        self.writepath_line.setText(writepath)

    def showModalDialog(self):
            n = nuke.selectedNode()
            write = nuke.nodes.Write()
            write.setInput(0,n)
            write['file'].fromUserText(self.writepath_line.text())
            if not os.path.isdir(os.path.dirname(write['file'].value())):
                os.makedirs(os.path.dirname(write['file'].value()))



if __name__ == '__main__':
    n = nuke.root().name()
    if n[-3:] == ".nk":
        w = nuke.selectedNode()
        wp = writePathPannel(n)
        if wp.match:
            # print "11111"
            wp.show()
    else:
        nuke.message('Nuke script unsaved')


