import pandas, os
# 数据总结
writer = pandas.ExcelWriter('../爬虫数据整理/弹幕.xlsx')
for i in os.listdir('../爬虫数据3.0'):
    path = os.path.join('../爬虫数据3.0/', i)
    if os.path.isdir(path):
        data = {}
        lis = []
        for j in os.listdir(path):
            with open(os.path.join(path, j), 'r', encoding='utf8') as f:
                data[j[3:j.find('.')]] = pandas.Series(f.readlines())
                lis.append(j[3:j.find('.')])
        temp = lis.pop(1)
        lis.append(temp)
        print(lis)
        data = pandas.DataFrame(data)
        data = data.reindex(lis, axis=1)
        data.to_excel('../爬虫数据整理/'+i[:3]+'弹幕.xlsx')
writer.save()