import os

path = r"D:\Maya_film\Maya2018\material_export_and_reconnect\scenes\test.ma"
path = path.replace("\\","/")
flag = "/"
name = path[path.rfind(flag)+1:].split(".")[0]
print name
