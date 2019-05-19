# -*- encoding: utf-8 -*-
import sys
import math
import os
import maya.mel
import maya.cmds as cmds
print "Function Run..."


def Creat_camera():
    cmds.select(ado=True)
    names = cmds.ls(selection=True)
    object_x = object_y = object_z = radiousValue = 0
    for num in range(len(names)):
        X = cmds.getAttr(names[num] + ".translateX")
        Y = cmds.getAttr(names[num] + ".translateY")
        Z = cmds.getAttr(names[num] + ".translateZ")
        object_x = object_x + X
        object_y = object_y + Y
        object_z = object_z + Z

    aim_x = object_x / len(names)
    aim_y = object_y / len(names)
    aim_z = object_z / len(names)

    for num in range(len(names) - 1):
        X = cmds.getAttr(names[num] + ".translateX")
        Y = cmds.getAttr(names[num] + ".translateY")
        Z = cmds.getAttr(names[num] + ".translateZ")

        baseRadious = math.sqrt((X - aim_x) ** 2 + (Y - aim_y) ** 2 + (Z - aim_z) ** 2)
        if baseRadious > radiousValue:
            radiousValue = baseRadious

    camera_x = aim_x + 6 * radiousValue
    camera_y = aim_y + 6 * radiousValue
    camera_z = 0

    cam_1 = cmds.camera(name='cam_1')
    cmds.move(camera_x, camera_y, camera_z)
    cmds.rotate(-50, 90, 'cam_1')
    cmds.move(aim_x, aim_y, aim_z, 'cam_1.rotatePivot')


def TakeScreen(path,publishPath=""):
    print "TakeScreen have Run..."
    # cmds.file(path, o=1, f=1)
    cmds.file(path, o=1, f=1)
    print "file open "
    videosPath = os.path.dirname(path)
    videosName = os.path.basename(path).split(".")[0]

    Creat_camera()
    cmds.lookThru('cam_1')

    knum_Uni = 100
    knum = int(knum_Uni)
    cmds.playbackOptions(min=1, max=knum)
    name = cmds.ls(selection=True)
    cmds.manipPivot(o=(360, 90, 360))
    cmds.currentTime(1)
    cmds.setKeyframe()
    cmds.setKeyframe()
    cmds.setKeyframe()
    cam_RY = cmds.getAttr(name[0] + ".ry")
    cmds.currentTime(knum / 2)
    cmds.setAttr(name[0] + ".ry", cam_RY + 180.0)
    cmds.setKeyframe()
    cmds.setKeyframe()
    cmds.setKeyframe()
    cmds.currentTime(knum)
    cmds.setAttr(name[0] + ".ry", cam_RY + 360.0)
    cmds.setKeyframe()
    cmds.setKeyframe()
    cmds.setKeyframe()

    movPath = "%s/%s.mov" % (videosPath, videosName)
    print movPath
    cmds.playblast(filename=movPath, format="avi", sequenceTime=0,
                   clearCache=1,
                   viewer=1,
                   showOrnaments=1,
                   fp=4,
                   fo=1,
                   percent=100,

                   quality=100, widthHeight=[1080, 720])


