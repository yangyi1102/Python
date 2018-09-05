# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 15:48:44 2017

@author: 17549
"""
import scipy.misc
import matplotlib.pyplot as plt
import numpy as np
lena=scipy.misc.face()
def get_indices(size):
    arr=np.arange(size)
    return arr%4==0
lenal=lena.copy()
xindices=get_indices(lena.shape[0])
yindices=get_indices(lena.shape[1])
lenal[xindices,yindices]=0
plt.subplot(221)
plt.imshow(lenal)
lena2=lena.copy()
lena2[(lena>lena.max()/4)&(lena<3*lena.max()/4)]=0
plt.subplot(212)
plt.imshow(lena2)
plt.show()