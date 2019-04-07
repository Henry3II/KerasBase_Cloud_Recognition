# coding=utf-8
from PIL import Image
import os
import re

'''
读取目录下的所有图片，并将每个图片调用转换尺寸函数，并将缩小尺寸的每个图片保存到另一个目录下

'''
def fixed_size(infile, width, height, outfile):
	"""按照固定尺寸处理图片"""
	im = Image.open(infile)
	#im = im.convert('RGB')
	out = im.resize((width, height), Image.ANTIALIAS)
	out.save(outfile)

def dirlist(path, allfile):
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        else:
            allfile.append(filepath)
        #print(allfile)
    return allfile

def load_files(rootdir):

    allfile=dirlist(rootdir,[])
    for file in allfile:
            fixed_size(file, 300, 300, file)
            print("=========================Convert Finished: " + str(file) + "============================")


#dirlist("train/mid/",[])
load_files("test_300300/")



