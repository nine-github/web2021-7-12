import pandas, os, re, xlrd, numpy
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
with open('../爬虫数据3.0/B站用户分布.txt', 'r', encoding='utf8') as f:
    dir = {}
    for i in f.readlines():
        j = i.replace('\n', '')
        if j:
            lis = j.split(':')
            dir[lis[0]] = int(lis[1])
data = pandas.Series(dir)
data.sort_values(inplace=True)


plt.bar(data.index, data.values)
for i in data.index:
    print(i + ':' + str(data[i]))
plt.show()