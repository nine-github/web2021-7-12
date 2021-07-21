import pandas, os, re, xlrd, numpy
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn import *
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.metrics import accuracy_score


#数据读入
path = '../数据整理/B站用户信息/用户信息.xlsx'
excel = xlrd.open_workbook(path)
lis = excel.sheet_names()
datas = []
for i in lis:
    data = pandas.read_excel(path, i)[['user_sex', 'user_level', 'user_is_vip']]
    datas.append(data)
data = pandas.concat(datas)

#保留原始数据
data_ini = data

#数据预处理
data = data[data['user_sex'] != '保密']
data.loc[data['user_sex'] == '男', 'user_sex'] = 1
data.loc[data['user_sex'] == '女', 'user_sex'] = 0
data.loc[data['user_is_vip'] == 'N', 'user_is_vip'] = 0
data.loc[data['user_is_vip'] == 'Y', 'user_is_vip'] = 1

#训练、测试集划分
data_train = data[['user_sex', 'user_level']].values.astype(float)
data_target = data['user_is_vip'].values.astype(float).reshape(-1, 1)
x_train, x_test, y_train, y_test = train_test_split(data_train,data_target,test_size=0.2)

#决策树模型及评价
model = DecisionTreeClassifier()
model.fit(x_train, y_train)
model.score(x_test, y_test)


#逻辑回归模型
logreg = LogisticRegression()
logreg.fit(x_train, y_train)
y_test_pred = logreg.predict(x_test)
#分别计算两组测试集和训练集的均方误差、平均绝对误差和决定系数
mse = metrics.mean_squared_error(y_test, y_test_pred)
mae = metrics.mean_absolute_error(y_test, y_test_pred)
print('房价预测模型的MSE、MAE与准确度为：')
print(mse, mae, accuracy_score(y_test_pred, y_test))


#神经网络模型及评价
mlp = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 5))
mlp.fit(x_train, y_train)
y_test_pre = mlp.predict(x_test)
print('准确率：', mlp.score(x_test, y_test))
print("预测报告：")
print(metrics.classification_report(y_test, y_test_pre))
print('混淆矩阵:')
print(metrics.confusion_matrix(y_test, y_test_pre))