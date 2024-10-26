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

# 预测测试集
y_pred = model.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# 绘制散点图
plt.scatter(range(len(X_test)), y_test, label='True labels', c='blue')
plt.scatter(range(len(X_test)), y_pred, label='Predicted labels', c='red', marker='x')

# 生成用于绘制逻辑函数曲线的数据
x = np.linspace(X_test.min(), X_test.max(), 100)
y_logit = 1 / (1 + np.exp(-(model.intercept_[0] + model.coef_[0][0] * x)))

# 绘制逻辑函数曲线
plt.plot(x, y_logit, label='Logistic function', c='green')

plt.xlabel("Sample Index")
plt.ylabel("Outcome")
plt.title("Logistic Regression: True vs Predicted Labels")
plt.legend()
plt.show()