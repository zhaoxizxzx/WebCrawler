# -*- coding: utf-8 -*-
import urllib.request
import  urllib.parse
import json
from bs4 import BeautifulSoup
import re
import ContactRatio,datetime
import sqlite3

# 建立表格
conn = sqlite3.connect("test.db")
c = conn.cursor()
sql = '''
    create table Leon
        (num int not null,
        id int not null)
'''
c.execute(sql)
conn.commit()
conn.close()
print("successful")

# # 添加数据
# conn = sqlite3.connect("test.db")
# par = (af2, follower)
# c = conn.cursor()
# sql = '''
#                    insert into followers (time,num)
#                    values(?,?);
#
#
#                '''
# c.execute(sql, par)
# conn.commit()
# conn.close()









