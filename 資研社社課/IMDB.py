# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:16:54 2020

@author: Eva
"""

import requests as re
from bs4 import BeautifulSoup

url = "https://www.imdb.com/find"
url2 = "https://www.imdb.com"

a = input("請搜尋電影名稱")
payload = {"q" : str(a) }
r = re.get( url , params = payload)

sp = BeautifulSoup( r.text , "html.parser" )
str1 = sp.find( "td" , class_ = "result_text")
if str1 != None:
    #print(str(str1)+"\n")
    
    sp2 = BeautifulSoup( str(str1) , "html.parser" )
    str2 = sp2.select( 'a' )[0].get('href')
    
    #print(str2)
    
    
    r2 = re.request( "GET" , url2 + str(str2) )
    
    sp3 = BeautifulSoup( r2.text , "html.parser" )
    str3 = sp3.find( "div" , class_ = "title_wrapper")
    #print(str(str1)+"\n")
    
    sp4 = BeautifulSoup( str(str3) , "html.parser" )
    str4 = sp4.select( 'h1' )[0]
    str4_1 = sp4.select( 'a' )[0]
    
    #str4 = str(str4).strip(str(str4_1))
    
    str4_2 = str4.text.replace("("+str4_1.text+")","")
    #print(str4.text)
    print("標題:\t"+str4_2)
    
    
    str5 = sp3.find("span" , itemprop = "ratingValue")
    print("評分:\t"+str5.text)
    
    str6 = sp3.find("div" , class_ = "subtext")
    str6_1 = str6.find_all("a")
    
    print("電影類型:\t")
    for i in range(len(str6_1)-1):
        print("\t"+str6_1[i].text)
        
    str7 = sp3.find("table" ,class_ = "cast_list").find_all("tr",class_="odd")
    str7_ = sp3.find("table" ,class_ = "cast_list").find_all("tr",class_="even")
    #print(str7)
    
    str7_1 = []
    for i in str7:
        str7_1.append(i.select("img")[0].get("alt"))
    
    for i in str7_:
        str7_1.append(i.select("img")[0].get("alt"))
    
    print("演員:\t")
    for i in str7_1:
        print("\t"+i)
else:
    print("找不到該電影")