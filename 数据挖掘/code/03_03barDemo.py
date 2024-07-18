import pandas as pd
import matplotlib.pyplot as plt
data_url = "train.csv"
df = pd.read_csv(data_url)
#sex = df.groupby('Sex')['Survived'].sum()
sexNew =  df.groupby(['Sex','Survived'])['Survived'].count().unstack()
sexNew.plot(kind='bar')
plt.show()