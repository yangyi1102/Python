# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 08:46:09 2017

@author: 17549
"""

from pyecharts import Polar
import random
data=[(i,random.randint(1,100)) for i in range(101)]
polar=Polar("极坐标散点图")
polar.add("",data,boundary_gap=False,type='scatter',is_splitline_show=False,
          area_color=None,is_axisline_show=True)
polar.show_config()
polar.render(r"E:\14_极坐标散点图.html")

