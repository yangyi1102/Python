# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 14:03:59 2017

@author: 17549
"""

import matplotlib.pyplot as plt
import numpy as np
import  matplotlib
plt.axis([0,5,0,20])
plt.title("tutle",fontsize=20,fontname='Time New Bejing')
plt.xlabel('x',color='gray')
plt.ylabel('y',color='gray')
plt.text(1,1.5,'first')
plt.text(2,4.5,'second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'fourth')
plt.text(1.1,12,r'$y=x^2$',fontsize=20,color='pink')
plt.grid(True)
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.plot([1,2,3,4],[0.5,2.5,4,12],'b*')
plt.plot([1,2,3,4],[0.8,3.5,8,15],'g^')
plt.legend(['First series','Second series','Third series',],loc=2)
plt.savefig('D:/frst.png')
plt.show()
