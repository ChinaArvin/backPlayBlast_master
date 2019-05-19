#coding:utf-8

#
# a="ABCDEFGHIJABCDEFGHIJABCDEF/GHIJ"
# b="/"
# print("在a中查找最后一个b后面的字符:"+a[a.rfind(b)+1:])

# working_file_pattern = ('/Volumes/Seagate/vfxstorage/project/'
#                         '(?P<project>[a-z][a-z0-9]{2})/shots/(?P<sequence>[0-9]{3})/'
#                         '(?P<shot>[0-9]{4})/(?P<task_type>[a-z]+)/(?P<full_task>[a-z0-9-]+)/'
#                         '(?P=project)_(?P=sequence)_(?P=shot)_(?P=full_task)_v(?P<version_number>[0-9]{3}).nk')
# print working_file_pattern

# working_file_pattern = ("D:/NUKE_file/"
#                         "(?P<project>[A-Z]{2})/(?P<comp>[a-z]{4})/"
#                         "(?P<EP>[A-Z0-9]{4})/(?P<shot>[a-z0-9]{7})/"
#                         "(?P=project)_(?P=comp)_(?P=EP)_(?P=shot)_(?P<filename>[a-z]{4}).nk")
#
# rootname = "D:/NUKE_file/GF/comp/EP02/shot050/GF_comp_EP02_shot050_comp.nk"

working_file_pattern = ("D:/NUKE_file/C1_NukeWorld/"
                        "(?P<project>[a-z0-9]{3})/(?P<sequence>[0-9]{3})/"
                        "(?P<shot>[0-9]{4})/(?P<task_type>[a-z]{4})/(?P<version>[a-z0-9]{4})/"
                        "(?P=project)_(?P=sequence)_(?P=shot)_(?P=task_type)_(?P=version).nk")
import os
import re
rootname = "D:/NUKE_file/C1_NukeWorld/td2/010/0010/comp/v003/td2_010_0010_comp_v003.nk"

match = re.match(working_file_pattern,rootname)
# print match.groupdict()
# print os.path.dirname(rootname)

# def A(str,num):
#     if num ==0:
#         print "first step"
#     if num == 1:
#         print "second step"
#
# def B():
#     A("abc",1)
# B()

# !/usr/bin/python
import re

# line = "Cats are smarter than dogs"
#
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if matchObj:
#     print "matchObj.group() : ", matchObj.group()
#     print "matchObj.group(1) : ", matchObj.group(1)
#     print "matchObj.group(2) : ", matchObj.group(2)
# else:
#     print "No match!!"

line = 'asdf fjdk; afed, fjek,asdf, foo'
fields = re.split(r'[;,\s]\s*', line)
# fields = re.split(r'(;|,|\s)\s*', line)
values = fields[::3]
print fields
print values