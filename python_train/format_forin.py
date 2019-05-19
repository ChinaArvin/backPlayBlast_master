import os

resolution_folder = "D:/TD_lesson/TDke/td2/shots/010/0010/comp/anim-final"
print "resolution_folder:", resolution_folder
resolutions = [folder for folder in os.listdir(resolution_folder) if os.path.isfile('{}/{}'.format(resolution_folder, folder))]
resolutions2 = [folder for folder in os.listdir(resolution_folder)]
print "resolutions:", resolutions