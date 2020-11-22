# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 17:11:55 2020

@author: Eva
"""

import csv 
import pymysql

conn = pymysql.connect('localhost',user="a069eva",passwd="2rgirdal",charset="utf8",db="csv_db 6")

sql = """
    CREATE TABLE IF NOT EXISTS NTUEfood(
        ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        店名 varchar(20),
        地址 varchar(30),
        電話 varchar(20),
        營業時間 varchar(100),
        Google評分 float(5)
        );
"""
with conn.cursor() as cursor:
    cursor.execute(sql)
    with open('NTUEfood.csv',newline="") as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                if not row[0] == "店名":
                    sql = """
                    insert into NTUEfood(店名,地址,電話,營業時間,Google評分) values
                    ("""
                    
                    for i in range(len(row)):
                        if i == 0 or i== 1 or i == 2 or i == 3: 
                            sql+=('\"' + row[i] +'\",')
                        elif i == 4:
                            sql += (row[i])
                    sql +=")"
                cursor.execute(sql)
    conn.commit()
conn.close()