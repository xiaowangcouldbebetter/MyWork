import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.neighbors import KNeighborsClassifier

#加载文件
CKD_dataset = pd.read_csv("C:/Users/小王/Desktop/text/pythonProject/实验报告+代码/KNN（慢性肾病）/KNN/data/kidney_disease.csv", header=0, na_values="?")
print(CKD_dataset.head(10))

# 预处理用于训练分类器的数据
print(CKD_dataset.info())               # 打印数据集的基本信息
print(CKD_dataset.columns)              # 打印数据集的列名
print(CKD_dataset.describe())           # 打印数据集的统计信息
print(CKD_dataset.shape)                # 打印数据集的形状
print(CKD_dataset.head().T)             # 打印数据集的前五行，并将它们转置为行列互换的形式，以便更容易查看每个样本的特征和标签


#清理数据用于训练分类器
cols_names = {"bp": "blood_pressure",
              "sg": "specific_gravity",
              "al": "albumin",
              "su": "sugar",
              "rbc": "red_blood_cells",
              "pc": "pus_cell",
              "pcc": "pus_cell_clumps",
              "ba": "bacteria",
              "bgr": "blood_glucose_random",
              "bu": "blood_urea",
              "sc": "serum_creatinine",
              "sod": "sodium",
              "pot": "potassium",
              "hemo": "haemoglobin",
              "pcv": "packed_cell_volume",
              "wc": "white_blood_cell_count",
              "rc": "red_blood_cell_count",
              "htn": "hypertension",
              "dm": "diabetes_mellitus",
              "cad": "coronary_artery_disease",
              "appet": "appetite",
              "pe": "pedal_edema",
              "ane": "anemia"}

CKD_dataset.rename(columns=cols_names, inplace=True)
print(f"\nSo we have {CKD_dataset.shape[1]} columns and {CKD_dataset.shape[0]} instances")

# Change to Numerical Dtyp
# 将数据集中的三个特征（red_blood_cell_count，packed_cell_volume和white_blood_cell_count）的数据类型转换为方便机器学习的数字类型
CKD_dataset['red_blood_cell_count'] = pd.to_numeric(CKD_dataset['red_blood_cell_count'], errors='coerce')
CKD_dataset['packed_cell_volume'] = pd.to_numeric(CKD_dataset['packed_cell_volume'], errors='coerce')
CKD_dataset['white_blood_cell_count'] = pd.to_numeric(CKD_dataset['white_blood_cell_count'], errors='coerce')

# Drop id Column as it is seems to be an unique identifier for each row
# 删除了数据中的"ID"列
CKD_dataset.drop(["id"], axis=1, inplace=True)

# Checking missing values
# 调用"isnull()"方法检查并统计数据中缺失值的数量，"sort_values()"方法将其按降序排列
CKD_dataset.isnull().sum().sort_values(ascending=False)

# Replace incorrect values
# 通过"replace()"方法将数据中出现的一些错误的值做了替
CKD_dataset['diabetes_mellitus'] = CKD_dataset['diabetes_mellitus'].replace(
    to_replace={'\tno': 'no', '\tyes': 'yes', ' yes': 'yes'})
CKD_dataset['coronary_artery_disease'] = CKD_dataset['coronary_artery_disease'].replace(to_replace='\tno', value='no')
CKD_dataset['classification'] = CKD_dataset['classification'].replace(to_replace='ckd\t', value='ckd')

# Convert nominal values to binary values
# 使用replace替换“?”
CKD_dataset.replace("?", np.NaN, inplace=True)
conv_value = {"red_blood_cells": {"normal": 1, "abnormal": 0},
              "pus_cell": {"normal": 1, "abnormal": 0},
              "pus_cell_clumps": {"present": 1, "notpresent": 0},
              "bacteria": {"present": 1, "notpresent": 0},
              "hypertension": {"yes": 1, "no": 0},
              "diabetes_mellitus": {"yes": 1, "no": 0},
              "coronary_artery_disease": {"yes": 1, "no": 0},
              "appetite": {"good": 1, "poor": 0},
              "pedal_edema": {"yes": 1, "no": 0},
              "anemia": {"yes": 1, "no": 0},
              "classification": {"ckd": 1, "notckd": 0}}
CKD_dataset.replace(conv_value, inplace=True)

# Fill null values with mean value of the respective column
#使用"fillna()"方法将数据中的缺失值填充为每个列的平均值
CKD_dataset.fillna(round(CKD_dataset.mean(), 2), inplace=True)

# Save the final data cleaning
# 将数据集保存到指定路径。
CKD_dataset.to_csv("C:/Users/小王/Desktop/text/pythonProject/实验报告+代码/KNN（慢性肾病）/KNN/data/kidney_disease_final.csv", sep=',', index=False)


#分类
# Classifies


def import_data():
    kidney_disease_dataset = pd.read_csv('C:/Users/小王/Desktop/text/pythonProject/实验报告+代码/KNN（慢性肾病）/KNN/data/kidney_disease_final.csv', sep=',', header=0)

    # 打印数据集形状
    print("Dataset Lenght: ", len(kidney_disease_dataset))
    print("Dataset Shape: ", kidney_disease_dataset.shape)

    # 打印数据集观察结果
    return kidney_disease_dataset


# Split Training/Testing Data

# 将数据集分为训练集和测试集的过程，并将其作为函数split_dataset()的结果返回
def split_dataset(kidney_disease_dataset):
    # Seperating the target variable
    X = kidney_disease_dataset.values[:, 0:24]
    Y = kidney_disease_dataset.values[:, -1]

    # 将数据集拆分为训练和测试
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.3, random_state=100)

    return X, Y, X_train, X_test, y_train, y_test

# 设计三个分类器分别基于基尼函数的决策树、随机森林、k近邻
def train_using_gini(X_train, X_test, y_train):
    # 创建分类器的对象
    clf_gini = DecisionTreeClassifier(criterion="gini",
                                      random_state=100, max_depth=3, min_samples_leaf=5)
    # 进行训练
    clf_gini.fit(X_train, y_train)

    return clf_gini


def train_using_rfc(X_train, X_test, y_train):
    # 创建分类器的对象
    rfc = RandomForestClassifier(random_state=100)
    # Performing training
    rfc.fit(X_train, y_train)

    return rfc


def train_using_knn(X_train, X_test, y_train):
    # 创建分类器的对象
    knn = KNeighborsClassifier(n_neighbors=1)
    # Performing training
    knn.fit(X_train, y_train)

    return knn


# Predictions进行预测
def prediction(X_test, clf_object):
    # Predicton on test with giniIndex
    y_pred = clf_object.predict(X_test)
    return y_pred


# Accuracy，计算准确率
def cal_accuracy(y_test, y_pred):
    print("Confusion Matrix: \n",
          confusion_matrix(y_test, y_pred))

    print("Accuracy : ",
          accuracy_score(y_test, y_pred) * 100)

    print("Report : \n",
          classification_report(y_test, y_pred))


# Main code
# 编写主函数，cal_accuracy()计算准确率，使用y_pred_rfc进行预测
def main():
    # Building Phase
    data = import_data()                       # 导入数据
    X, Y, X_train, X_test, y_train, y_test = split_dataset(data)#将数据进行分割

    # Operational Phase
    print("\nResults Using Gini Index:")
    clf_gini = train_using_gini(X_train, X_test, y_train)# 使用Gini Index进行训练
    # Prediction using gini
    y_pred_gini = prediction(X_test, clf_gini)
    cal_accuracy(y_test, y_pred_gini)

    # Operational Phase
    print("Results Using RandomForestClassifier:")
    rfc = train_using_rfc(X_train, X_test, y_train)# 使用RandomForestClassifier进行训练
    # Prediction using rfc
    y_pred_rfc = prediction(X_test, rfc)
    cal_accuracy(y_test, y_pred_rfc)

   # Operational Phase
    print("Results Using KNeighborsClassifier:")
    knn = train_using_knn(X_train, X_test, y_train)# 使用KNeighborsClassifier进行训练
    # Prediction using knn
    y_pred_knn = prediction(X_test, knn)
    cal_accuracy(y_test, y_pred_knn)


# Calling main function
if __name__ == "__main__":
    main()
