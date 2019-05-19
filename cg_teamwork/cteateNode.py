#coding=utf-8

import sys, os

sys.path.append(r"C:\cgteamwork_5\bin\base")

from cgtw import *

if __name__=='__main__':

        t_tw=tw()
        account_id = t_tw.sys().get_account_id()
        t_module=t_tw.task_module("proj_big", "asset_task")
        print t_module
#
#         t_module.init_with_id(account_id)
#
# #        print t_module.create_note("create note test")
#         print t_module.get_note_with_task_id(["text"])
