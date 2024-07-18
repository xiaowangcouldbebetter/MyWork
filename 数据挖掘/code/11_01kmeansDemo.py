from sklearn.cluster import KMeans
import pandas as pd
data_url = "iris_train.csv"
df = pd.read_csv(data_url)
X = df.iloc[:,1:5]
estimator = KMeans(n_clusters=3)#构造聚类器
result = estimator.fit_predict(X)
print(result)