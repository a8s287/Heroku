# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 18:58:51 2020

@author: Eva
"""

import openpyxl
#from openpyxl import Workbook
wb = openpyxl.Workbook()   #創建Excel文檔
sheet = wb.active  #使用目前的工作表
# sheet = wb[‘Sheet’]
sheet['A1'] = 'Python'#寫入單一儲存格
row = [1 ,2, 3, 4, 5]
sheet.append(row)  #以行的方式寫入
wb.save('example.xlsx')
