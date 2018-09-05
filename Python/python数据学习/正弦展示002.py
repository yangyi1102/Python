# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 12:20:01 2017

@author: 17549
"""

#import math
#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib
#t=np.arange(0,2.5,0.1)
#plt.plot()
#plt.plot(math.sin,math.pi*t+math.pi/2)
#plt.plot(math.sin,math.pi*t-math.pi/2)
#plt.plot(t,y1,'b*',t,y2,'g^',t,y3,'ys')
#plt.show()
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