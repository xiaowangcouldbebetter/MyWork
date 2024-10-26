__author__ = 'xiaowang'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score


# 读取数据
data = pd.read_csv("diabetes.csv")

# 分离特征和目标变量
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# 数据标准化
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 决策树模型拟合
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 预测测试集
y_pred = model.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# 使用PCA进行特征降维
pca = PCA(n_components=2)
X_r = pca.fit_transform(X)

# 可视化决策树分类结果
plt.figure()
colors = ['navy', 'turquoise']
lw = 2
for color, i in zip(colors, [0, 1]):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=.8, lw=lw, label=str(i))
plt.title('xiaowang__PCA of Diabetes dataset')
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.show()