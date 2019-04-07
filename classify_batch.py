'''
读取test目录下所有文件，并将所有图片传入模型函数，并将图片名及判断结果写入csv文件的两列。
'''
# USAGE
# python classify.py --model pokedex.model --labelbin lb.pickle --image examples/charmander_counter.png
# python classify.py -m model.model -l lb.pickle -i img.jpg
# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import cv2
import csv
import os

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-m", "--model", required=True,
# 	help="path to trained model model")
# ap.add_argument("-l", "--labelbin", required=True,
# 	help="path to label binarizer")
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image")
# args = vars(ap.parse_args())

model = load_model("1vgg1000.model")
lb = pickle.loads(open("1vgg1000.pickle", "rb").read())

def write_csv(filename, label):
	path  = "11.csv"
	with open(path,'a+', newline = '') as f:   #单纯a+会每个一行一个空行
		csv_write = csv.writer(f)
		data_row = [filename,label]
		csv_write.writerow(data_row)


def listdir(path, list_name):  #传入存储的list
	for file in os.listdir(path):
		file_path = os.path.join(path, file)
		if os.path.isdir(file_path):
			listdir(file_path, list_name)
		else:
			list_name.append(file_path)    #file_path[5:]将前面的路径去掉，只保留文件名
	#print(list_name)


def predict_cnn(image, model, lb):
	'''
	将预测部分整合为函数，并将结果的标签1/2/3/4/5写入csv文件。
	'''
	# pre-process the image for classification
	filename = str(image)
	model = model
	lb = lb
	image = cv2.imread(image)
	image = cv2.resize(image, (300, 300))
	image = image.astype("float") / 255.0
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)

	proba = model.predict(image)[0]
	idx = np.argmax(proba)
	label = lb.classes_[idx]
	label = "{}: {:.2f}% ".format(label, proba[idx] * 100)
	print("[label]", label)   # [:1]就是标签位
	print(label[0])
	write_csv(filename[12:], label[0])

filelist = []

listdir('test_224224/', filelist)
print(len(filelist))
#print(filelist)
#pbar = ProgressBar().start()
for image_file in filelist:
	#args["image"] = image_file
	print(image_file)
	predict_cnn(image_file, model, lb)
	#os.system("python classify4.py --model model200.model --label lb200.pickle -i " + image_file)

