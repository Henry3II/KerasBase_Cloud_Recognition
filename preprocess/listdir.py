# -*- coding: utf-8 -*-  
import os  
  
def listdir(path, list_name):  #传入存储的list
	for file in os.listdir(path):  
		file_path = os.path.join(path, file)  
		if os.path.isdir(file_path):  
			listdir(file_path, list_name)  
		else:  
			list_name.append(file_path[9:])    #将前面的路径去掉，只保留文件名
	print(list_name)

listdir('data_ext/',[])
