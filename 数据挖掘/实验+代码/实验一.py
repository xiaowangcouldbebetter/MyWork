
# 实验一：利用sklearn库实现具体数据的直方图、箱线图、散点图。

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

# 从本地文件加载名为 "iris_train.csv"数据集
iris_df = pd.read_csv('C:/Users/小王/Desktop/text/pythonProject/小王的python/数据挖掘/code/iris_train.csv')  # 使用pandas读取CSV文件

# 提取特征和目标值
data = iris_df.iloc[:, :-1].values  # 提取特征数据
target = iris_df.iloc[:, -1].values  # 提取目标值

# 将目标值转换为数值表示
target_numeric = pd.factorize(target)[0]

# 绘制直方图
plt.figure(figsize=(10, 6))  # 创建一个新的图表，设置大小为10x6英寸
for i in range(data.shape[1]):  # 遍历特征的列数
    plt.hist(data[:, i], bins=30, alpha=0.5, label=iris_df.columns[i])  # 绘制直方图，设置柱数为30，透明度为0.5，添加标签
plt.xlabel('Size')  # 设置x轴标签
plt.ylabel('Frequency')  # 设置y轴标签
plt.title('Histogram of Iris Dataset')  # 设置图表标题
plt.legend()  # 显示图例
plt.show()  # 显示图表

# 绘制箱线图
plt.figure(figsize=(10, 6))  # 创建一个新的图表，设置大小为10x6英寸
plt.boxplot(data, labels=iris_df.columns[:-1])  # 绘制箱线图，设置x轴标签为特征列名
plt.title('Boxplot of Iris Dataset')  # 设置图表标题
plt.show()  # 显示图表

# 绘制散点图
plt.figure(figsize=(10, 6))  # 创建一个新的图表，设置大小为10x6英寸
plt.scatter(data[:, 0], data[:, 1], c=target_numeric, cmap='viridis', s=100)  # 绘制散点图，设置颜色参数为数值表示的目标值，颜色映射为'viridis'，点大小为100
plt.xlabel(iris_df.columns[0])  # 设置x轴标签
plt.ylabel(iris_df.columns[1])  # 设置y轴标签
plt.title('Scatter Plot of Iris Dataset')  # 设置图表标题
plt.colorbar(label=iris_df.columns[-1])  # 显示颜色条，并设置标签
plt.show()  # 显示图表


