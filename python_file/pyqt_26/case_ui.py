# -*- coding: utf-8 -*
from PyQt4 import QtCore,QtGui,uic
import sys
window_class,base_class = uic.loadUiType("e:/pycharm_Code/TD_scripts/untitled.ui")


class CaseWindow(window_class,base_class):
    def __init__(self,parent = None):
        super(CaseWindow, self).__init__(parent)
        self.setupUi(self)
def main():
    '''
    '''
    app = QtGui.QApplication(sys.argv)
    window = CaseWindow()
    window.show()

    app.exec_()

if __name__ == '__main__':
    main()
