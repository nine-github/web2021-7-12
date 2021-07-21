import requests
import os
import re
import json
import pymongo
import time
import random


class BCommentParse(object):
    def __init__(self,base_url):
        self.headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        self.base_url=base_url

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
        r=requests.get(api,headers=self.headers)
        _json=json.loads(r.text)
        self.video_title=_json['data']['title']
        avid=_json['data']['aid']
        return avid

    def set_page(self):
        """
        配置数据库
        :return:
        """
        host = '127.0.0.1'
        port = 27017
        myclient = pymongo.MongoClient(host=host, port=port)
        mydb = 'Bilibili'
        sheetname = self.video_title
        db = myclient[mydb]
        self.post = db[sheetname]

    def parse_comment(self):
        self.my_init()
        base_url=f'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&type=1&oid={self.oid}&sort=2'
        n=0
        url=base_url+'&pn={}'
        headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        try:
            while True:
                r=requests.get(url.format(n),headers=headers)
                _json=json.loads(r.text)
                replies=_json.get('data').get('replies')
                item={}
                n+=1
                if len(replies)!=0:
                    print(f'\033[34;47m--------------------正在爬取{n}页--------------------')
                    for replie in replies:
                        item['user_id']=replie.get('member').get('mid')#用户id
                        item['user_name']=replie.get('member').get('uname')#用户名
                        item['user_sex']=replie.get('member').get('sex')#性别
                        item['user_level']=replie.get('member').get('level_info').get('current_level')#等级
                        vip=replie.get('member').get('vip').get('vipStatus')#是否vip
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
    video_url=input("请输入网址:")
    if video_url.startswith('https://www.bilibili.com/video/'):
        b=BCommentParse(video_url)
        b.parse_comment()
    else:
        print('请输入正确地址！')



