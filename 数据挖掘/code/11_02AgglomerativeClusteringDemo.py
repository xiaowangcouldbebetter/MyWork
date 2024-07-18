from sklearn.cluster import AgglomerativeClustering
import pandas as pd
data_url = "iris_train.csv"
df = pd.read_csv(data_url)
X = df.iloc[:,1:5]
clustering = AgglomerativeClustering(linkage= 'average', n_clusters=3)
result = clustering.fit_predict(X)
print(result)

