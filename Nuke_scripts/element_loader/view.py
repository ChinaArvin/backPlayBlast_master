import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
import os
import nuke

class VersionComboBox(QtGui.QComboBox):
    versionChanged = QtCore.Signal(dict)

    def __init__(self, parent=None):
        QtGui.QComboBox.__init__(self, parent)

    def set_value(self, row, sequence,shot,task):
        self._row = row
        self._task = task
        self._sequence = sequence
        self._shot = shot
        self.activated.connect(self.itemChanged)

    def itemChanged(self):
        info = {
            'task': self._task,
            'version': self.currentText(),
            'row': self._row,
            'sequence':self._sequence,
            'shot':self._shot
        }
        self.versionChanged.emit(info)


class ElementLoaderView(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ElementLoaderView, self).__init__()

        self.setLayout(QtGui.QVBoxLayout())
        self.setWindowTitle("Element Loader")
        self.resize(600,260)

        self.project_label = QtGui.QLabel("Project:")
        self.project_name = QtGui.QLineEdit()
        self.project_name.setFixedWidth(70)
        self.sequence_label = QtGui.QLabel("sequence:")
        self.sequence_list = QtGui.QComboBox()
        self.sequence_list.setFixedWidth(70)
        self.shot_label = QtGui.QLabel("shot:")
        self.shot_list = QtGui.QComboBox()
        self.shot_list.setFixedWidth(90)
        self.version_list = QtGui.QComboBox()
        self.version_list.setFixedWidth(70)


        self.shot_layout = QtGui.QHBoxLayout()
        self.shot_layout.addWidget(self.project_label)
        self.shot_layout.addWidget(self.project_name)
        self.shot_layout.addStretch(1)
        self.shot_layout.addWidget(self.sequence_label)
        self.shot_layout.addWidget(self.sequence_list)
        self.shot_layout.addStretch(1)
        self.shot_layout.addWidget(self.shot_label)
        self.shot_layout.addWidget(self.shot_list)
        self.shot_layout.addStretch(2)

        self.layout().addLayout(self.shot_layout)

        self.element_table = QtGui.QTableWidget(0,3)
        self.element_table.setHorizontalHeaderLabels(['task', 'version', 'format'])
        self.element_table.setColumnWidth(2,280)
        self.load_button = QtGui.QPushButton('Load')
        self.load_button.clicked.connect(self.load)

        self.button_layout = QtGui.QVBoxLayout()
        self.button_layout.addWidget(self.load_button)

        self.load_layout = QtGui.QHBoxLayout()
        self.load_layout.addWidget(self.element_table)
        self.load_layout.addLayout(self.button_layout)
        self.layout().addLayout(self.load_layout)

        self.message_box = QtGui.QMessageBox()


    def set_project(self, project_name):
        self.project_name.setText(project_name)

    def set_sequence(self, sequences):
        self.sequence_list.clear()
        self.sequence_list.addItems(sequences)

    def set_shot(self, shots):
        self.shot_list.clear()
        self.shot_list.addItems(shots)


    def clear_table(self):
        for i in range(0, self.element_table.rowCount()):
            self.element_table.removeRow(0)

    def set_task(self, row_count, task):
        # print "task_row_count",row_count
        self.element_table.insertRow(row_count)
        self.element_table.setRowHeight(row_count,50)
        element_item = QtGui.QTableWidgetItem(task)
        element_item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
        element_item.setCheckState(QtCore.Qt.Checked)
        self.element_table.setItem(row_count, 0, element_item)
        # self.element_table.setCellWidget(row_count, 1,version_combo)

    def set_version(self,row_count,versions,task,sequence,shot):
        # print "row_count",row_count
        # print "No.2versions:",versions
        for index in range(row_count+1):
            self.version_combo = VersionComboBox()
            self.version_combo.set_value(row=index, sequence=sequence, shot=shot, task=task)
            for t in versions:
                self.version_combo.addItem(t)
            self.element_table.setCellWidget(row_count,1, self.version_combo)
            self.version_combo.versionChanged.connect(self.set_resolution)

    def set_resolution(self,info):
        self.version = info['version']
        self.task = info['task']
        self.sequence = info['sequence']
        self.shot = info['shot']
        resolutions = self.search_resolution(self.sequence, self.shot, self.task,self.version).keys()
        index =info['row']
        combo = VersionComboBox()
        self.listw = QtGui.QListWidget()
        self.listw.itemSelectionChanged.connect(self.current_name)
        print "current version:",self.version
        if len(resolutions) == 0:
            resolutions = "no resolutions"
            combo.addItem(resolutions)
            self.listw.addItem(resolutions)
        else:
            for t in resolutions:
                combo.addItem(t)
                self.listw.addItem(t)
        self.element_table.setCellWidget(index,2,self.listw)

    def search_resolution(self, sequence, shot, task,version):
        print "search run..."
        project_folder_pattern = 'D:/TD_lesson/TDke/{project}/shots'
        resolution_folder = '{}/{}/{}/{}/{}'.format(project_folder_pattern.format(project="td2"),
                                             sequence,shot,task,version)
        resolutions = [folder for folder in os.listdir(resolution_folder)
                       if os.path.isfile('{}/{}'.format(resolution_folder,folder))]

        dict = {}
        for resolution in resolutions:
            dict[resolution] = '{}/{}'.format(resolution_folder,resolution)

        return dict



    def current_name(self):
        self.filename =  self.lisw.selectedItems()[0].text().encode('utf-8')

    def load(self):
        project_folder_pattern = 'D:/TD_lesson/TDke/{project}/shots'
        resolution_folder = '{}/{}/{}/{}/{}'.format(project_folder_pattern.format(project="td2"),
                                                    self.sequence, self.shot, self.task, self.version)
        filename = self.filename
        filepath = '{}/{}'.format(resolution_folder,filename)
        nuke.scriptReadFile(filepath)





# import sys
# app = QtGui.QApplication(sys.argv)
# ui = ElementLoaderView()
# ui.show()
# sys.exit(app.exec_())
