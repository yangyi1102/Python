# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:45:27 2017

@author: 17549
"""

from pyecharts import EffectScatter
v1=[10,20,30,40,50,60]
v2=[25,20,15,10,60,33]
es=EffectScatter("动态散点图升级")
es.add("",[10],[10],symbol_size=20,effect_scale=3.5,effect_period=3,symbol="pin")
es.add("",[20],[20],symbol_size=12,effect_scale=4.5,effect_period=4,symbol="rect")
es.add("",[30],[30],symbol_size=30,effect_scale=5.5,effect_period=5,symbol="roundRect")
es.add("",[40],[40],symbol_size=10,effect_scale=6.5,effect_brushtype='fill',symbol="diamond")
es.add("",[50],[50],symbol_size=16,effect_scale=5.5,effect_period=3,symbol="arrow")
es.add("",[60],[60],symbol_size=6,effect_scale=2.5,effect_period=3,symbol="triangle")
es.show_config()
es.render(r"E:\9_动态散点图(升级).html")