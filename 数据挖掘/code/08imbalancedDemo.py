import pandas as pd
data_url = "diabetes.csv"
df = pd.read_csv(data_url)
X = df.iloc[:,0:8]
y=df.iloc[:,8]
print(X.info())
print("---------------------")
from imblearn.over_sampling import RandomOverSampler
ros = RandomOverSampler(random_state=0)
X_resampled, y_resampled = ros.fit_resample(X, y)
print(X_resampled.info())