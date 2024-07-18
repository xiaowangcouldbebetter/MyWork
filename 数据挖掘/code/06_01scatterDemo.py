import pandas as pd
import matplotlib.pyplot as plt
data_url = "iris_train.csv"
df = pd.read_csv(data_url)
x = df.iloc[:,1]
y = df.iloc[:,2]
fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.xlabel('x')
plt.ylabel('y')
ax1.scatter(x,y,c = 'r',marker = 'o')
plt.show()
