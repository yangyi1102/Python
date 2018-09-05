# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 14:51:55 2017

@author: 17549
"""

import matplotlib.pyplot as plt
import numpy as np 
plt.plot([1,2,3,4])
plt.show()
plt.axis([0,5,0,20])
plt.title('first plot')
plt.plot([1,2,3,4],[1,4,9,16],'or')
plt.show()
import math
t=np.arange(0,2.5,0.1)
y1=map(math.sin,math.pi*t)
y2=map(math.sin,math.pi*t+math.pi/2)
y3=map(math.sin,math.pi*t-math.pi/2)
plt.plot(t,y1,'b*',t,y2,'g^',t,y3,'ys')
plt.show()
