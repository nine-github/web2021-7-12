import json
import re
import requests
import time
import random

area = input("请输入要爬取弹幕的视频的分区:")
bv = input("请输入所要爬取弹幕的视频的BV号:")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}
url = "https://api.bilibili.com/x/player/pagelist?bvid=" + str(bv) + "&jsonp=jsonp"
try:
    # 延时操作,防止爬的太快
    time.sleep(1 + random(0, 1))
    response = requests.get(url=url, headers=headers)
except Exception as e:
    print(e)
else:
    # 转成文本
    res_text = response.text
    # 获取到的是str字符串 需要解析成json数据
    res_dict = json.loads(res_text)
    # 根据网页解析信息，获取cid
    cid = res_dict['data'][0]['cid']
    #接下来根据cid去爬取弹幕数据
    url = "https://api.bilibili.com/x/v1/dm/list.so?oid=" + str(cid)
try:
    # 延时操作,防止爬的太快
    time.sleep(1 + random(0, 1))
    response = requests.get(url=url, headers=headers)
except Exception as e:
        print(e)
else:
    #按照utf-8解码
    res_xml = response.content.decode('utf-8')
    #使用正则表达式去匹配
    pattern = re.compile('<d.*?>(.*?)</d>')
    #使用findall方法去查找所有弹幕
    danmaku_list = pattern.findall(res_xml)
    file = open('B站' + area + '弹幕数据.txt', mode='a', encoding='utf-8-sig', newline='')
    for one_danmaku in danmaku_list:
        # 一条条弹幕写入
        file.write(one_danmaku)
        # 换行操作
        file.write('\n')