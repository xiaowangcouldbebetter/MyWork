from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import pandas as pd
data_url = "iris_train.csv"
df = pd.read_csv(data_url)
X = df.iloc[:,1:5]
X = StandardScaler().fit_transform(X)
db = DBSCAN(eps=1, min_samples=5).fit(X)
print(db.labels_)