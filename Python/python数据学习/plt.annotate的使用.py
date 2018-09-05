# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 23:58:45 2017

@author: 17549
"""

import matplotlib.pyplot as plt
import numpy as np
a=np.arange(0.0,5.0,0.02)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.xlabel("横轴:时间",fontproperties='SimHei',fontsize=15,color='green')
plt.ylabel("纵轴:振幅",fontproperties='SimHei',fontsize=15,color='blue')
plt.title(r"正弦波 $y=cos(2\pi x)$",fontproperties='SimHei',fontsize=25)#"$"一标准文本$y=cos(2\pi x)$格式#
plt.annotate(r'$\mu=100$',xy=(2,1),xytext(3,1.5),xytext(3,1.5)=dict(facecolor='black',shrink=0.1,width=2))
#r'$\mu=100$',表示字符串，xy=(2,1)表示箭头指示的位置，xytext(3,1.5)文本的位置，dict箭头的参数，颜色，宽度
plt.axis([-1,6,-2,2])
plt.grid(True)#图形加入网格曲线
plt.show()