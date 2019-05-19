# num = [i for i in range(4) if i >=2]
# print num
# import os
# print os.listdir("E:/pycharm_Code/TD_scripts/toolkit")
import getpass
import os
TOOLKIT_ROOT = 'E:/pycharm_Code/TD_scripts/toolkit'

user_name = getpass.getuser()
if not os.listdir('{}/{}'.format(TOOLKIT_ROOT, user_name)):
    os.rmdir('{}/{}'.format(TOOLKIT_ROOT, user_name))