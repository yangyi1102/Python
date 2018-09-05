# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 10:07:15 2017

@author: 17549
"""

from pyecharts import Polar
radius=['周一','周二','周三','周四','周五','周六','周日']
polar=Polar("极坐标-堆叠柱状图",width=1200,height=600)
polar.add("A",[1,2,3,4,3,5,1],radius_data=radius,type='barAngle',is_stack=True)
polar.add("B",[2,4,6,1,2,3,1],radius_data=radius,type='barAngle',is_stack=True)
polar.add("C",[1,2,3,4,1,2,5],radius_data=radius,type='barAngle',is_stack=True)
polar.show_config()
polar.render(r"E:\16_极坐标-堆叠柱状图.html")