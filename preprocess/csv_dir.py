
'''
读取CSV标签文件，并将图片目录下的所有图片移到对应标签文件名的目录下。

'''

import os
import re
import csv
import shutil

csv_file = "train.csv"

def listdir(path, list_name):  #传入存储的list
	for file in os.listdir(path):  
		file_path = os.path.join(path, file)  
		if os.path.isdir(file_path):  
			listdir(file_path, list_name)  
		else:  
			list_name.append(file_path[5:])    #将前面的路径去掉，只保留文件名
	#print(list_name)


filename = []
listdir('data/',filename)

with open(csv_file) as file:
	reader = csv.reader(file)
	#print(list(reader))
	for row in reader:
		#print(reader.line_num, row)   #用于获取所有内容
		#print(row)   #输出CSV中每一行的内容
		#print(row[0])	#输出文件名
		#print(row[1])	#输出文件标签
		if row[0] in filename:
			#print(row[0])    #y验证
			if row[1] == '1':
				#print(row[0]+"1_GAOJI")
				shutil.copy('data/'+row[0],'1_GAOJI/')
			if row[1] == '2':
				shutil.copy('data/'+row[0],'2_JUAN')
			if row[1] == '3':
				shutil.copy('data/'+row[0],'3_CENGJI')
			if row[1] == '4':
				shutil.copy('data/'+row[0],'4_JI')
			if row[1] == '5':
				shutil.copy('data/'+row[0],'5_JIAZHUANG')








