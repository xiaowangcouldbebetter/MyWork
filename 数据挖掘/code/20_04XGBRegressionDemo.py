from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import xgboost as xgb
import pandas as pd
train_csv ='trainOX.csv'
train_data = pd.read_csv(train_csv)
train_data.drop(['ID','date','hour'],axis=1,inplace=True)
X = train_data.iloc[:,0:10]
y = train_data.iloc[:,10]
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
reg = xgb.XGBRegressor(max_depth=5, learning_rate=0.1, n_estimators=160, silent=False, objective='reg:linear')
reg.fit(X_train, y_train)
y_val_pre = reg.predict(X_val)
print("Mean squared error: %.2f" % mean_squared_error(y_val, y_val_pre ))