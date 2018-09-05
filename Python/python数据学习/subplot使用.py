# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:26:06 2017

@author: 17549
"""

import numpy as np   
import matplotlib.pyplot as plt
def  f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)
a=np.arange(0.0,5.0,0.02)  #生成数组a
plt.subplot(211)
plt.plot(a,f(a))
plt.subplot(2,1,2)#2行 1列 
plt.plot(a,np.cos(2*np.pi*a),'r--')#曲线为虚线进行cos处理
plt.show
