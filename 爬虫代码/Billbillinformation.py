"""
Parsel库:parsel的模块主要用来将请求后的字符串格式解析成css进行内容的匹配，为了使用后面的css选择器
Request库:请求头的使用
Use-agent:请求头来伪装成浏览器，以便更好地抓取数据。
Re库:使用正则表达式进行评论爬取
Json库:将数据解析成json数据进行后面的分析
Pymongo:进行py3下MongoDB的存储操作
Time:延迟操作
urllib3库:消除警告
"""

import re
import pymongo
import time
import urllib3
import json
import requests
import parsel
import csv
import random

class Barea_rank():
    #用户输入信息
    area = input("请输入要爬取前十视频的分区:")
    url = input("请输入要爬取前十视频的网页:")
    # 请求头，模拟浏览器的运行
    if url.startswith("https://www.bilibili.com/v/popular/rank/"):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }
        file = open('B站' + area + '排名数据.csv', mode='w', encoding='utf-8-sig', newline='')
        csv_writer = csv.DictWriter(file, fieldnames=['标题', '播放量', '弹幕量', '作者', '综合得分', '视频地址', '硬币'])
        csv_writer.writeheader()
        # 在urllib3时代，官方强制验证https的安全证书，如果没有通过是不能通过请求的，虽然添加忽略验证的参数，但是依然会给出醒目的warning
        # 从urllib3中消除警告
        urllib3.disable_warnings()
        try:
            # 延时操作,防止爬的太快
            time.sleep(1 + random(0, 1))
            response = requests.get(url = url, headers = headers)
        except Exception as e:
            print(e)
        else:
            # parsel的模块主要用来将请求后的字符串格式解析成css进行内容的匹配
            selector = parsel.Selector(response.text)
            # 使用css selector(选择子)格式，获取接下来的数据
            lis = selector.css('.rank-list li')
            dit = {}
            for li in lis:
                # 根据网页解析出来的对应格是，用css获取相关信息
                title = li.css('.info a::text').get()  # 标题
                bf_info = li.css('div.content > div.info > div.detail > span:nth-child(1)::text').get().strip()  # 播放量
                dm_info = li.css('div.content > div.info > div.detail > span:nth-child(2)::text').get().strip()  # 弹幕量
                bq_info = li.css('div.content > div.info > div.detail > a > span::text').get().strip()  # 作者
                score = li.css('.pts div::text').get()  # 综合得分
                page_url = li.css('.img a::attr(href)').get()  # 视频地址
                # 使用元组保存
                dit = {
                    '标题': title,
                    '播放量': bf_info,
                    '弹幕量': dm_info,
                    '作者': bq_info,
                    '综合得分': score,
                    '视频地址': page_url,
                }
                # 写入文件
                csv_writer.writerow(dit)
                print(dit)
    else:
        print("请输入正确的网址!")

class BVideo_information():
    bv = input('请输入要爬取视频点赞投币等数据的BV号:')
    area = input("请输入你爬取的视频点赞投币等数据的分区:")
    file = open('B站' + area + '排行榜数据.csv', mode='a', encoding='utf-8-sig', newline='')
    csv_writer = csv.DictWriter(file, fieldnames=["观看数量", "弹幕数量", "评论数量", "收藏数量", "投币数量", "分享数量", "点赞数量"])
    csv_writer.writeheader()
    # 用户输入所要爬取的视频信息
    url = 'http://api.bilibili.com/x/web-interface/view?bvid=' + bv
    # 请求头，模拟浏览器的运行
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    }
    # 在urllib3时代，官方强制验证https的安全证书，如果没有通过是不能通过请求的，虽然添加忽略验证的参数，但是依然会给出醒目的warning
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
                '点赞数量': like
            }
            csv_writer.writerow(dit)
            print(dit)
            file.close()

class Bdanmaku():
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
            #一条条弹幕写入
            file.write(one_danmaku)
            #换行操作
            file.write('\n')

class Buser_information(object):
    def __init__(self,base_url):
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        self.base_url = base_url

    def my_init(self):
        id = self.base_url.split('video/')[-1].split('?')[0]
        if id.startswith('av'):
            id = id.split('av')[-1]
            self.oid = self.get_avid_title(id)
        else:
            self.oid = self.get_avid_title(id, av=False)
        self.set_page()

    def get_avid_title(self,id_number,av=True):
        """
        获取av号以及视频标题
        :param id_number: av/bv号
        :param av: 是否为av号
        :return: av号
        """
        if av==True:
            api=f'https://api.bilibili.com/x/web-interface/view?aid={id_number}'
        else:
            api=f'https://api.bilibili.com/x/web-interface/view?bvid={id_number}'
        r = requests.get(api,headers = self.headers)
        #解析成json数据
        _json = json.loads(r.text)
        self.video_title=_json['data']['title']
        avid=_json['data']['aid']
        return avid

#数据库配置，这里使用mongodb
    def set_page(self):
        host = '127.0.0.1'
        port = 27017
        myclient = pymongo.MongoClient(host=host, port=port)
        mydb = 'Bilibili'
        sheetname = self.video_title
        db = myclient[mydb]
        self.post = db[sheetname]

    def parse_comment(self):
        self.my_init()
        base_url = f'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&type=1&oid={self.oid}&sort=2'
        n = 0
        url=  base_url+'&pn={}'
        headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        try:
            while True:
                r=requests.get(url.format(n),headers=headers)
                _json=json.loads(r.text)
                replies=_json.get('data').get('replies')
                item={}
                n+=1
                if len(replies)!=0:
                    #爬取过程，可以看见具体爬到哪里了
                    print(f'\033[34;47m--------------------正在爬取{n}页--------------------')
                    for replie in replies:
                        item['user_id']=replie.get('member').get('mid')#用户id
                        item['user_name']=replie.get('member').get('uname')#用户名
                        item['user_sex']=replie.get('member').get('sex')#性别
                        item['user_level']=replie.get('member').get('level_info').get('current_level')#等级
                        vip=replie.get('member').get('vip').get('vipStatus')#是否vip
                        #判断是否为VIP
                        if vip==1:
                            item['user_is_vip']='Y'
                        elif vip==0 :
                            item['user_is_vip']='N'
                        comment_date=replie.get('member').get('ctime')#评论日期
                        timeArray = time.localtime(comment_date)
                        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                        item['apprecate_count']=replie.get('like')#点赞数
                        item['reply_count']=replie.get('rcount')#回复数
                        item['comment_date']=otherStyleTime
                        item['comment']=replie.get('content').get('message')#评论内容
                        #判断数据库中有无此文档，也可用于断点续
                        res=self.post.count_documents(item)
                        if res==0:
                            data = dict(item)
                            self.post.insert(data)
                            print(f'\033[35;46m{item}\033[0m')
                        else:
                            print('\033[31;44m pass\033[0m')
                    time.sleep(1 + random(0, 1))
                else:
                    print(f'\033[31;44m--------------------程序在第{n}页正常退出！--------------------\033[0m')
                    break
        except:
            pass


if __name__ == '__main__':
    #爬取top10视频信息的内容
    Barea_rank()
    #爬取单个视频的数据统计的内容
    BVideo_information()
    #爬取单个视频的弹幕的内容
    Bdanmaku()
    #爬取用户信息以及评论的内容
    video_url=input("请输入所要爬取评论和用户信息的视频网址:")
    if video_url.startswith('https://www.bilibili.com/video/'):
        b=Buser_information(video_url)
        b.parse_comment()
    else:
        print('请输入正确地址！')
