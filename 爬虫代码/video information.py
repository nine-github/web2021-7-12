import urllib3
import requests
import json
import csv
import time
import random

bv = input('请输入要爬取视频的BV号:')
area = input("请输入你爬取的视频的分区:")
file = open('B站' + area + '排行榜数据.csv', mode='a', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(file, fieldnames=["观看数量", "弹幕数量", "评论数量", "收藏数量", "投币数量", "分享数量", "点赞数量"])
csv_writer.writeheader()
#用户输入所要爬取的视频信息
url = 'http://api.bilibili.com/x/web-interface/view?bvid=' + bv
# 请求头，模拟浏览器的运行
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}
#在urllib3时代，官方强制验证https的安全证书，如果没有通过是不能通过请求的，虽然添加忽略验证的参数，但是依然会给出醒目的warning
# 从urllib3中消除警告
urllib3.disable_warnings()
try:
    # 延时操作,防止爬的太快
    time.sleep(1 + random(0, 1))
    response = requests.get(url, headers=headers)
except Exception as e:
    print(e)
else:
    content = json.loads(response.text)
    # 获取到的是str字符串 需要解析成json数据
    # print(response.content.decode('utf-8'))
    statue_code = content.get('code')
    # print(statue_code)
    dit = {}
    if statue_code == 0:
        # 根据B站网页源代码解析，爬取相关数据
        view = content['data']['stat']['view']
        danmaku = content['data']['stat']['danmaku']
        reply = content['data']['stat']['reply']
        favorite = content['data']['stat']['favorite']
        coin = content['data']['stat']['coin']
        share = content['data']['stat']['share']
        like = content['data']['stat']['like']
        dit = {
            '观看数量': view,
            '弹幕数量': danmaku,
            '评论数量': reply,
            '收藏数量': favorite,
            '投币数量': coin,
            '分享数量': share,
            '点赞数量':like
        }
        csv_writer.writerow(dit)
        print(dit)
        file.close()




