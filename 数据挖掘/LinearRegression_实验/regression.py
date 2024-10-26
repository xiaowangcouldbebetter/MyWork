import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score

iris = datasets.load_iris()
X = iris.data[:, :2]  # 只使用前两个特征
y_linear = iris.data[:, 2]  # 线性和非线性回归的目标变量
y_logistic = (iris.target > 1).astype(int)  # 逻辑回归的目标变量，二分类

# 创建多项式特征
poly_features = PolynomialFeatures(degree=2)

# 转换特征
X_poly = poly_features.fit_transform(X)

# 创建线性回归模型
nonlinear_reg = LinearRegression()

# 训练模型
nonlinear_reg.fit(X_poly, y_linear)

# 输出回归方程
print("非线性回归方程: y =", nonlinear_reg.intercept_, "+", nonlinear_reg.coef_[0], "* x1 +", nonlinear_reg.coef_[1], "* x1^2 +", nonlinear_reg.coef_[2], "* x2 +", nonlinear_reg.coef_[3], "* x2^2")

# 可视化
y_pred_nonlinear = nonlinear_reg.predict(X_poly)
plt.scatter(X[:, 0], y_linear, color='blue', label='Actual')
plt.scatter(X[:, 0], y_pred_nonlinear, color='red', label='Predicted')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.legend()
plt.show()

# 计算均方误差
mse_nonlinear = mean_squared_error(y_linear, y_pred_nonlinear)
print("非线性回归均方误差:", mse_nonlinear)