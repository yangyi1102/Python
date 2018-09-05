# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 18:07:30 2017

@author: 17549
"""

from pyecharts import Funnel
attr=["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
value=[20,40,60,80,100,120]
funnel=Funnel("动态漏图",width=600,height=400,title_pos='center')
funnel.add("商品",attr,value,is_label_show=True,label_pos="outside",
           legend_orient='vertical',legend_pos='left')
funnel.show_config()
funnel.render(r"E:\12_动态漏图升级.html")