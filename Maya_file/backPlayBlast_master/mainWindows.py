# -*- encoding: utf-8 -*-
import sys
import os
import subprocess
#from qss import uiQss


from PySide import QtGui as QtWidgets
from PySide import QtCore
from PySide import QtGui

#QtCore.QCoreApplication.addLibraryPath(os.path.join(os.path.dirname(QtCore.__file__), "plugins"))
import mouseDragEvent
MAYABATCHPATH = r'C:/Program Files/Autodesk/Maya2018/bin/mayabatch.exe'


class MainView(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MainView, self).__init__(parent)
        self.setWindowTitle(u'场景预览')
        self._mainUI()

    def _mainUI(self):
        resultLButton = QtGui.QPushButton(u'生成预览')
        # self.FileText =QTextEdit(self)
        self.listWidget = mouseDragEvent.My_ListWidget(self)
        self.listWidget.setDragEnabled(True)

        Hlayout2 = QtGui.QHBoxLayout()
        Hlayout2.addStretch(0)
        Hlayout2.addWidget(resultLButton)

        VLayout = QtGui.QVBoxLayout()
        VLayout.addWidget(self.listWidget)
        VLayout.addLayout(Hlayout2)
        self.setLayout(VLayout)
        resultLButton.clicked.connect(self.displayMessage)

    def Run(self):
        maFileList = []
        currentPath = os.path.dirname(__file__)
        publishPath = '%s/mianFunction.py' % currentPath
        melFile = '%s/playBlast.mel' % currentPath
        print "currentPath", currentPath
        print "melFile", melFile
        count = self.listWidget.count()
        for ii in xrange(count):
            maFileList.append(self.listWidget.item(ii).text())
        for ii in maFileList:
            cmd = '"{mayaBatchPath}" -script "{melFile}" "{publishPath}" "{maPath}" "{currentFolder}"'.format(
                mayaBatchPath=MAYABATCHPATH,
                melFile=melFile,
                publishPath=publishPath,
                maPath=ii,
                currentFolder=os.path.dirname(ii),
            )
            print cmd
            subprocess.call(cmd, shell=True)
            print "complate"
        return True
    def displayMessage(self):
        if self.Run():
            QtWidgets.QMessageBox.about(self,"Message",u"拍平完成")
        else:
            QtWidgets.QMessageBox.warning(self,"Error",u"请检查错误")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MainView()
    ex.show()
    sys.exit(app.exec_())





