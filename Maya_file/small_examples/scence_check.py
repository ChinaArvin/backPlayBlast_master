import maya.cmds as mc

layers = mc.ls(type="displayLayer")
for layer in layers:
    print layer