# -*- coding:utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class MainWidget(QMainWindow):
    def __init__(self,parent = None):
        super(MainWidget, self).__init__(parent)
        font = QFont(self.tr("黑体"),12)
        QApplication.setFont(font)

        mainSplitter = QSplitter(Qt.Vertical,self)
        leftText = QTextEdit(self.tr("左窗口"),mainSplitter)
        leftText.setAlignment(Qt.AlignCenter)

        bottomleftText = QTextEdit(self.tr("下窗口"), mainSplitter)
        bottomleftText.setAlignment(Qt.AlignCenter)
        mainSplitter.setStretchFactor(1, 1)
        mainSplitter.setWindowTitle(self.tr("分割窗口"))

        rightSpliter = QSplitter(Qt.Vertical,self)
        rightSpliter.setOpaqueResize(False)
        upText = QTextEdit(self.tr("上窗口"),rightSpliter)
        upText.setAlignment(Qt.AlignCenter)

        bottomText = QTextEdit(self.tr("下窗口"),rightSpliter)
        bottomText.setAlignment(Qt.AlignCenter)
        mainSplitter.setStretchFactor(1,1)
        mainSplitter.setWindowTitle(self.tr("分割窗口"))

        self.setCentralWidget(mainSplitter)

app = QApplication(sys.argv)
main = MainWidget()
main.show()
app.exec_()