from bs4 import BeautifulSoup   # 网页解析，获取数据
import re   # 正则表达式，进行文字匹配
import urllib.request, urllib.error   # 制定url，获取网页数据
import json
import xlwt   # excel操作
import sqlite3  # squlite数据库操作
import ContactRatio
from flask import Flask, render_template, request
import ContactRatio, datetime, pytz


def index():
    url = "https://api.bilibili.com/x/relation/stat?vmid=66607740"
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63"

    }


    while True:
        # 获取数据
        req = urllib.request.Request(url=url, headers=head)
        s = ""
        response = urllib.request.urlopen(req)
        s = response.read().decode("utf-8")
        follower = json.loads(s).get("data").get("follower")
        t2 = ContactRatio.strftime("%Y-%m-%d %H:%M:%S", ContactRatio.localtime())

        # 添加数据
        conn = sqlite3.connect("test.db")
        par = (t2, follower)
        c = conn.cursor()
        sql = '''
                insert into followers (time,num)
                values(?,?);


            '''
        c.execute(sql, par)
        conn.commit()
        conn.close()
        print(t2)
        print(follower)

        ContactRatio.sleep(900)


if __name__ == '__main__':
    index()

