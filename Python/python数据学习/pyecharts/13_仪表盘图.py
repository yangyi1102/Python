# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 18:13:19 2017

@author: 17549
"""

from pyecharts import Gauge
gauge=Gauge("仪表盘图")
gauge.add("业务指标","完成率",66.66)
gauge.show_config()
gauge.render(r"E:\13_仪表盘图.html")