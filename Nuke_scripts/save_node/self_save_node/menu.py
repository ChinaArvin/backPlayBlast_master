import copy
import getpass
import os

import nuke

import user_toolkit

menu = nuke.menu('Nuke')
menu.addCommand('Toolkit/Add User Template',
                lambda: user_toolkit.run(),
                'Shift+Alt+R')

TOOLKIT_ROOT = 'E:/pycharm_Code/TD_scripts/toolkit'
user_name = getpass.getuser()
