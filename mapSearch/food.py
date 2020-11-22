# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 18:30:54 2020

@author: Eva
"""

import requests as re


url = "https://www.google.com.tw/maps/search/%E9%A4%90%E5%BB%B3/@25.0233862,121.5366113,15z/data=!3m1!4b1!4m8!2m7!3m6!1z6aSQ5buz!2zMTA2MDMz5Y-w5YyX5biC5aSn5a6J5Y2A5ZKM5bmz5p2x6Lev5LqM5q61MTM06Jmf5ZyL56uL6Ie65YyX5pWZ6IKy5aSn5a24!3s0x3442a908a8232611:0xeebfb2d71a5025c7!4m2!1d121.5453446!2d25.023387" 

r = re.request("GET", url)
print(r.text)
print("a")