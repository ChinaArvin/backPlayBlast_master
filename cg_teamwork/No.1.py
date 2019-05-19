#coding=utf-8

import sys, os

sys.path.append(r"C:\cgteamwork_5\bin\base")

from cgtw import *

if __name__=='__main__':

    t_tw=tw()

    print t_tw.sys().get_argv_key('Key')
    os.system('pause')
