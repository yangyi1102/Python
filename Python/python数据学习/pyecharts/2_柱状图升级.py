# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 11:28:11 2017

@author: 17549
"""

from pyecharts import Bar
attr=["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
v1=[5,20,36,10,10,90]
v2=[10,25,8,60,20,80]
bar=Bar("柱状图实例2")
bar.add("商家A",attr,v1,is_stack=True)
bar.add("商家B",attr,v2,is_stack=True)
bar.show_config()
bar.render(r"E:\2_柱状图升级.html")