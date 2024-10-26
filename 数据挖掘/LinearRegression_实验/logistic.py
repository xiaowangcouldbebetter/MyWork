__author__ = 'xiaowang'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

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

# 逻辑回归模型拟合
model = LogisticRegression()
model.fit(X_train, y_train)

# 获取回归方程的系数和截距
intercept = model.intercept_[0]
coefficients = model.coef_[0]

# 构建逻辑回归方程
features = data.columns[:-1]
equation = "y = 1 / (1 + np.exp(-({:.2f}".format(intercept)
for coef, feature in zip(coefficients, features):
    equation += "+{:.2f}*{}".format(coef, feature)
equation += "))"
print("Logistic regression equation:", equation)

# 预测测试集
y_pred = model.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# 绘制混淆矩阵
cm = confusion_matrix(y_test, y_pred)
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title("xiaowang_Confusion Matrix")
plt.colorbar()
tick_marks = np.arange(2)
plt.xticks(tick_marks, ["0", "1"])
plt.yticks(tick_marks, ["0", "1"])
plt.xlabel("Predicted label")
plt.ylabel("True label")
plt.show()