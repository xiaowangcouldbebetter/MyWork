import pandas as pd
from sklearn.linear_model import SGDRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
train_csv ='trainOX.csv'
train_data = pd.read_csv(train_csv)
train_data.drop(['ID','date','hour'],axis=1,inplace=True)
X = train_data.iloc[:,0:10]
y = train_data.iloc[:,10]
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
reg = make_pipeline(StandardScaler(),SGDRegressor(max_iter=1000, tol=1e-3))
reg.fit(X_train, y_train)
y_val_pre = reg.predict(X_val)
print("Mean squared error: %.2f" % mean_squared_error(y_val, y_val_pre ))