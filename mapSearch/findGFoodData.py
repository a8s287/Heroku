# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 21:48:45 2020

@author: Eva
"""

import requests as re
import json
import csv
from bs4 import BeautifulSoup

with open("NTUEfood.csv","a",newline="") as csvfile:
    writer = csv.writer(csvfile)
    #writer.writerow(['店名','地址','電話','營業時間','Google評價'])
    
    while(1) :
        inputs = input("要尋找的店名")
        if inputs == "0":
            break
        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?key=AIzaSyA5lQ8EKJpwDhnXIIrs4497_AU8szINizY&input="+inputs+"&inputtype=textquery&fields=formatted_address,name,rating,place_id"
        r = re.request( "GET" , url )
        
        jr = json.loads(r.text)
        #print(jr)
        for i in jr["candidates"]:
            if "大安區" in i["formatted_address"]:
                name = i["name"]
                formatted_address = i["formatted_address"]
                place_id = i["place_id"]
                rating = i["rating"]
            
                d_url = "https://maps.googleapis.com/maps/api/place/details/json?key=AIzaSyA5lQ8EKJpwDhnXIIrs4497_AU8szINizY&input="+inputs+"&inputtype=textquery&fields=formatted_phone_number,opening_hours,url&place_id="+place_id
                dr = re.request("GET", d_url)
                djr = json.loads(dr.text)
                if 'formatted_phone_number' in  djr['result']:
                    formatted_phone_number = djr['result']['formatted_phone_number']
                else:
                    formatted_phone_number = ""
                weekday_text = []
                if 'opening_hours' in  djr['result']:
                    for i in djr['result']['opening_hours']['weekday_text']:
                        weekday_text.append(i)
                else:
                    weekday_text = ""
                m_url = djr['result']['url']
                
                
                """print("店名:\t"+name)
                print("地址:\t"+formatted_address)
                print("電話:\t"+formatted_phone_number)
                print("營業時間:\t")
                for i in weekday_text:
                    print(i)
                print("Google評價:\t" + str(rating) )
                print("url\t"+m_url)
                """
                writer.writerow([name,formatted_address,formatted_phone_number,weekday_text,str(rating)])
            
                #mr = re.request("GET", m_url)
                #print(mr.text)
                #sp = BeautifulSoup( mr.text , "html.parser" )
                
                #str = sp.find("script")
                #print(str)
                