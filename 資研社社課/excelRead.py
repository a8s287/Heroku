# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 19:08:16 2020

@author: Eva
"""

import openpyxl  
wb = openpyxl.load_workbook('example.xlsx')  #加載Excel文檔
sheet = wb['Sheet']
print('表名 - ' + sheet.title)
cell = sheet['A1'] 
print('取得 A1 單元格 :'+ cell.value)
