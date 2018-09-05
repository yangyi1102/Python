# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:47:04 2017

@author: 17549
"""

from pyecharts import Line3D
import math
_data=[]
for t in range(0,25000):
    _t=t/1000
    x=(1+0.25*math.cos(75*_t))*math.cos(_t)
    y=(1+0.25*math.cos(75*_t))*math.sin(_t)
    z=_t+2.0*math.sin(75*_t)
    _data.append([x,y,z])
range_color=['#313695','#4575b4','#74add1','#abd9e9','#e0f3f8','#ffffbf',
              '#fee090','#fdae61','#f46d43','#d73027','#a50026']
line3d=Line3D("3D折线图",width=1200,height=600)
line3d.add("",_data,is_visualmap=True,visual_range_color=range_color,
           visual_range=[0,30],grid3D_rotate_sensitivity=5)
line3d.show_config()
line3d.render(r"E:\6_3D折线图.html")