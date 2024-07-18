import pylab as pl
import pandas as pd
data_url = "iris_train.csv"
df = pd.read_csv(data_url)
y = df.ix[:, 2]
pl.hist(y)
pl.xlabel('data')
pl.show()
