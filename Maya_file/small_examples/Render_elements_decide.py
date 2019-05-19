# coding:utf-8
import sys
import imp
import math
import maya.cmds as cmds

try:
    imp.find_module('PySide2')
    from PySide2 import QtCore
    from PySide2 import QtGui
    from PySide2 import QtWidgets
except:
    from PySide import QtGui
    from PySide import QtCore



class Base_UI(QtWidgets.QDialog):
    def __init__(self):
        super(Base_UI, self).__init__()
        self.resize(300, 400)
        self.left_list = QtWidgets.QListWidget()
        self.right_list = QtWidgets.QListWidget()
        self.setWindowTitle("Decide elements")

        self.tip_label = QtWidgets.QLabel(u"显示渲染元素请点击Touch按钮")
        self.decide_button = QtWidgets.QPushButton(u"Touch")

        self.left_label = QtWidgets.QLabel(u"已添加的所有渲染元素")
        self.right_label = QtWidgets.QLabel(u"已启用的渲染元素")

        bottom_layout = QtWidgets.QHBoxLayout()
        bottom_layout.addWidget(self.left_list)
        bottom_layout.addWidget(self.right_list)

        top1_layout = QtWidgets.QHBoxLayout()
        top1_layout.addWidget(self.tip_label)
        top1_layout.addWidget(self.decide_button)

        top2_layout = QtWidgets.QHBoxLayout()
        top2_layout.addWidget(self.left_label)
        top2_layout.addWidget(self.right_label)

        mainlayout = QtWidgets.QVBoxLayout()
        mainlayout.addItem(top1_layout)
        mainlayout.addItem(top2_layout)
        mainlayout.addItem(bottom_layout)
        self.setLayout(mainlayout)

        self.decide_button.clicked.connect(self.Display)

    def Display(self):
        render_elements = cmds.ls(type="VRayRenderElement")
        for render_element in render_elements:

            self.left_list.addItem(render_element)
            name = render_element
            r_e_name = cmds.getAttr(name + ".enabled")
            if r_e_name == 1:
                self.right_list.addItem(render_element)


ui = Base_UI()
ui.show()
