# -*- coding: utf-8 -*-
import urllib.request
import  urllib.parse
import json
from bs4 import BeautifulSoup
import re
import requests
import ContactRatio, datetime, pytz
import sqlite3


def index():
    final = []
    num2 = 0
    baseurl = 'https://movie.douban.com/subject/1295644/reviews?start='
    for i in range(255):
        url = baseurl + str(i*20)
        html = askurl(url)
        findname = re.compile(r'href="https://www.douban.com/people/(.*?)/">')
        bs = BeautifulSoup(html, "html.parser")
        t_list = bs.find_all()
        for item in t_list:
            item = str(item)
            num = re.findall(findname, item)
            if num != []:
                if num[0] not in final:
                    final.append(num[0])
                    # 添加数据
                    conn = sqlite3.connect("test.db")
                    num2 += 1
                    par = (num2, num[0])
                    c = conn.cursor()
                    sql = '''
                                       insert into Leon (num,id)
                                       values(?,?);
                
                
                                   '''
                    c.execute(sql, par)
                    conn.commit()
                    conn.close()
        if i % 10 == 0:
            ContactRatio.sleep(20)
    print(final)
    print(len(final))


def askurl(url):
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'

    }
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode("utf-8")
    return html


if __name__ == '__main__':
    index()






