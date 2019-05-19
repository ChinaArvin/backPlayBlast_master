from PyQt4 import QtGui, QtCore
import sys


# http://stackoverflow.com/a/12468386/2052889
class ButtonLineEdit(QtGui.QLineEdit):

    def __init__(self, parent=None):
        super(ButtonLineEdit, self).__init__(parent)

        self.button = QtGui.QToolButton(self)
        self.button.setIcon(QtGui.QIcon("E:\pycharm_Code\Maya_file\material_export_import/file.png"))
        self.button.setStyleSheet('border: 0px; padding: 0px;')
        self.button.setCursor(QtCore.Qt.ArrowCursor)

        frameWidth = self.style().pixelMetric(
            QtGui.QStyle.PM_DefaultFrameWidth)
        buttonSize = self.button.sizeHint()

        self.setStyleSheet(
            'QLineEdit {padding-right: %dpx; }' % (buttonSize.width() + frameWidth + 1))
        self.setMinimumSize(max(self.minimumSizeHint().width(), buttonSize.width() + frameWidth * 2 + 2),
                            max(self.minimumSizeHint().height(), buttonSize.height() + frameWidth * 2 + 2))

        self.button.clicked.connect(self.buttonClicked)

    def resizeEvent(self, event):
        buttonSize = self.button.sizeHint()
        frameWidth = self.style().pixelMetric(
            QtGui.QStyle.PM_DefaultFrameWidth)
        self.button.move(self.rect().right() - frameWidth - buttonSize.width(),
                         (self.rect().bottom() - buttonSize.height() + 1) / 2)
        super(ButtonLineEdit, self).resizeEvent(event)

    def buttonClicked(self):
        print 'You clicked the button!'


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = ButtonLineEdit('search.png')
    win.show()
    sys.exit(app.exec_())