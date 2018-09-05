# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 13:11:30 2017

@author: 17549
"""

import matplotlib.pyplot as plt
import numpy as np
import  matplotlib
plt.plot([1,2,3,2,1,0,1,2,1,4],linewidth=5.0,color='green')
plt.show()
t=np.arange(0,5,0.01)
y1=np.sin(2*np.pi*t)
y2=np.sin(2*np.pi*t)
plt.subplot(211)
plt.plot(t,y1,'b-.',linewidth=1.0)
plt.plot(t,y2,'r--',linewidth=1.0)
plt.show()

