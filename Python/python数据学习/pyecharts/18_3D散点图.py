# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 09:42:33 2017

@author: 17549
"""


from pyecharts import Scatter3D
import random
data=[[random.randint(0,100),random.randint(0.100),random.randint(0,100)] for _ in
       range(80)]
range_color=['#313695','#4575b4','#74add1','#abd9e9','e0f3f8','fee090','fdae61',
              '#f46d43','#d73027','#a50026']
scatter3D=Scatter3D("3D 散点图",width=1200,height=600)
scatter3D.add("",data,is_visualmap=True,visual_range_color=range_color)
scatter3D.show_config()
scatter3D.render(r"E:\18_3D散点图.html")