import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
from sklearn.impute import SimpleImputer
data_url = "train.csv"
df = pd.read_csv(data_url)
imp = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imp.fit(df.iloc[:,5:6])
pl.boxplot(imp.transform(df.iloc[:,5:6]))
pl.xlabel('data')
pl.show()