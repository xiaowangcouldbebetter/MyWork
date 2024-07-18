#导入库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import svm      #支持向量机模型
from sklearn import metrics  #评估指标
from sklearn.model_selection import train_test_split  #数据集的划分
from sklearn.preprocessing import StandardScaler      #数据集标准化

#1.加载data文件夹里的数据集：威斯康星乳腺肿瘤数据集
data=pd.read_csv("../data/data.csv")


#2.查看样本特征和特征值，查看样本特征值的描述信息。
feature_names=data.columns                     #获取所需特征的名称
print(feature_names)
print('-----------------------------------')
data.info()                                    #返回表格信息
print('-----------------------------------')


#3.进行数据清洗（如删除无用列，将诊断结果的字符标识B、M替换为数值0、1等）。
data.drop('id',axis=1,inplace=True)            #删除无用列id

#将诊断结果diagnosis的字符标识B,M替换为数值0,1等
data['diagnosis']=data['diagnosis'].map({'M':1,'B':0})
print('-----------------------------------')
data.info()
print('-----------------------------------')

#将mean(平均值),se(标准误差),worst(最坏值)分组
feature_mean=list(data.columns[1:11])
feature_se=list(data.columns[11:21])
feature_worst=list(data.columns[21:31])

#4.进行特征选取（方便后续的模型训练）。
sns.countplot(x=data['diagnosis'])             #看整体良性、恶性肿瘤的诊断情况


#用热力图呈现features_mean字段之间的相关性，从而选取特征，构建热力图
corr=data[feature_mean].corr()                   # 计算features_mean字段之间的相关系数
plt.figure(figsize=(10,6))
sns.heatmap(corr,annot=True)                   #使用heatmap()函数创建热力图
plt.show()                                     #展示热力图，show()

#创建一个列表feature_remain，并把特征'radius_mean','texture_mean', 'smoothness_mean','compactness_mean','symmetry_mean', 'fractal_dimension_mean'存入
feature_remain = ['radius_mean','texture_mean', 'smoothness_mean','compactness_mean','symmetry_mean', 'fractal_dimension_mean'] 

#5.进行数据集的划分（训练集和测试集），抽取特征选择的数值作为训练和测试数据。
train,test=train_test_split(data,test_size=0.2)#使用 train_test_split() 方法将数据集 data 划分为训练集 train 和测试集 test。其中参数 test_size=0.2 表示测试集占总数据集的 20%，而剩下的 80% 数据将作为训练集。

#从训练集 train 中抽取 feature_remain 中指定的特征作为训练数据 train_X。
train_X=train[feature_remain]                  #抽取特征选择的数值作为训练和测试数据
train_y=train['diagnosis']                     #将训练集 train 中的 'diagnosis' 列作为训练标签 train_y。
test_X=test[feature_remain]
test_y=test['diagnosis']

#6.进行数据标准化操作（可采用Z-Score规范化数据）。
ss=StandardScaler()
train_X=ss.fit_transform(train_X)              #使用fit_transform()函数对训练数据集(train_X) 进行标准化处理，
test_X=ss.transform(test_X)

#7.配置模型，创建SVM分类器。
model=svm.SVC()

#8.训练模型。
model.fit(train_X,train_y)

#9.模型预测。
pre_y=model.predict(test_X)

#10.模型评估。  
print("准确率:%.2f"%metrics.accuracy_score(pre_y,test_y))
