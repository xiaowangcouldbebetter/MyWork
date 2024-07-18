import pandas as pd
import matplotlib.pyplot as plt
data_url = "train.csv"
df = pd.read_csv(data_url)
S=df[df.Survived==1]
D=df[df.Survived==0]
plt.hist(S.iloc[:,9])
#plt.hist(S.iloc[:,5])
plt.hist(D.iloc[:,9])
#plt.hist(S.iloc[:,5])
plt.show()