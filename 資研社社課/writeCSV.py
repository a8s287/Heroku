# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 18:51:53 2020

@author: Eva
"""

import csv
with open('C:/Users/Eva/Desktop/Python/output.csv', 'w', newline='') as csvfile:    #開啟輸出的csv檔案
  writer = csv.writer(csvfile)                                         #建立csv檔寫入器
  writer.writerow(['姓名', '科目', '成績'])
  writer.writerow(['Sean','資料結構', 80])
  writer.writerow(['Vivian','微積分',90])
