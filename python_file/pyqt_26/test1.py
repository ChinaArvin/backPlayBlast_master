from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

app = QApplication(sys.argv)
b = QPushButton("Hello Kitty!")
b.show()
app.connect(b, SIGNAL("clicked()"), app, SLOT("quit()"))

widget = QWidget()
widget.resize(300,300)
widget.setWindowTitle('LMN')
widget.show()
app.exec_()   
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

app = QApplication(sys.argv)
b = QPushButton('cxt')
b.show()
app.connect(b,SIGNAL("clicked()") , app , SLOT("quit()"))

widget = QWidget()
widget.resize(300,300)
widget.setWindowTitle('LMN')
widget.show()
sys.exit(app.exec_())
'''