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
plt.bar(data['user_level'].value_counts().index, data['user_level'].value_counts())
plt.title('用户等级分布')
for j in data['user_level'].value_counts().index:
    plt.text(j, data['user_level'].value_counts()[j], data['user_level'].value_counts()[j])
plt.savefig('../数据处理/等级与会员/各区等级分布/总图.png')
plt.show()
#分区图
for i in range(len(datas)):
    plt.bar(datas[i]['user_level'].value_counts().index, datas[i]['user_level'].value_counts())
    plt.title(lis[i] + '用户等级分布')
    for j in datas[i]['user_level'].value_counts().index:
        plt.text(j, datas[i]['user_level'].value_counts()[j], datas[i]['user_level'].value_counts()[j])
    plt.savefig('../数据处理/等级与会员/各区等级分布/' + lis[i] +'.png')
    plt.show()