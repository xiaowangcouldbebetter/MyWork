import pandas as pd
from sklearn import preprocessing
data_url = "train.csv"
df = pd.read_csv(data_url)
X = df.iloc[:,4:5]
enc = preprocessing.OrdinalEncoder()
y = enc.fit_transform(X)
print(y)

