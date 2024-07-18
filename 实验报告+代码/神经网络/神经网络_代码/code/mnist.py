#导入库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mping 
import math

from multilayer_perceptron import MultilayerPerceptron

import warnings
warnings.filterwarnings("ignore")

#读取原始数据，并进行可视化
data = pd.read_csv('../data/mnist-demo.csv')                    #读取csv文件
numbers_to_display = 25                                         # 指定要展示的数字个数
num_cells = math.ceil(math.sqrt(numbers_to_display))            # 计算画布的行、列数
plt.figure(figsize=(10,10))                                     # 创建一个大小为10x10的画布
for plot_index in range(numbers_to_display):                    # 循环展示每一张图像
    digit = data[plot_index:plot_index+1].values                # 读取一张图像
    digit_label = digit[0][0]                                   # 获取该图像的数字标签
    digit_pixels = digit[0][1:]                                 # 获取该图像的所有像素值
    image_size = int(math.sqrt(digit_pixels.shape[0]))          # 计算该图像的宽和高
    frame = digit_pixels.reshape((image_size,image_size))
    plt.subplot(num_cells,num_cells,plot_index+1)
    plt.imshow(frame,cmap='Greys')                              # 显示该图像
    plt.title(digit_label)
plt.subplots_adjust(wspace=0.5,hspace=0.5)                      # 调整子图之间的间距
plt.show()

#数据处理
train_data = data.sample(frac = 0.8)                            # 将80%的数据作为训练数据
test_data = data.drop(train_data.index)                         # 将20%的数据作为测试数据

train_data = train_data.values                                  # 将训练数据和测试数据转化为numpy数组
test_data = test_data.values

num_training_examples = 5000                                    # 指定训练数据集大小为5000，即使用前5000个样本进行模型训练


x_train = train_data[:num_training_examples,1:]
y_train = train_data[:num_training_examples,[0]]

x_test = test_data[:,1:]                                        # 将测试数据中的输入数据x_test和标签y_test分别提取出来
y_test = test_data[:,[0]]

#构建BP神经网络参数
layers=[784,25,10]                                              # 神经网络层数和每层神经元数
normalize_data = True                                           # 是否对数据进行标准化处理
max_iterations = 500                                            #训练迭代的次数
alpha = 0.1                                                     # 学习率
#调用函数
multilayer_perceptron = MultilayerPerceptron(x_train,y_train,layers,normalize_data) # 训练神经网络，返回训练后的神经网络参数和损失函数的值
(thetas,costs) = multilayer_perceptron.train(max_iterations,alpha)
# 可视化训练过程
plt.plot(range(len(costs)),costs)
plt.xlabel('Grident steps')
plt.xlabel('costs')                                             #损失函数的值
plt.show()                                                      #显示图像

#计算准确率及误差
y_train_predictions = multilayer_perceptron.predict(x_train)# 使用模型对训练集和测试集的数据进行预测
y_test_predictions = multilayer_perceptron.predict(x_test)

train_p = np.sum(y_train_predictions == y_train)/y_train.shape[0] * 100
test_p = np.sum(y_test_predictions == y_test)/y_test.shape[0] * 100
print ('训练集准确率：',train_p)
print ('测试集准确率：',test_p)

#可视化预测模型结果
numbers_to_display = 64 # 需要显示的结果的个数
num_cells = math.ceil(math.sqrt(numbers_to_display))
plt.figure(figsize=(15, 15))
for plot_index in range(numbers_to_display):            # 循环遍历 64 个预测结果，并在对应子图上显示结果的图像和标签
    digit_label = y_test[plot_index, 0]                 # 获取当前图像对应的真实标签
    digit_pixels = x_test[plot_index, :]                # 获取当前图像像素点
    predicted_label = y_test_predictions[plot_index][0]
    image_size = int(math.sqrt(digit_pixels.shape[0]))   # 计算图像的大小
    frame = digit_pixels.reshape((image_size, image_size))# 将图像的像素值转化成一个矩阵
    color_map = 'Greens' if predicted_label == digit_label else 'Reds'# 设置颜色映射方式
    plt.subplot(num_cells, num_cells, plot_index + 1)
    plt.imshow(frame, cmap=color_map)# 调整子图之间的水平和垂直间距
    plt.title(predicted_label)
    plt.tick_params(axis='both', which='both', bottom=False, left=False, labelbottom=False, labelleft=False)# 去除子图上刻度线
plt.subplots_adjust(hspace=0.5, wspace=0.5)# 调整子图之间的水平和垂直间距
plt.show()




