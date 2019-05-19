import sys, os
# get asset_taskID
sys.path.append(r"C:\cgteamwork_5\bin\base")

from cgtw import *

if __name__=='__main__':
        t_tw=tw()
        t_pipeline = t_tw.pipeline("proj_lzw007")

        print t_pipeline.get_with_module("asset_task",["name"])