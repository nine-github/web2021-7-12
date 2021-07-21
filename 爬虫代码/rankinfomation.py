import time
import requests
import parsel
import csv
#用户输入所需要爬的分区
area = input("请输入要爬取的分区:")
url = input("请输入要爬取的网页:")
# 请求头，模拟浏览器的运行
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
file = open('B站' + area + '排名数据.csv', mode='w', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(file, fieldnames=['标题', '播放量', '弹幕量', '作者', '综合得分', '视频地址', '硬币'])
csv_writer.writeheader()
try:
    # 延时操作,防止爬的太快
    time.sleep(0.5)
    response = requests.get(url = url, headers = headers)
except Exception as e:
    print(e)
else:
    #parsel的模块主要用来将请求后的字符串格式解析成css进行内容的匹配
    selector = parsel.Selector(response.text)
    #使用css selector(选择子)格式，获取接下来的数据
    lis = selector.css('.rank-list li')
    dit = {}
    for li in lis:
        #根据网页解析出来的对应格式，用css获取相关信息
        title = li.css('.info a::text').get()  # 标题
        bf_info = li.css('div.content > div.info > div.detail > span:nth-child(1)::text').get().strip()  # 播放量
        dm_info = li.css('div.content > div.info > div.detail > span:nth-child(2)::text').get().strip()  # 弹幕量
        bq_info = li.css('div.content > div.info > div.detail > a > span::text').get().strip()  # 作者
        score = li.css('.pts div::text').get()  # 综合得分
        page_url = li.css('.img a::attr(href)').get()  # 视频地址
        #使用元组保存
        dit = {
            '标题': title,
            '播放量': bf_info,
            '弹幕量': dm_info,
            '作者': bq_info,
            '综合得分': score,
            '视频地址': page_url,
        }
        #写入文件
        csv_writer.writerow(dit)
        print(dit)
