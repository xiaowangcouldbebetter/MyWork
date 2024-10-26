__author__ = 'xiaowang'

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score


# 读取数据
data = pd.read_csv("diabetes.csv")

# 分离特征
X = data.drop("Outcome", axis=1)

# 数据标准化
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 使用PCA进行特征降维
pca = PCA(n_components=2)
X_r = pca.fit_transform(X)

# K - means聚类
#kmeans = KMeans(n_clusters=2, random_state=42)
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
y_kmeans = kmeans.fit_predict(X_r)

# 可视化聚类结果
plt.figure()
colors = ['navy', 'turquoise']
lw = 2
for color, i in zip(colors, [0, 1]):
    plt.scatter(X_r[y_kmeans == i, 0], X_r[y_kmeans == i, 1], color=color, alpha=.8, lw=lw, label=str(i))
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.title('xiaowang_K - means ')
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.show()

# 计算轮廓系数
silhouette_avg = silhouette_score(X_r, y_kmeans)
print("K - means：", silhouette_avg)