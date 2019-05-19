# coding:utf-8
import maya.cmds as mc
import shutil
import json
import os

list = mc.ls(type="shadingEngine")
# print list
SG_lists = []
material_object_dict = {}
for SG_list in list:
    if "SG" in SG_list:
        SG_lists.append(SG_list)
# print SG_lists

for material_nameSG in SG_lists:
    material_name = material_nameSG.replace("SG", "")
    # print material_name
    mc.hyperShade(objects=material_name)
    objects = mc.ls(sl=True, long=True)
    # print objects
    for object in objects:
        material_object_dict[object] = material_nameSG

# print material_object_dict
if material_object_dict == None:
    print "No material !!!"
else:
    mc.select(SG_lists, ne=True)

scence_texture = mc.ls(textures=True)
# print scence_texture
init_texture_path = []
def get_texture_initalpath(num=0):
    num += 1
    # print num
    # texture_pathss = []
    for i in range(len(scence_texture)):
        if "file" in scence_texture[i]:
            print "scence_texture",scence_texture[i]
            if mc.getAttr(scence_texture[i] + ".fileTextureName"):
                texture_path = mc.getAttr(scence_texture[i] + '.fileTextureName')
                print "texture_paths", texture_path
                # texture_pathss.append(texture_path)
                if num <=1:
                    init_texture_path.append(texture_path)


def creat_texture_newpath(save_aspath):
    get_texture_initalpath()
    texture_paths = init_texture_path
    # texture_namelist = mc.ls(type='file')
    # print texture_namelist
    if len(texture_paths) != 0:
        # print "texture_paths",texture_paths
        for i in range(len(texture_paths)):

            texture_filePath = os.path.dirname(texture_paths[i])

            flag = '/'
            texture_filePath_name = texture_filePath[texture_filePath.rfind(flag) + 1:]
            texture_name = texture_paths[i][texture_paths[i].rfind(flag) + 1:]
            # print "texture_name:", texture_filePath_name
            save_aspath = save_aspath.replace("\\", "/")
            path1 = save_aspath + '/' + texture_filePath_name
            # print "path1:", path1
            if os.path.exists(path1) == 0:
                os.mkdir(path1)

            if not os.path.exists("save_aspath+'/'+texture_filePath_name+'/'+texture_name"):
                if texture_paths[i] == save_aspath + '/' + texture_filePath_name + '/' + texture_name:
                    print "path have correct"
                else:
                    shutil.copy(texture_paths[i], save_aspath + '/' + texture_filePath_name + '/' + texture_name)

            # print scence_texture[i] + '.fileTextureName'
            mc.setAttr(scence_texture[i] + '.fileTextureName',
                       save_aspath + '/' + texture_filePath_name + '/' + texture_name,
                       type="string")


def set_texture_path_back():
    print "texture_paths:",init_texture_path
    if init_texture_path:
        for i in range(len(init_texture_path)):
            #print "path:",texture_paths[i]
            texture_namelist = mc.ls(type='file')
            mc.setAttr(texture_namelist[i] + '.fileTextureName', init_texture_path[i],
                       type="string")


def export(save_path):
    path = os.path.dirname(save_path)
    if material_object_dict != None:
        creat_texture_newpath(save_aspath=path)
        mc.file(save_path, options="v=0", type="mayaAscii", pr=True, es=True)
        set_texture_path_back()

        with open(path + "/test.json", "w") as f:
            f.write(json.dumps(material_object_dict, indent=4))
    else:
        print "Error!!!"


def import_connect(save_path):
    flag = '/'
    name = save_path[save_path.rfind(flag) + 1:].split(".")[0]
    path = os.path.dirname(save_path)
    with open(path + "/test.json", "r") as f:
        SG_dict = json.load(f)

    for key in SG_dict.keys():
        SG_dict[key] = name + ":" + SG_dict[key]
        # print "SG_dict[key]:",SG_dict[key]
        if mc.objExists(SG_dict[key]):
            continue
        mc.file(save_path, i=True, type="mayaAscii", ignoreVersion=True, ra=True, mergeNamespacesOnClash=False,
                namespace=name, options="v=0", pr=True, importTimeRange="combine")

    for key in SG_dict.keys():
        # print "key:" ,key
        mc.select(key, r=True)
        mc.sets(e=True, forceElement=SG_dict[key])



