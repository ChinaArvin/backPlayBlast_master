# -*- coding: utf-8 -*-
import sys
from PySide import QtGui

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Menubar')


        self.creatAction()
        self.creatMenus()

    def creatAction(self):

        self.exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self) # 创建一个退出动作,该动作会关闭当前窗口
        self.exitAction.setShortcut('Ctrl+Q') # 自定义快捷键
        self.exitAction.setStatusTip('Exit application') # 状态栏提示
        self.exitAction.triggered.connect(self.close) # 利用信号槽机制,将退出动作和窗口的关闭函数联系起来

        self.statusBar()
    def creatMenus(self):
        #menubar = self.menuBar() # 创建一个菜单栏
        #fileMenu = menubar.addMenu('&File') # 在菜单栏中添加 菜单
        fileMenu = self.menuBar().addMenu(u"文件")
        fileMenu.addAction(self.exitAction) # 将前面创建的exitAction添加到该菜单







def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()