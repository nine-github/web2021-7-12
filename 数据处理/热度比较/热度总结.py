import pandas, xlrd
# 热度总结
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