# -*- coding: utf-8 -*-  
import os  
  
def listdir(path, list_name):  
	for file in os.listdir(path):  
		file_path = os.path.join(path, file)  
		if os.path.isdir(file_path):  
			listdir(file_path, list_name)  
		else:  
			list_name.append(file_path[9:]) 
	print(list_name)

listdir('data_ext/',[])
