# -*- coding:utf-8 -*-
# 复制图像到另一个文件夹
# 文件所在文件夹
import shutil
import os
file_dir = r'E:\pycharm_Code\python_train\image'
# 创建一个子文件存放文件
name = 'class'
print file_dir + "\\" +  name

# file_list = os.listdir(file_dir)
#
# shutil.copy(r"E:\pycharm_Code\python_train\image\5.jpg",r"E:\pycharm_Code\python_train\newimage")


# for image in file_list:
#
#     #如果图像名为B.png 则将B.png复制到F:\\Test\\TestA\\class
#     if image == "5.png":
#         if os.path.exists(os.path.join(file_dir,'class_name')):
#             shutil.copy(os.path.join(file_dir,image), os.path.join(file_dir, 'class_name'))
#         else:
#             os.makedirs(os.path.join(file_dir,'class_name'))
#             shutil.copy(os.path.join(file_dir, image), os.path.join(file_dir, 'class_name'))
