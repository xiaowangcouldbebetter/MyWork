from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
data_url = "iris_train.csv"
df = pd.read_csv(data_url)
X = df.iloc[:,1:5]
y = df.iloc[:,5]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
print ('训练集准确率：', accuracy_score(y_train, clf.predict(X_train)))
print ('测试集准确率：', accuracy_score(y_test, clf.predict(X_test)))