
#实验三： 请利用sklearn库实现一个分类方法和一个聚类方法。并实现可视化

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
from sklearn.metrics import silhouette_score

# 加载鸢尾花数据集
iris = datasets.load_iris()
X = iris.data  # 特征数据
y = iris.target  # 目标数据

# 分类方法：逻辑回归
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # 划分训练集和测试集
scaler = StandardScaler()  # 标准化特征数据
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = LogisticRegression()  # 创建逻辑回归模型
model.fit(X_train, y_train)  # 在训练集上拟合模型
y_pred = model.predict(X_test)  # 在测试集上进行预测
accuracy = accuracy_score(y_test, y_pred)  # 计算分类准确率
print("逻辑回归分类准确率：", accuracy)

# 可视化逻辑回归分类结果
pca = PCA(n_components=2)  # 使用PCA进行特征降维
X_r = pca.fit(X).transform(X)  # 对原始数据进行降维
plt.figure()
colors = ['navy', 'turquoise', 'darkorange']
lw = 2
target_names = iris.target_names
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=.8, lw=lw, label=target_name)  # 绘制散点图
plt.title('PCA of IRIS dataset')  # 设置图表标题
plt.legend(loc='best', shadow=False, scatterpoints=1)  # 设置图例
plt.show()  # 显示图表

# 聚类方法：K-means
kmeans = KMeans(n_clusters=3, random_state=42)  # 创建K-means聚类模型
kmeans.fit(X)  # 在数据上进行聚类
y_kmeans = kmeans.predict(X)  # 获取聚类结果

# 可视化聚类结果
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')  # 绘制散点图
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)  # 标记聚类中心
plt.title('K-means Clustering')  # 设置图表标题
plt.show()  # 显示图表

# 打印轮廓系数
silhouette_avg = silhouette_score(X, y_kmeans)  # 计算轮廓系数
print("K-means：", silhouette_avg)  # 打印轮廓系数
