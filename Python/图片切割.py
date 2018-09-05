# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 14:37:43 2018

@author: 17549
"""

# -*-coding:utf-8-*-
from PIL import Image
im = Image.open("D:/m.jpg")
img_size = im.size
print("图片宽度和高度分别是{}".format(img_size))
x = 0
y = 0
w = 800
h = 15
region0 = im.crop((x, y, x+w, y+h))
region0.show()
region0.save("D:/crop_test.png")
x = 0
y = 20
w = 800
h = 20
region2 = im.crop((x, y, x+w, y+h))
region2.show()
region2.save("D:/crop_test2.png")
x = 0
y = 45           #45
w = 800
h = 16
region3 = im.crop((x, y, x+w, y+h))
region3.show()
region3.save("D:/crop_test3.png")
 
# 截取图片中一块宽是250和高都是300的
x = 0
y = 70
w = 800
h = 15
region4 = im.crop((x, y, x+w, y+h))
region4.save("D:/crop_test4.png")
region4.show()
x = 0
y = 90
w = 800
h = 15
region5 = im.crop((x, y, x+w, y+h))
region5.show()
region5.save("D:/crop_test5.png")
