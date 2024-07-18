import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings
from sklearn.linear_model import SGDRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
warnings.filterwarnings('ignore')
train_csv ='trainOX.csv'
train_data = pd.read_csv(train_csv)
test_csv ='test_noLabelOX.csv'
test_data = pd.read_csv(test_csv)
train_data.head(10)
train_data.isnull().sum()
import time
def getYear(dt):
    t = time.strptime(dt, '%Y-%m-%d')
    return t.tm_year
def getMonth(dt):
    t = time.strptime(dt, '%Y-%m-%d')
    return t.tm_mon
def getDay(dt):
    t = time.strptime(dt, '%Y-%m-%d')
    return t.tm_mday
def getWeek(dt):
    t = time.strptime(dt,'%Y-%m-%d')
    return t.tm_wday
train_data['year']=train_data['date'].apply(getYear)
train_data['month']=train_data['date'].apply(getMonth)
train_data['day']=train_data['date'].apply(getDay)
train_data['week']=train_data['date'].apply(getWeek)
test_data['year']=test_data['date'].apply(getYear)
test_data['month']=test_data['date'].apply(getMonth)
test_data['day']=test_data['date'].apply(getDay)
test_data['week']=test_data['date'].apply(getWeek)
from scipy.stats import norm
sns.distplot(train_data['Label'], fit=norm)
print("Skewness: %f" % train_data['Label'].skew())
print("Kurtosis: %f" % train_data['Label'].kurt())

from scipy import stats
fig = plt.figure()
res = stats.probplot(train_data['Label'], plot=plt)
train_data[train_data['Label']==0].head(10)

train_data = train_data.drop(train_data[train_data['Label'] == 0].index)
train_data['Label_log'] = np.log(train_data['Label'])
sns.distplot(train_data['Label_log'], fit=norm);
print("Skewness: %f" % train_data['Label_log'].skew())
print("Kurtosis: %f" % train_data['Label_log'].kurt())
res = stats.probplot(train_data['Label_log'], plot=plt)

var = 'DEWP'
data = pd.concat([train_data['Label_log'], train_data[var]], axis=1)
data.plot.scatter(x=var, y='Label_log', ylim=(0, 10));
var = 'TEMP'
data = pd.concat([train_data['Label_log'], train_data[var]], axis=1)
data.plot.scatter(x=var, y='Label_log', ylim=(0, 10));
var = 'Iws'
data = pd.concat([train_data['Label_log'], train_data[var]], axis=1)
data.plot.scatter(x=var, y='Label_log', ylim=(0, 10));
var = 'Ir'
data = pd.concat([train_data['Label_log'], train_data[var]], axis=1)
data.plot.scatter(x=var, y='Label_log', ylim=(0, 10));
var = 'DEWP'
data = pd.concat([train_data['Label_log'], train_data[var]], axis=1)
f, ax = plt.subplots(figsize=(20, 16))
fig = sns.boxplot(x=var, y="Label_log", data=data)
fig.axis(ymin=0, ymax=10);
#correlation matrix
corrmat = train_data.corr()
f, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(corrmat, vmax=0.8, square=True)
k = 5 #number of variables for heatmap
cols_large = corrmat.nlargest(k, 'Label_log')['Label_log'].index
cols_small = corrmat.nsmallest(k, 'Label_log')['Label_log'].index
cols =cols_large.append(cols_small)
cols
cm = np.corrcoef(train_data[cols].values.T)
sns.set(rc = {"figure.figsize":(12,10)})
sns.set(font_scale=1.25)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size':10}, yticklabels=cols.values, xticklabels=cols.values)
plt.show()
train_data['hour']=train_data['hour'].astype('float32')
train_data['DEWP']=train_data['DEWP'].astype('float32')
train_data['TEMP']=train_data['TEMP'].astype('float32')
train_data['PRES']=train_data['PRES'].astype('float32')
train_data['Iws']=train_data['Iws'].astype('float32')
train_data['Is']=train_data['Is'].astype('float32')
train_data['Ir']=train_data['Ir'].astype('float32')
train_data['cbwd_NE']=train_data['cbwd_NE'].astype('float32')
train_data['cbwd_NW']=train_data['cbwd_NW'].astype('float32')
train_data['cbwd_SE']=train_data['cbwd_SE'].astype('float32')
train_data['cbwd_cv']=train_data['cbwd_cv'].astype('float32')
train_data['year']=train_data['year'].astype('float32')
train_data['month']=train_data['month'].astype('float32')
train_data['day']=train_data['day'].astype('float32')
train_data['week']=train_data['week'].astype('float32')
train_data['Label_log']=train_data['Label_log'].astype('float32')

test_data['hour']=test_data['hour'].astype('float32')
test_data['DEWP']=test_data['DEWP'].astype('float32')
test_data['TEMP']=test_data['TEMP'].astype('float32')
test_data['PRES']=test_data['PRES'].astype('float32')
test_data['Iws']=test_data['Iws'].astype('float32')
test_data['Is']=test_data['Is'].astype('float32')
test_data['Ir']=test_data['Ir'].astype('float32')
test_data['cbwd_NE']=test_data['cbwd_NE'].astype('float32')
test_data['cbwd_NW']=test_data['cbwd_NW'].astype('float32')
test_data['cbwd_SE']=test_data['cbwd_SE'].astype('float32')
test_data['cbwd_cv']=test_data['cbwd_cv'].astype('float32')
test_data['year']=test_data['year'].astype('float32')
test_data['month']=test_data['month'].astype('float32')
test_data['day']=test_data['day'].astype('float32')
test_data['week']=test_data['week'].astype('float32')
train_data.columns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# train_data.drop(['date'], axis=1, inplace=True)
y=train_data['Label_log']
var =['hour','DEWP', 'TEMP', 'PRES', 'Iws', 'Is', 'Ir',
       'cbwd_NE', 'cbwd_NW', 'cbwd_SE', 'cbwd_cv', 'year', 'month', 'day',
       'week']
X=train_data[var]
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
#reg = LinearRegression().fit(X_train, y_train)
reg = make_pipeline(StandardScaler(),SGDRegressor(max_iter=1000, tol=1e-3))
reg.fit(X_train, y_train)
y_val_pre = reg.predict(X_val)
y_val1= y_val.reset_index(drop=True)
print("Mean squared error: %.2f" % mean_squared_error(y_val1, y_val_pre ))
df1 = pd.DataFrame (y_val_pre, columns = ['p'])
df1['r'] = y_val
df1.to_csv("test1.csv",encoding = "utf-8",header=1,index=0)

X_test = test_data[var]
y_test=reg.predict(X_test)
y_rel = np.round(np.exp(y_test))
df = pd.DataFrame (y_rel, columns = ['pm2.5'])
df.to_csv("sample.csv",encoding = "utf-8",header=1,index=0)