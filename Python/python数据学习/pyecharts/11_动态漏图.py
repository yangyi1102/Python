# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 17:53:52 2017

@author: 17549
"""

from pyecharts import Funnel
attr=["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
value=[20,40,60,80,100,120]
funnel=Funnel("动态漏图")
funnel.add("商品",attr,value,is_label_show=True,label_pos="inside",label_text_color="fff")
funnel.show_config()
funnel.render(r"E:\11_动态漏图.html")
