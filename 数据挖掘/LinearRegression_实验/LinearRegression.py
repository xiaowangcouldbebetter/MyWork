__author__ = 'xiaowang'

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# 加载鸢尾花数据集
iris = load_iris()
X = iris.data[:, :2]
y = iris.data[:, 2]

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 线性回归模型拟合
model = LinearRegression()
model.fit(X_train, y_train)

# 获取回归方程的系数和截距
intercept = model.intercept_
slope = model.coef_
linear_regression_equation = "y = {:.2f} + {:.2f}x1 + {:.2f}x2".format(intercept, slope[0], slope[1])
print("xiaowang_Linear regression equation:", linear_regression_equation)

# 预测测试集
y_pred = model.predict(X_test)

# 绘制散点图
plt.scatter(X_test[:, 0], y_test, label='True values')

# 生成用于绘制拟合直线的数据
x_min, x_max = X_test[:, 0].min() - 0.5, X_test[:, 0].max() + 0.5
x_fit = np.zeros((len(np.arange(x_min, x_max, 0.1)), 2))
x_fit[:, 0] = np.arange(x_min, x_max, 0.1)
x_fit[:, 1] = X_test[0, 1]
y_fit = model.predict(x_fit)
plt.plot(x_fit[:, 0], y_fit, color='red', label='Fitted line')

plt.xlabel('Feature 1')
plt.ylabel('Target variable')
plt.title('Linear Regression on Iris Dataset')
plt.legend()
plt.show()