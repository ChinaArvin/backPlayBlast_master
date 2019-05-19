# -*- coding: utf-8 -*
import maya.cmds as mc
import shutil
import os


def get_texture_initalpath():
    texture_paths = []
    scence_texture = mc.ls(textures=True)
    print "scence_texture:",scence_texture

    for i in range(len(scence_texture)):
        if ":" and "file" in scence_texture[i]:
            print scence_texture[i]
            if mc.getAttr(scence_texture[i] + ".fileTextureName"):

                texture_path = mc.getAttr(scence_texture[i] + '.fileTextureName')
                texture_paths.append(texture_path)
    print "texture_paths:",texture_paths
    return texture_paths


def creat_newpath(save_aspath):
    texture_paths = get_texture_initalpath()
    if texture_paths:
        for i in range(len(texture_paths)):
            texture_filePath = os.path.dirname(texture_paths[i])
            #print texture_filePath
            flag = '/'
            texture_filePath_name = texture_filePath[texture_filePath.rfind(flag) + 1:]
            texture_name = texture_paths[i][texture_paths[i].rfind(flag) + 1:]
            print "texture_name:",texture_paths[i]
            # print  texture_filePath_name
            # print texture_filePath_name+'\\'+texture_name
            save_aspath =save_aspath.replace("\\","/")
            path = save_aspath+ '/' +texture_filePath_name
            if os.path.exists(path) == 0:
                os.mkdir(path)
            if not os.path.exists("save_aspath+'/'+texture_filePath_name+'/'+texture_name"):
                shutil.copy(texture_paths[i], save_aspath+'/'+texture_filePath_name+'/'+texture_name)
                #         贴图原路径          另存的路径       图片及上一级文件夹名

            texture_namelist = mc.ls(type='file')
            print texture_namelist[i] + '.fileTextureName'
            mc.setAttr(texture_namelist[i] + '.fileTextureName', save_aspath + '/' + texture_filePath_name + '/' + texture_name,
                       type="string")


        if i == len(texture_paths)-1:
            all_reference = mc.ls(r=True, type="reference")
            for r in all_reference:
                reference_path = mc.referenceQuery(r, filename=True)
            scence_name = "re_as_"+reference_path.split("/")[-1].split(".")[0]
            # scence_name = mc.file(q=True, sn=True).split('/')[-1]
            rename_file_path = save_aspath + '/' +scence_name
            mc.file(reference_path, selectAll=True)
            mc.file(rename = rename_file_path)
            mc.file(force=True,es=True,type="mayaAscii")
            print True

