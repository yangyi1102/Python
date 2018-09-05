# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:07:47 2017

@author: 17549
"""

from pyecharts import Graph
nodes=[{"name":"结点1","symbolSize":10},
       {"name":"结点2","symbolSize":20},
       {"name":"结点3","symbolSize":30},
       {"name":"结点4","symbolSize":40},
       {"name":"结点5","symbolSize":50},
       {"name":"结点6","symbolSize":40},
       {"name":"结点7","symbolSize":30},
       {"name":"结点8","symbolSize":20}]
links=[]
for i in nodes:
    for j in nodes:
        links.append({"source":i.get('name'),"target":j.get('name')})
graph=Graph("关系图-力应布局")
graph.add("",nodes,links,repulsion=8000)
graph.show_config()
graph.render(r"E:\7_关系图-力应布局.html")