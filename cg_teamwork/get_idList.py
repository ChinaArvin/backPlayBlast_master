#coding=utf-8

import sys, os

sys.path.append(r"C:\cgteamwork_5\bin\base")

from cgtw import *

if __name__=='__main__':
        t_tw=tw()
        t_info_module=t_tw.info_module("proj_lzw007", "asset")
        t_info_module.init_with_filter([["asset.type_name","=","chars"]])
        aa =  t_info_module.get_with_filter(["asset.asset_name"],[["asset.type_name","=","chars"]])
        num = 0
        for i in aa:
            if i["asset.asset_name"] == "test2":
                num += 1
            #print num
        if num == 0:
                print t_info_module.create({"asset.asset_name": "test2", "asset.type_name": "chars"})
        #print t_info_module.get_id_list()

        os.system('pause')

