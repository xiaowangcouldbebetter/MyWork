import pandas as pd
data_url = "train.csv"
df = pd.read_csv(data_url)
X = df.iloc[:,11:12]
y = pd.get_dummies(X,drop_first = True)
print(y)




