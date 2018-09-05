# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 21:36:03 2017

@author: 17549
"""

import matplotlib.pyplot as plt
import  matplotlib
matplotlib.rcParams['font.style']='italic'
matplotlib.rcParams['font.family']='Youyuan'
plt.plot([1.5,2.5,3.5,4.5,])
plt.ylabel("纵轴（值）")
plt.savefig('test',dpi=600)
plt.show()
#绘制余弦波
import matplotlib.pyplot as plt
import numpy as np
import  matplotlib
matplotlib.rcParams['font.size']='50'
matplotlib.rcParams['font.family']='STSong'
a=np.arange(0.0,5.0,0.02,)#生成数组a
plt.ylabel("纵轴:振幅")
plt.xlabel("纵轴：时间")
plt.plot(a,np.cos(2*np.pi*a),'p',)
plt.savefig('test',dpi=100)
plt.show()
#第二种方法显示中文，建议用第二种方法（在需要中文时候显示）
import numpy as np
import matplotlib.pyplot as plt
a=np.arange(0.0,5.0,0.02,)#生成数组a
plt.ylabel("纵轴:振幅",fontproperties='SimHei',fontsize=20)
plt.xlabel("纵轴：时间",fontproperties='YouYuan',fontsize=20)
plt.plot(a,np.cos(2*np.pi*a),'3')
plt.show()