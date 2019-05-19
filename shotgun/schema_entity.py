# coding:utf-8
import sys
sys.path.append(r"D:\TD_lesson\ShotGun\python-api-3.0.40")
from shotgun_api3 import *

sg = Shotgun(
    'https://chinaboylmn.shotgunstudio.com',
     script_name = 'schema_entity.py',
     api_key ="a0-jjrstjqmvEaotrszqfzljt")

# --------------Entity-------------------------------
# for entity in sg.schema_entity_read().keys():
#     if "camera" in entity.lower():
#         print entity

# --------------find camera lens----------------------------------
# print sg.find("CustomEntity01",[["code","is","50mm f1.4"]])
project = sg.find_one("Project",[["name","is","Online Training"]])
schema = sg.schema_entity_read(project_entity = project)
# for entity in sorted(schema.keys()):
#      print entity
# print schema["CustomEntity01"]
# -----------------资产下所有字段----------------------------------
asset_schema = sg.schema_field_read("Asset",project_entity = project)
# for field in sorted(asset_schema.keys()):
#     print field
# for field in sorted(asset_schema["sg_asset_type"].keys()):
#     print field
# print asset_schema['sg_asset_type']['name']

# --------------------find files---------------------------------------
# print sg.find_one("Attachment",[["id","is",558]],["this_file"])
# version_schema = sg.schema_field_read("Version")
# for field in version_schema.keys():
#     if "upload" in field.lower():
#         print field

# -----------------------------------------Upload-----------------------------------------------------------------------
# version = sg.create("Version",{"project":project})
# print version["id"]
# attachment_id = sg.upload("Version",version["id"],"C:/Users/86131/Desktop/test.mov",field_name = "sg_uploaded_movie")
# my_file = sg.find_one("Attachment",[["id","is",attachment_id]],["this_file"])
# print my_file["this_file"]["url"]

# --------------------------------------DOWNLOAD------------------------------------------------------------------------

# version = sg.find_one("Version",[["id","is",6969]],["image","filmstrip_image"])
# print version['filmstrip_image']
# sg.download_attachment({"url":version["image"]},file_path = r'C:/Users/86131/Desktop/image .jpg')

# lens = sg.find_one("CustomEntity01",[["code","contains","85"]],["sg_image_manual"])
# attachment = lens["sg_image_manual"]
# attachment_rate = sg.find_one("Attachment",[["id","is",attachment['id']]],["this_file","file_size"])
# print "Downloading file %s (%s kilobytes)..." % (attachment_rate['this_file']['name'],attachment_rate["file_size"])
# sg.download_attachment(attachment['id'],file_path = 'C:/Users/86131/Desktop/%s' % attachment['name'])


version = sg.find_one('Version',[["id","is",6983]],["image"])
url = version["image"]
print url
print version['id']
# sg.download_attachment({"url":url},file_path = 'C:/Users/86131/Desktop/version_%s_thumb.jpg' % version["id"])
downloaded_file = sg.download_attachment({"url":"%s/thumbnail/full/Version/%s" % (sg.base_url,version['id'])},
                                         file_path = "C:/Users/86131/Desktop/version_%s_thumb_orig" % version['id'])
import imghdr
new_file_path = "".join([downloaded_file,".",imghdr.what(downloaded_file)])
import os
os.rename(downloaded_file,new_file_path)
print new_file_path
