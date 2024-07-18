import pandas as pd
#读取文件，存储副本到data，样本ID作为行索引
train = pd.read_csv('Sample_train.csv',index_col='ID')
test = pd.read_csv('test_noLabel.csv',index_col='ID')
print(train.info())
print(test.info())
#由结果知数据不含缺失值
#舍弃无关属性
def drop_useless_attribution(data):
    data.drop('EmployeeNumber',axis=1,inplace=True)  #员工编号对离职没有影响，舍弃
    data.drop('StandardHours',axis=1,inplace=True)  #标准工时全是80，舍弃
    data.drop('Over18',axis=1,inplace=True)  #员工全部成年，舍弃
drop_useless_attribution(train)
drop_useless_attribution(test)
#字符表示的序数型属性
#柱状图分析可知出差越多离职的可能性越大
#train[['Label','BusinessTravel']].groupby(['BusinessTravel']).mean().plot.bar()
#Non-Travel转成0，Travel_Rarely转成1，Travel_Frequently转成2
train['BusinessTravel'] = train['BusinessTravel'].map(
    {'Non-Travel':0,'Travel_Rarely':1,
     'Travel_Frequently':2})
test['BusinessTravel'] = test['BusinessTravel'].map(
    {'Non-Travel':0,'Travel_Rarely':1,
     'Travel_Frequently':2})
#字符表示的二进制属性
#直方图分析可知性别对离职无显著影响，舍弃
train.drop('Gender', axis=1, inplace=True)
test.drop('Gender', axis=1, inplace=True)
#直方图分析可知加班对离职影响十分显著
#train[['Label','OverTime']].groupby(['OverTime']).mean().plot.bar()
#No转换成0，Yes转换成1
train['OverTime'] = train['OverTime'].map(
        {'No': 0, 'Yes': 1})
test['OverTime'] = test['OverTime'].map(
        {'No': 0, 'Yes': 1})

#对字符表示的标称型属性进行哑编码
train = pd.get_dummies(train)
test = pd.get_dummies(test)
print(train.info())
#构造新属性
import numpy as np
def NewAtt(data):
    #40工资提高的百分比与工作投入度之比(比率）
    data['JobInvolvementPerPercentSalaryHike']=data['PercentSalaryHike']/data['JobInvolvement']
    #41工作满意度与工作投入度之比（比率）
    data['JobInvolvementSatisfaction']=data['JobSatisfaction']/data['JobInvolvement']
    #42已婚加班（序数）
    data['MaritalStatus_MarriedOverTime']=np.where(data['MaritalStatus_Married']==1,data['OverTime'],0)
    #43已婚出差（序数）
    data['MaritalStatus_MarriedBusinessTravel']=np.where(data['MaritalStatus_Married']==1,
    data['BusinessTravel'],0)
    #44就职过的公司平均工作年限（比率）
    data['AverageWorkYearsPerCompany']=data['TotalWorkingYears']/(data['NumCompaniesWorked']+1)
NewAtt(train)
NewAtt(test)
#找出相关系数绝对值在[0.8,1)内的所有属性对
corr = train.corr()
#返回满足条件的属性对所在的位置，其中第一个数组是行索引，第二个数组是列索引
corr_where = np.where(corr[corr.abs()<1].abs()>=0.8)
#将行索引和列索引合并成元组，添加到列表中
corr_att_list = []
for i in range(len(corr_where[0])):
    corr_att_list.append((corr_where[0][i],corr_where[1][i]))
print(corr_att_list)
print(train.iloc[:,[6,8]].corr())  #第1组属性的相关系数
print(train.iloc[:,[23,33]].corr())  #第2组属性的相关系数
print(train.iloc[:,[24,25,39]].corr())  #第3组属性的相关系数
def DropCorrAtt(data):
    data.drop(['MonthlyIncome','JobRole_Human Resources','JobRole_Sales Executive'],axis=1,inplace=True)
DropCorrAtt(train)
DropCorrAtt(test)
from sklearn.preprocessing import StandardScaler,MinMaxScaler
#对比率型属性标z-分数规范化
def StdS(data):
    data.iloc[:,[0,2,8,10,14,17,18,19,20,40,41,44]] = \
    StandardScaler().fit_transform(data.iloc[:,[0,2,8,10,14,17,18,19,20,40,41,44]])
StdS(train)
StdS(test)
#对序数型属性最大最小规范化
def MMS(data):
    data.iloc[:, [1, 3, 4, 5, 6, 7, 11, 12,13,15,16,42,43]] = \
        MinMaxScaler().fit_transform(data.iloc[:, [1, 3, 4, 5, 6, 7, 11, 12,13,15,16,42,43]])
MMS(train)
MMS(test)
#将标签赋值给新变量，并从train中移除
train_Label = pd.DataFrame(train['Label'])
train.drop('Label',axis=1,inplace=True)
print(train.info())
