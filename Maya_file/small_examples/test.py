#-*- coding:utf-8 -*-
#######line 支持文件拖拽，并且显示文件筐
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
class MyLineEdit(QLineEdit):
    def __init__(self,parent=None):
        super(QLineEdit,self).__init__(parent)
        ###初始化打开接受拖拽使能
        self.setAcceptDrops(True)

    def dragEnterEvent(self,event):
        event.accept()

    def dropEvent(self, event):
        ###获取拖放过来的文件的路径
        st = str(event.mimeData().urls())
        ########st就是Qt文件的路径。我们将这个路径稍作处理便可以得到我们想要的路径了
        ####### url 统一资源定位符是对可以从互联网上得到的资源的位置和访问方法的一种简洁的表示，是互联网上标准资源的地址。
        #######是互联网上标准资源的地址。互联网上的每个文件都有一个唯一的URL，它包含的信息指出文件的位置以及浏览器应该怎么处理它
        st = st.replace("[PyQt4.QtCore.QUrl(u'file:///","")
        st = st.replace("'), ",",")
        st = st.replace("PyQt4.QtCore.QUrl(u'file:///","")
        st = st.replace("')]","")
        st = st.decode('unicode_escape')
        self.setText(st)
        print(type(st))
        print "drag end"

class MyWindow(QDialog,QWidget):
    def __init__(self,parent = None):
        super(MyWindow,self).__init__(parent)
        self.resize(400,400)
        self.mainlayout = QGridLayout(self)
        self.mylineEdit = MyLineEdit()
        self.mainlayout.addWidget(self.mylineEdit)
        self.mylineEdit.setMinimumHeight(100)
        self.mylineEdit.setText(u"将文件拖拽到这里")

app=QApplication(sys.argv)
window=MyWindow()
window.show()
app.exec_()
