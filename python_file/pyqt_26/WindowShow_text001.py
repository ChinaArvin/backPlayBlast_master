#-*-coding:utf-8 -*-
from PySide import QtGui,QtCore
import os


class Window(QtGui.QDialog):
    def __init__(self,parent=None):
        super(Window,self).__init__(parent)
        self.setWindowTitle(u"文件浏览")
        self.resize(1000, 600)

        self._browser1 = FileBrowser()

        '''顶部布局========================================================================='''

        self.aa = QtGui.QWidget(self)

        self.fileButton = QtGui.QPushButton(u'文件',self)
        self.fileButton.setIcon(QtGui.QIcon('Icon/Christmas002.jpg'))
        self.openPrintButton = QtGui.QPushButton(u"计算机", self)
        self.viewButton = QtGui.QPushButton(u"查看",self)
        self.viewButton.setFlat(True)
        self.closeAction = QtGui.QPushButton(u"帮助", self)


        self.fileMenu = QtGui.QHBoxLayout()
        self.fileMenu.addWidget(self.fileButton)
        self.fileMenu.addWidget(self.openPrintButton)
        self.fileMenu.addWidget(self.viewButton)
        self.fileMenu.addWidget(self.closeAction)
        self.fileMenu.addSpacing(800)

        '''中部布局================================================================'''

        self.backButton = QtGui.QPushButton(u"返回")
        self.nextButton = QtGui.QPushButton(u"前进")
        self.upButton = QtGui.QPushButton(u"上移")
        self.outputShow = QtGui.QLineEdit()
        self.searchShow = QtGui.QLineEdit()
        self.searchButton = QtGui.QPushButton(u"搜索")

        self.layout_g = QtGui.QGridLayout()
        self.layout_g.addWidget(self.nextButton,0,0)
        self.layout_g.addWidget(self.backButton,0,1)
        self.layout_g.addWidget(self.upButton,0,2)
        self.layout_g.addWidget(self.outputShow,0,3,1,1)
        self.layout_g.addWidget(self.searchShow,0,4,1,10)
        self.layout_g.addWidget(self.searchButton,0,16)

        '''下部布局=============================================================='''

        self.treeWidgetLayout = QtGui.QVBoxLayout()
        self.treeWidgetLayout.addWidget(self._browser1)


        '''总布局位置============================================================'''

        self.layout_h = QtGui.QVBoxLayout()
        self.layout_h.addLayout(self.fileMenu)
        self.layout_h.addSpacing(80)
        self.layout_h.addLayout(self.layout_g)
        self.layout_h.addLayout(self.treeWidgetLayout)
        self.setLayout(self.layout_h)

        '''链接===================================================================='''

        self.fileButton.clicked.connect(self.showFileMenu)
        self.viewButton.clicked.connect(self.showViewMenu)

    '''显示抛出的窗口函数================================================='''
    def showFileMenu(self):
        self.popup_File = FileMenuDialog(self)
        mouse_xy = self.fileButton.mapToGlobal(self.fileButton.pos())
        x = mouse_xy.x()-20
        y = mouse_xy.y()+13
        self.popup_File.move(x,y)
        self.popup_File.show()

    def showViewMenu(self):
        self.popup_View = ViewMenuDialog(self)
        mouse_xy = self.fileButton.mapToGlobal(self.fileButton.pos())
        x = mouse_xy.x() + 140
        y = mouse_xy.y() + 15
        self.popup_View.move(x, y)
        self.popup_View.show()
        '''实现返回前进函数==========================================='''
    def backFunction(self):
        pass


'''文件下的功能======================================================================='''
class FileMenuDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent=parent)

        self.popup_window = self.setWindowFlags(QtCore.Qt.Popup)

        '''菜单栏===================================================='''
        copyBtn = QtGui.QPushButton(u"复制")
        copyBtn.setIcon(QtGui.QIcon('Icon/8.png'))
        copyToBtn = QtGui.QPushButton(u"复制到")
        pasteBtn = QtGui.QPushButton(u"粘贴")
        pasteBtn.setIcon(QtGui.QIcon('Icon/paste.png'))
        closeBtn = QtGui.QPushButton(u"关闭")
        closeBtn.clicked.connect(self.close)

        self.copyBtn = copyBtn

        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(copyBtn)
        self.layout.addWidget(copyToBtn)
        self.layout.addWidget(pasteBtn)
        self.layout.addWidget(closeBtn)

        self.setLayout(self.layout)


'''查看部分=================================================================================='''
class ViewMenuDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent=parent)

        self.popup_View = self.setWindowFlags(QtCore.Qt.Popup)

        preViewButton_1 = QtGui.QPushButton(u"预览窗格")
        preViewButton_2 = QtGui.QPushButton(u"详细预览窗格")
        GPSButton = QtGui.QPushButton(u"导航预览")
        arrangementButton = QtGui.QPushButton(u"排列方式")
        groupButton = QtGui.QPushButton(u"分组依据")
        addColumnButton = QtGui.QPushButton(u"添加列")
        adjustColumnButton = QtGui.QPushButton(u"调整列")

        '''一级排列========================================='''
        previewLayout = QtGui.QVBoxLayout()
        previewLayout.addWidget(preViewButton_1)
        previewLayout.addWidget(preViewButton_2)

        culumnLayout = QtGui.QVBoxLayout()
        culumnLayout.addWidget(groupButton)
        culumnLayout.addWidget(addColumnButton)
        culumnLayout.addWidget(adjustColumnButton)

        '''二级排列========================================='''
        paneLayout = QtGui.QHBoxLayout()
        paneLayout.addWidget(GPSButton)
        paneLayout.addLayout(previewLayout)

        viewLayout = QtGui.QHBoxLayout()
        viewLayout.addWidget(arrangementButton)
        viewLayout.addLayout(culumnLayout)


        '''总排列==========================================='''
        self.totalLayout = QtGui.QHBoxLayout()
        self.totalLayout.addLayout(paneLayout)
        self.totalLayout.addLayout(viewLayout)
        self.setLayout(self.totalLayout)


'''TreeWidget================================================================================='''
class DirBrowser(QtGui.QTreeWidget):
    def __init__(self, parent=None):
        # QtGui.QTreeWidget.__init__(self, parent=parent)
        super(DirBrowser, self).__init__(parent)
        self.setHeaderLabel(u"此电脑")
        # self.setItemHidden(cc,True)
        self.itemExpanded.connect(self.expand)

        # Add window drives
        for d in self.getDrives():
            # print 'd:',d
            self.item = QtGui.QTreeWidgetItem(self, [d])
            self.item.path = d
            QtGui.QTreeWidgetItem(self.item, '')                   # ?        ?

    '''获取根目录地址======================================================='''

    def getDrives(self):
        result = []
        for d in QtCore.QDir.drives():
            print d.filePath()
            result.append(d.filePath())

        return result

    def expand(self, item):
        if hasattr(item, 'takeChildren'):
            item.takeChildren()                             # ?           ?

        files = os.listdir(item.path)
        files.sort()
        for f in files:
            path = item.path.rstrip('/') + '/' + f          # Python rstrip()删除 string 字符串末尾的指定字符（默认为空格）

            if os.path.isdir(path):                         # 判断路径是否为目录
                newItem = QtGui.QTreeWidgetItem(item, [f])
                newItem.path = path

                QtGui.QTreeWidgetItem(newItem, '')

class FileBrowser(QtGui.QSplitter):
    def __init__(self, parent=None):
        QtGui.QSplitter.__init__(self, parent=parent)
        #self.setWindowTitle('File Browser')

        self._browser = DirBrowser()
        self._files = QtGui.QTreeWidget()
        self._files.setHeaderLabels([u"文件名", u"修改日期", u"大小"])


        self._browser.itemClicked.connect(self.chooseDir)

        self.addWidget(self._browser)
        self.addWidget(self._files)

    def chooseDir(self, item, column):
        self._files.clear()

        files = os.listdir(item.path)
        files.sort()
        for f in files:
            texts = [f, '', '']
            self.ItemHidden = QtGui.QTreeWidgetItem(self._files, texts)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
