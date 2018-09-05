# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 11:08:52 2017

@author: 17549
"""

from pyecharts import Pie
attr=["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
v1=[11,12,13,10,10,10]
v2=[19,21,32,20,20,33]
pie=Pie("玫瑰图实例",title_pos="center",width=900,title_text_size=60)
pie.add("goodsA",attr,v1,center=[25,50],is_random=True,radius=[30,75],rosetype="radius")
pie.add("goodsB",attr,v2,center=[75,50],is_random=True,radius=[30,75],rosetype="area",is_lengend_show=False,
       is_label_show=True)
pie.show_config()
pie.render(r"E:\3_动态饼图.html")