# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 01:38:21 2020

@author: Eva
"""

from PIL import Image
import pytesseract

ImageText = pytesseract.image_to_string( Image.open( "test1.jpg" ),lang = "chi_tra" )
print( ImageText )