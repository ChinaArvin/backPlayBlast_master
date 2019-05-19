import sys
sys.path.append(r"D:\TD_lesson\ShotGun\python-api-3.0.40")
from shotgun_api3 import *

sg = Shotgun(
    'https://chinaboylmn.shotgunstudio.com',
     script_name = 'find_one.py',
     api_key = "mvzrkwbfknrjd6dxn-lNaeowq")

# project = sg.find_one("Project",[["name","contains","curd"]],["name"])
# print project

# shots = sg.find("Shot",[["project","is",project]],["code","sg_status_list"])
# for shot in shots:
#     print shot

# sg.create("Shot",{"code":"sh002","project":project})
# print sg.find("Shot",[["code","is","sh002"],["project","is",project]])
# print sg.find_one("Shot",[["code","is","sh002"],["project","is",project]],["sg_status_list","description"])
# sequence = sg.create("Sequence",{"project":project,"code":"seq001"})
# print sequence
# shots = sg.find("Shot",[["project","is",project]])
# for shot in shots:
#     sg.update("Shot",shot['id'],{"sg_status_list":"rdy","sg_sequence":sequence})

