# -*- coding: utf-8 -*-
"""model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QvrmZplZ8QPEYYCc3qbKcnFTfAnxe_e3
"""

#Google Colab session for training the model

#manually install tensorflowjs
!pip install tensorflowjs

#import libraries
import numpy as np
import tensorflow as tf
import tensorflowjs as tfjs
from tensorflow import keras

#import data from MNIST
(data_train, label_train), (data_test, label_test) = keras.datasets.mnist.load_data()

#preprocessing train and test data (images)
data_train = data_train.reshape([60000, 28, 28, 1])
data_train = data_train / 255.0

data_test = data_test.reshape([10000, 28, 28, 1])
data_test = data_test / 255.0

#convert labels to categorical
label_train = keras.utils.to_categorical(label_train)
label_test = keras.utils.to_categorical(label_test)

#define the model
model = keras.Sequential([
  keras.layers.Flatten(input_shape=(28, 28)),     #layer 0 (input)
  keras.layers.Dense(512, activation='relu'),     #layer 1 (hidden)
  keras.layers.Dense(64, activation='relu'),      #layer 2 (hidden)
  keras.layers.Dense(10, activation='softmax')    #layer 3 (output)
])

#define compile methods
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#training the model
model.fit(data_train, label_train, epochs=4)

#testing the model
loss, acc = model.evaluate(data_test, label_test)
print('Accuracy: ', acc)

#finally saving the model so that it can be opened using JS
tfjs.converters.save_keras_model(model, 'model')