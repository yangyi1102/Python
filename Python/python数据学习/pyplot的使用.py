# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 19:47:28 2017

@author: 17549
"""

import matplotlib.pyplot as plt
import  numpy as np
a=np.arange(10)
plt.plot(a,a*1.5,a,a*2.5,a,a*3.5,a,a*4.5,)
plt.show()
import matplotlib.pyplot as plt
import  numpy as np
a=np.arange(10)
plt.plot(a,a*1.5,'go-',a,a*2.5,'rx',a,a*3.5,'*',a,a*4.5,'b-.')
plt.show()
