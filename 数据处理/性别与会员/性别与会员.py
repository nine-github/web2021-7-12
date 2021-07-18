import pandas, os, re, xlrd, numpy
import matplotlib.pyplot as plt
path = '../数据整理/B站用户信息/用户信息.xlsx'
excel = xlrd.open_workbook(path)
lis = excel.sheet_names()
datas = []
for i in lis:
    data = pandas.read_excel(path, i)
    datas.append(data[['user_sex', 'user_is_vip']])
data = pandas.concat(datas)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
a = data.loc[data['user_sex'] != '保密']
#总图
plt.subplot(2, 2, 1)
plt.pie(a['user_sex'].value_counts().sort_index(), labels = ['女', '男'], autopct='%3.1f%%', pctdistance=0.8, shadow=True)
plt.title('男女比例')
plt.subplot(2, 2, 2)
plt.pie(data['user_is_vip'].value_counts().sort_index(), labels = ['否', '是'], autopct='%3.1f%%', pctdistance=0.8, shadow=True)
plt.title('会员比例')
plt.subplot(2, 2, 3)
plt.pie(a.loc[a['user_sex'] == '男', 'user_is_vip'].value_counts().sort_index(), labels = ['否', '是'], autopct='%3.1f%%', pctdistance=0.8, shadow=True)
plt.title('男生中的会员')
plt.subplot(2, 2, 4)
plt.pie(a.loc[a['user_sex'] == '女', 'user_is_vip'].value_counts().sort_index(), labels = ['否', '是'], autopct='%3.1f%%', pctdistance=0.8, shadow=True)
plt.title('女生中的会员')
plt.show()
#分图
plt.subplot(1, 2, 1)
plt.pie(a['user_sex'].value_counts().sort_index(), labels = ['女', '男'], autopct='%3.1f%%', pctdistance=0.8, shadow=True)
plt.title('男女比例')
plt.subplot(1, 2, 2)
plt.pie(data['user_is_vip'].value_counts().sort_index(), labels = ['否', '是'], autopct='%3.1f%%', pctdistance=0.8, shadow=True)
plt.title('会员比例')
plt.show()
plt.subplot(1, 2, 1)
plt.pie(a.loc[a['user_sex'] == '男', 'user_is_vip'].value_counts().sort_index(), labels = ['否', '是'], autopct='%3.1f%%', pctdistance=0.8, shadow=True)
plt.title('男生中的会员')
plt.subplot(1, 2, 2)
plt.pie(a.loc[a['user_sex'] == '女', 'user_is_vip'].value_counts().sort_index(), labels = ['否', '是'], autopct='%3.1f%%', pctdistance=0.8, shadow=True)
plt.title('女生中的会员')
plt.show()
#细分图
plt.pie(a['user_sex'].value_counts().sort_index(), labels = ['女', '男'], autopct='%3.1f%%', pctdistance=0.8, shadow=True)
plt.title('男女比例')
plt.show()
plt.pie(data['user_is_vip'].value_counts().sort_index(), labels = ['否', '是'], autopct='%3.1f%%', pctdistance=0.8, shadow=True)
plt.title('会员比例')
plt.show()
plt.pie(a.loc[a['user_sex'] == '男', 'user_is_vip'].value_counts().sort_index(), labels = ['否', '是'], autopct='%3.1f%%', pctdistance=0.8, shadow=True)
plt.title('男生中的会员')
plt.show()
plt.pie(a.loc[a['user_sex'] == '女', 'user_is_vip'].value_counts().sort_index(), labels = ['否', '是'], autopct='%3.1f%%', pctdistance=0.8, shadow=True)
plt.title('女生中的会员')
plt.show()