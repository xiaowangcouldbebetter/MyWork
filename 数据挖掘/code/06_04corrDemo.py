import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
train_csv ='trainOX.csv'
train_data = pd.read_csv(train_csv)
train_data.drop(['ID','date','hour'],axis=1,inplace=True)
corrmat = train_data.corr()
f, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(corrmat, vmax=0.8, square=True)
plt.show()