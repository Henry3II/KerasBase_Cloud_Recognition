# import the necessary packages
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dropout
from keras.layers.core import Dense
from keras import backend as K


class CNN:
	@staticmethod

	def build(width, height, depth, classes):
		# initialize the model along with the input shape to be
		# "channels last" and the channels dimension itself
		model = Sequential()
		inputShape = (height, width, depth)
		chanDim = -1

		# if we are using "channels first", update the input shape
		# and channels dimension
		if K.image_data_format() == "channels_first":
			inputShape = (depth, height, width)
			chanDim = 1

		nb_filters = 32
		# size of pooling area for max pooling
		pool_size = (2, 2)
		# convolution kernel size
		kernel_size = (3, 3)

		model = Sequential()
		"""
		model.add(Convolution2D(nb_filters, kernel_size[0], kernel_size[1],
		                        border_mode='same',
		                        input_shape=input_shape))
		"""
		model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1]),
								padding='same',
								input_shape=inputShape))  # 卷积层1
		model.add(Activation('relu'))  # 激活层
		model.add(Conv2D(nb_filters, (kernel_size[0], kernel_size[1])))  # 卷积层2
		model.add(Activation('relu'))  # 激活层
		model.add(BatchNormalization(axis=chanDim))
		model.add(MaxPooling2D(pool_size=pool_size))  # 池化层
		model.add(Dropout(0.25))  # 神经元随机失活
		model.add(Flatten())  # 拉成一维数据
		model.add(Dense(128))  # 全连接层1
		model.add(Activation('relu'))  # 激活层
		model.add(Dropout(0.5))  # 随机失活
		model.add(Dense(classes))  # 全连接层2
		model.add(Activation('softmax'))  # Softmax评分


		# return the constructed network architecture
		return model