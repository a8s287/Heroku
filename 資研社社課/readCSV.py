# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 18:56:53 2020

@author: Eva
"""

import csv
with open('C:/Users/Eva/Desktop/Python/output.csv', newline='') as csvfile:  # 開啟 CSV 檔案
  rows = csv.reader(csvfile)                               # 讀取 CSV 檔案內容
  for row in rows:                                               # 以迴圈輸出每一列
    print(row)
