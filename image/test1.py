# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 01:33:48 2020

@author: Eva
"""

from PIL import Image
import pytesseract
  
img = Image.open('test1.jpg')
text = pytesseract.image_to_string(img, lang='eng')
print(text)