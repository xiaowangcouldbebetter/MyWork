import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
data_url = "train.csv"
df = pd.read_csv(data_url)
imp = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imp.fit(df.iloc[:,5:6])
plt.hist(imp.transform(df.iloc[:,5:6]))
plt.show()
