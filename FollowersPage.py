from bs4 import BeautifulSoup   # 网页解析，获取数据
import re   # 正则表达式，进行文字匹配
import urllib.request, urllib.error   # 制定url，获取网页数据
import json
import xlwt   # excel操作
import sqlite3  # squlite数据库操作
import ContactRatio
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    t1 = []
    f1 = []
    # 装所有数据
    t = []
    f = []
    # 仅显示数据

    # 查询数据
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    sql = '''
                    select time,num from followers       
                       '''
    cursor = c.execute(sql)
    for row in cursor:
        t1.append(row[0])
        f1.append(row[1])
    conn.close()
    length = len(t1)
    for i in range(length-10,length):
        t.append(t1[i])
        f.append(f1[i])
    # print(t)
    # print(f)
    # print(t1)
    # print(f1)
    t1.clear()
    f1.clear()
    # print(t1)
    # print(f1)
    return render_template("Followers.html", time = t, foll = f)


if __name__ == '__main__':
    app.run()