# -*- coding:utf-8 -*-
from PySide import QtGui,QtCore
# from PySide2 import QtGui 
import sys
sys.path.append("E:\pycharm_Code\Maya_file\material_export_import")
import material_export_import


class ButtonLineEdit(QtGui.QLineEdit):
    def __init__(self, parent=None):
        super(ButtonLineEdit, self).__init__(parent)

        self.button = QtGui.QToolButton(self)
        self.button.setIcon(QtGui.QIcon("E:\pycharm_Code\Maya_file\material_export_import/_file.png"))
        self.button.setStyleSheet('border: 0px; padding: 0px;')
        self.button.setCursor(QtCore.Qt.ArrowCursor)

        frameWidth = self.style().pixelMetric(
            QtGui.QStyle.PM_DefaultFrameWidth)
        buttonSize = self.button.sizeHint()

        self.setStyleSheet(
            'QLineEdit {padding-right: %dpx; }' % (buttonSize.width() + frameWidth + 1))
        self.setMinimumSize(max(self.minimumSizeHint().width(), buttonSize.width() + frameWidth * 2 + 2),
                            max(self.minimumSizeHint().height(), buttonSize.height() + frameWidth * 2 + 2))



    def resizeEvent(self, event):
        buttonSize = self.button.sizeHint()
        frameWidth = self.style().pixelMetric(
            QtGui.QStyle.PM_DefaultFrameWidth)
        self.button.move(self.rect().right() - frameWidth - buttonSize.width(),
                         (self.rect().bottom() - buttonSize.height() + 1) / 2)
        super(ButtonLineEdit, self).resizeEvent(event)




class StockDialog(QtGui.QDialog):
    def __init__(self,parent = None):
        super(StockDialog, self).__init__(parent)
        self.setWindowTitle("Material Export Import")
        self.resize(350,140)

        self.listCombBox = QtGui.QComboBox()
        self.listCombBox.insertItem(0,"Export")
        self.listCombBox.insertItem(1,"Import")

        bottomlayout = QtGui.QHBoxLayout()
        bottomlayout.addStretch(20)
        bottomlayout.addWidget(self.listCombBox)

        stack = QtGui.QStackedWidget()
        stack.setFrameStyle(QtGui.QFrame.StyledPanel|QtGui.QFrame.Raised)

        page1 = Page1()
        page2 = Page2()

        stack.addWidget(page1)
        stack.addWidget(page2)

        mainLayout = QtGui.QVBoxLayout()
        # mainLayout.setMargin(10)
        mainLayout.setSpacing(6)
        mainLayout.addWidget(stack)
        mainLayout.addLayout(bottomlayout)

        self.listCombBox.currentIndexChanged.connect(stack.setCurrentIndex)

        self.setLayout(mainLayout)

class Page1(QtGui.QWidget):
    def __init__(self,parent = None):
        super(Page1, self).__init__(parent)

        exportButton = QtGui.QPushButton("Export")
        exportButton.setMaximumWidth(50)
        self.saveFileLineEdit = ButtonLineEdit()

        layout = QtGui.QHBoxLayout(self)
        layout.addWidget(exportButton)
        layout.addWidget(self.saveFileLineEdit)

        self.saveFileLineEdit.button.clicked.connect(self.buttonClicked)
        exportButton.clicked.connect(self.exportFun)

    def displayMessage(self):
        if self.Run():
            QtGui.QMessageBox.about(self,"Message",u"拍平完成")
        else:
            QtGui.QMessageBox.warning(self,"Error",u"请检查错误")

    def exportFun(self):
        if self.saveFileLineEdit.text() == None:
            print "Choice path!!"
        else:
            path = self.saveFileLineEdit.text()
            material_export_import.export(save_path=path)

    def buttonClicked(self):
        s = QtGui.QFileDialog.getSaveFileName(self, "open","../","(*.ma)")
        self.setText(s[0])


class Page2(QtGui.QWidget):
    def __init__(self,parent = None):
        super(Page2, self).__init__(parent)
        importButton = QtGui.QPushButton("Import")
        importButton.setMaximumWidth(50)
        self.fileLineEdit = ButtonLineEdit()

        layout = QtGui.QHBoxLayout(self)
        layout.addWidget(importButton)
        layout.addWidget(self.fileLineEdit)

        self.fileLineEdit.button.clicked.conncet(self.buttonClicked)
        importButton.clicked.connect(self.importFun)

    def importFun(self):
        path  = self.fileLineEdit.text()
        material_export_import.import_connect(path)

    def buttonClicked(self):
        s = QtGui.QFileDialog.getSaveFileName(self, "open","../","(*.ma)")
        self.setText(s[0])


app = QtGui.QApplication(sys.argv)
main = StockDialog()
main.show()
app.exec_()











