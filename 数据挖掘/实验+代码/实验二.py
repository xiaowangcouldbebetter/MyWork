
#实验二：请利用sklearn库实现具体数据的逻辑回归算法。

# 导入所需的库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import metrics

# 加载数据集
data = load_iris()  # 使用sklearn自带的鸢尾花数据集
iris_features = pd.DataFrame(data.data, columns=data.feature_names)  # 提取数据集的特征并存储到DataFrame中
iris_target = data.target  # 提取数据集的目标值

# 创建包含目标的完整数据集
iris_all = iris_features.copy()  # 复制特征数据集
iris_all['target'] = iris_target  # 添加目标值到完整数据集中

# 仅选择部分数据进行训练和测试
iris_features_part = iris_features.iloc[:100]  # 选择前100行作为训练和测试的特征数据集
iris_target_part = iris_target[:100]  # 选择前100个目标值作为训练和测试的目标数据集

# 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(iris_features_part, iris_target_part, test_size=0.2, random_state=2020)
# 将数据集划分为训练集和测试集，其中测试集占总数据集的20%，设置随机种子以确保结果可重现

# 创建并训练模型
clf = LogisticRegression(random_state=0, solver='lbfgs')  # 创建逻辑回归模型
clf.fit(x_train, y_train)  # 使用训练集训练模型

# 输出模型参数
print('The weight of Logistic Regression:', clf.coef_)  # 打印逻辑回归模型的权重
print('The intercept (w0) of Logistic Regression:', clf.intercept_)  # 打印逻辑回归模型的截距

# 进行预测
train_predict = clf.predict(x_train)  # 对训练集进行预测
test_predict = clf.predict(x_test)  # 对测试集进行预测

# 输出准确率
print('The accuracy of the Logistic Regression on the training set is:', metrics.accuracy_score(y_train, train_predict))  # 打印模型在训练集上的准确率
print('The accuracy of the Logistic Regression on the test set is:', metrics.accuracy_score(y_test, test_predict))  # 打印模型在测试集上的准确率

# 仅选择部分数据进行训练和测试
iris_features_part = iris_features.iloc[:100]
iris_target_part = iris_target[:100]

# 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(iris_features_part, iris_target_part, test_size=0.2, random_state=2020)

# 创建并训练模型
clf = LogisticRegression(random_state=0, solver='lbfgs')
clf.fit(x_train, y_train)

# 输出模型参数
print('The weight of Logistic Regression:', clf.coef_)
print('The intercept (w0) of Logistic Regression:', clf.intercept_)

# 进行预测
train_predict = clf.predict(x_train)
test_predict = clf.predict(x_test)

# 输出准确率
print('The accuracy of the Logistic Regression on the training set is:', metrics.accuracy_score(y_train, train_predict))
print('The accuracy of the Logistic Regression on the test set is:', metrics.accuracy_score(y_test, test_predict))





