import re

# working_file = ('D:/TD_lesson/TDke/'
#                  '(?P<project>[a-z][a-z0-9]{2})/shots/(?P<sequence>[0-9]{3})/'
#                  '(?P<shot>[0-9]{4})/(?P<task_type>[a-z]+)/(?P<full_task>[a-z0-9-]+)/'
#                  '(?P=project)_(?P=sequence)_(?P=shot)_(?P=full_task)_v(?P<version_number>[0-9]{3}).nk'
#                 )
#
# rootname = 'D:/TD_lesson/TDke/td2/shots/010/0010/comp/comp-slap/td2_010_0010_comp-slap_v003.nk'
#
# match = re.match(working_file,rootname)
#
# print match.groupdict()

project_folder_pattern = 'D:/TD_lesson/TDke/{project}/shots'
project_folder = project_folder_pattern.format(project="td2")
print project_folder

versions = ['anim-final', 'comp-slap']
for i in versions:
    print i
