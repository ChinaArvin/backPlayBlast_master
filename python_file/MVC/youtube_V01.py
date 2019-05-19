from PyQt4 import QtCore, QtGui
import sys

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setStyle("cleanlooks")


    data = QtCore.QStringList()
    data << "one" << "two" << "three" << "four" << "five"

    listView = QtGui.QListView()
    listView.show()

    listView2 = QtGui.QListView()
    listView2.show()

    model = QtGui.QStringListModel(data)

    listView.setModel(model)
    listView2.setModel(model)


    comboBox = QtGui.QComboBox()
    comboBox.setModel(model)
    comboBox.show()

    #count = listWidget.count()
    # for i in range(count):
    #     item = listWidget.item(i)
    #     item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)


    sys.exit(app.exec_())