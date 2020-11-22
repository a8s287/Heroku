# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:38:45 2020

@author: Eva
"""

import requests as re

url = "http://www.webscrapingfordatascience.com/basichttp/"
r = re.request('GET',url)

with open('test.txt','w') as outfile:
    outfile.write("狀態碼:")
    outfile.write((str)(r.status_code)+"\n")
    outfile.write("網址"+r.url+"\n")
    outfile.write(r.text)
