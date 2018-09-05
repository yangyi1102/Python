# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:23:34 2017

@author: 17549
"""

from pyecharts import Graph
import json
with open("..\json\weibo.json","r",encoding="utf-8") as f:
        j=json.load(f)
        nodes,links,categorise,cont,mid,userl=j
graph=Graph("微博转发关系图",width=1200,height=600)
graph.add("",nodes,links,categories,label_pos="right",
          repulsion=50,is_legend_show=False,
                      line_curve=0.2,
                      label_text_color=None)
graph.show_config()
graph.render(r"E:\6_关系图-力应布局.html")