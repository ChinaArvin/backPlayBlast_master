#coding=utf-8

import sys, os

sys.path.append(r"C:\cgteamwork_5\bin\base")

from cgtw import *

if __name__=='__main__':

    t_tw=tw()

    t_info_module = t_tw.info_module("proj_lzw007","asset")
    t_info_module.init_with_filter([["asset.type_name","=","chars"]])