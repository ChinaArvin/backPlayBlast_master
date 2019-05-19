from shutil import copyfile
copyfile(src, dst)
# src是将要复制的图像的文件路径
# dst是将要复制到的位置
copyfile('./test.txt', '/home/gaosiqi/'+'tmp/test.txt')
#         贴图原路径     另存的路径       图片及上一级文件夹名
