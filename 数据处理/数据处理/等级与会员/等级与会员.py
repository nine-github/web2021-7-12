import pandas, os, re, xlrd, numpy
import matplotlib.pyplot as plt
path = '../数据整理/B站用户信息/用户信息.xlsx'
excel = xlrd.open_workbook(path)
lis = excel.sheet_names()
datas = []
for i in lis:
    data = pandas.read_excel(path, i)
    datas.append(data[['user_level', 'user_is_vip']])
data = pandas.concat(datas)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
a = data['user_level']

#设置数据
index = a.unique()
index.sort()
b = a[data['user_is_vip'] == 'Y'].value_counts()
c = a[data['user_is_vip'] == 'N'].value_counts()
for i in list(set(index).difference(set(b.index))):
    b[i] = 0
for i in list(set(index).difference(set(c.index))):
    c[i] = 0


#叠加条形图
plt.bar(index, b.sort_index(), label='是会员')
plt.bar(index, c.sort_index(), bottom=b.sort_index(), label='非会员')
plt.title('等级与会员')
plt.legend(loc='upper left')
plt.xlabel('等级')
plt.ylabel('数量')
plt.savefig('../数据处理/等级与会员/等级与会员.png')
plt.show()

#会员等级分布
temp = a[data['user_is_vip'] == 'Y'].value_counts()
temp = temp.sort_index()
temp.index = ['Lv' + str(i) for i in temp.index]
plt.pie(temp, labels=temp.index, autopct='%3.1%%')
plt.title('会员等级分布')
plt.savefig('../数据处理/等级与会员/会员等级分布.png')
plt.show()

#非会员等级分布
temp = a[data['user_is_vip'] == 'N'].value_counts()
temp = temp.sort_index()
temp.index = ['Lv' + str(i) for i in temp.index]
plt.pie(temp, labels=temp.index, autopct='%3.1%%')
plt.title('非会员等级分布')
plt.savefig('../数据处理/等级与会员/非会员等级分布.png')
plt.show()


#会员、非会员与等级联合分布
plt.subplot(1, 2, 1)
temp = a[data['user_is_vip'] == 'Y'].value_counts()
temp = temp.sort_index()
temp.index = ['Lv' + str(i) for i in temp.index]
plt.pie(temp, labels=temp.index, autopct='%3.1%%')
plt.title('会员等级分布')
plt.subplot(1, 2, 2)
temp = a[data['user_is_vip'] == 'N'].value_counts()
temp = temp.sort_index()
temp.index = ['Lv' + str(i) for i in temp.index]
plt.pie(temp, labels=temp.index, autopct='%3.1%%')
plt.title('非会员等级分布')
plt.savefig('../数据处理/等级与会员/会员等级联合分布.png')
plt.show()