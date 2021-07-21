import pandas, os, re, xlrd, numpy
import matplotlib.pyplot as plt
# 热度总结表
path = '..\B站排行榜\B站排行榜数据.xlsx'
excels = xlrd.open_workbook(path)
sheetNames = excels.sheet_names()
b = pandas.read_excel(path, sheetNames[0])
for j in b:
    lis = {}
    for i in sheetNames:
        a = pandas.read_excel(path, i)
        lis[i] = a[j]
    pandas.DataFrame(lis).to_excel('../数据处理/' + j + '总结.xlsx')

#一键三连图
path = '../数据整理/B站排行榜/B站排行榜数据.xlsx'
excel = xlrd.open_workbook(path)
lis = excel.sheet_names()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
for i in lis:
    data = pandas.read_excel(path, i)
    data = data[['点赞数量', '投币数量', '收藏数量']]
    plt.bar(list(data), data.mean())
    for j in data:
        plt.text(j, data[j].mean(), round(data[j].mean()))
    plt.title(i + '热度统计')
    plt.savefig('../数据处理/热度比较/' + i + '.png')
    plt.show()