#coding=utf-8

import sys, os

sys.path.append(r"C:\cgteamwork_5\bin\base")

from cgtw import *

if __name__=='__main__':

    t_tw=tw()

    aa = t_tw.sys().get_sys_database()
    print aa
    t_modile = t_tw.info_module(aa, "asset")

    print t_modile.create({"asset.asset_name":"cgtw2","asset.type_name":"chars"})

    os.system('pause')
