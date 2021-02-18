from bs4 import BeautifulSoup   # 网页解析，获取数据
import re   # 正则表达式，进行文字匹配
import urllib.request, urllib.error   # 制定url，获取网页数据
import json
import xlwt   # excel操作
import sqlite3  # squlite数据库操作
import ContactRatio


def index():
    flipped = []
    ll = []
    leon = []
    c_rate = {}

    # flipped
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    sql = '''
        select id from flipped
    '''
    cursor = c.execute(sql)
    for row in cursor:
        flipped.append(row)
        counts = c_rate.get(row, 0)
        c_rate[row] = counts + 1

    conn.close()

    # loveletter
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    sql = '''
        select id from LoveLetter
    '''
    cursor = c.execute(sql)
    for row in cursor:
        ll.append(row)
        counts = c_rate.get(row, 0)
        c_rate[row] = counts + 1

    conn.close()

    # leon
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    sql = '''
        select id from Leon
    '''
    cursor = c.execute(sql)
    for row in cursor:
        leon.append(row)
        counts = c_rate.get(row, 0)
        c_rate[row] = counts + 1

    conn.close()

    # 记录重合度
    cnt = 0
    for item in c_rate:
        if c_rate[item] == 3:
            cnt += 1
    print("评价重合人数：%d" %cnt)
    lenf = len(flipped)
    lenll = len(ll)
    lenleon = len(leon)
    print("Flipped评价人数：%d" % lenf)
    print("LoveLetter评价人数：%d" % lenll)
    print("Leon评价人数：%d" % lenleon)
    m = max(lenf, lenll, lenleon)
    # print(cnt/lenf)
    print("评价用户重合率：%f%%" % (cnt/m*100))
    # print(len(flipped)+len(ll)+len(leon)-cnt)

if __name__ == '__main__':
    index()