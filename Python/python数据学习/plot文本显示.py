# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 22:15:49 2017

@author: 17549
"""

import matplotlib.pyplot as plt
import numpy as np
a=np.arange(0.0,5.0,0.02)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.xlabel("横轴:时间",fontproperties='SimHei',fontsize=15,color='green')
plt.ylabel("纵轴:振幅",fontproperties='SimHei',fontsize=15,color='blue')
plt.title(r"正弦波 $y=cos(2\pi x)$",fontproperties='SimHei',fontsize=25)#"$"一标准文本$y=cos(2\pi x)$格式#
plt.text(2,1, r'$\mu=100$',fontsise=15)#文本显示在横轴2，纵轴为1上
plt.axis([-1,6,-2,2])
plt.grad(True)#图形加入网格曲线
plt.show()