# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 12:46:49 2017

@author: 17549
"""
from pyecharts import EffectScatter
v1=[10,20,30,40,50,60]
v2=[25,20,15,10,60,33]
es=EffectScatter("动态散点图")
es.add("effectScatter",v1,v2)
es.show_config()
es.render(r"E:\5_动态散点图.html")