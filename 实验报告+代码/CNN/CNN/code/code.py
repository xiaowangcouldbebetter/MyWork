import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import glob
import cv2
import seaborn as sns
from skimage.filters import sobel
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow.keras import layers,models
from keras.models import model_from_json
from keras.models import load_model

#resizing image


size = 128

# Capture images and labels into array
# Start by creating empty lists

train_images = []
train_labels = []


for directory_path, _, filenames in os.walk('./data/Dataset/Train/'):
    label = directory_path.split("/")[-1]
    # print(label)
    for filename in filenames:
        img_path = os.path.join(directory_path, filename)
        # print(img_path)

        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (size, size))
        # img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        train_images.append(img)
        train_labels.append(label)

train_images = np.array(train_images)
train_labels = np.array(train_labels)

# Do the same for test images

test_images = []
test_labels = []

for directory_path, _, filenames in os.walk('./data/Dataset/Test/'):
    label = directory_path.split("/")[-1]
    # print(label)
    for filename in filenames:
        img_path = os.path.join(directory_path, filename)
        # print(img_path)

        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (size, size))
        # img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        test_images.append(img)
        test_labels.append(label)

test_images = np.array(test_images)
test_labels = np.array(test_labels)


#Encode labels from text (folder_names) to integers
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit(test_labels)
test_labels_encoded = le.transform(test_labels)
le.fit(train_labels)
train_labels_encoded = le.transform(train_labels)


#Split data into test and train datasets
x_train,y_train,x_test,y_test = train_images,train_labels_encoded,test_images,test_labels_encoded

#Normalize pixel value between 0 and 1
x_train,x_test = x_train/255.0, x_test/255.0

# CNN model building
cnn = models.Sequential([
    # 1st layer or Input layer
    layers.Conv2D(filters=128, kernel_size=(3, 3), activation='relu', input_shape=(128, 128, 3)),
    # Pooling
    layers.MaxPool2D((2, 2)),
    # 2nd layer
    layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu'),
    layers.MaxPool2D((2, 2)),
    # 3rd layer
    layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
    layers.MaxPool2D((2, 2)),
    # 4th layer
    layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
    layers.MaxPool2D((2, 2)),
    # 5th layer
    layers.Conv2D(filters=128, kernel_size=(3, 3), activation='relu'),
    layers.MaxPool2D((2, 2)),
    # Flattening
    layers.Flatten(),
    # Last connection
    layers.Dense(512, activation='relu'),
    # For Binary Classification

    layers.Dense(1, activation='sigmoid')
])

#compiling

cnn.compile(
    optimizer = 'adam',
    loss = 'binary_crossentropy',
    metrics = ['accuracy']
)

#Fitting model
history = cnn.fit(x_train,
        y_train,
        epochs = 12)

print(cnn.summary())

#Write model to drive
cnn.save("./model/cnn_model.h5")
print("Saved model to disk")

# load model
model = load_model('./model/cnn_model.h5')

#Prediction
test_prediction = model.predict(x_test)

test_pre = []
for i in test_prediction:
    if(i >= 0.5):
        test_pre.append(1)
    else:
        test_pre.append(0)
#test_pre

test = le.inverse_transform(test_pre)
print(test)

accuracy = model.evaluate(x_test,y_test)
print("Accuracy: ",accuracy)

#print overall accuracy

from sklearn import metrics
print("Accuracy = ",metrics.accuracy_score(test_labels,test))


import random
n = random.randint(0,x_test.shape[0]-1)
img = x_test[n]
plt.imshow(img);
plt.show()

#predict
input_img = np.expand_dims(img,axis = 0)
# img_new = np.reshape(img,(input_img.shape[0],-1))
img_prediction = model.predict(input_img)
if(img_prediction >= 0.5):
    img_prediction = 1
else:
    img_prediction = 0
img_prediction = le.inverse_transform([img_prediction])
print("The prediction for this image is : ", img_prediction)
print("The actual label for this image is : ", test_labels[n])
