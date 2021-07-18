import pandas, os, re, xlrd, numpy
import matplotlib.pyplot as plt
path = '../数据整理/B站用户信息/用户信息.xlsx'
excel = xlrd.open_workbook(path)
lis = excel.sheet_names()
datas = []
for i in lis:
    data = pandas.read_excel(path, i)
    datas.append(data[['user_level']])
data = pandas.concat(datas)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#整体图
plt.bar(data['user_level'].unique(), data['user_level'].value_counts())
plt.title('用户等级分布')
plt.show()
#分区图
for i in range(len(datas)):
    plt.bar(datas[i]['user_level'].unique(), datas[i]['user_level'].value_counts())
    plt.title(lis[i] + '用户等级分布')
    plt.show()