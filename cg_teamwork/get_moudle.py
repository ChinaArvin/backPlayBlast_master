#coding=utf-8

import sys, os

sys.path.append(r"C:\cgteamwork_5\bin\base")

from cgtw import *

if __name__=='__main__':

    t_tw=tw()

    print t_tw.info_module("proj_lzw007", "asset").get_module()
    # print t_tw.info_module("proj_lzw007", "asset").get_database()

    t_info_module = t_tw.info_module("proj_lzw007", "asset")

    t_info_module.init_with_filter([ ["asset.type_name","=","chars"], "and",
                                     [ "asset.asset_name", "=","cgtw2"] ])

    print t_info_module.get_distinct_with_filter({"asset.asset_name":"cgtw3","asset.type_name": "chars"})

    print t_info_module.set({'asset.cn_name':"模型"})

    os.system('pause')