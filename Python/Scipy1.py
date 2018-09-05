'''
Created on 2018年8月6日

@author: 杨毅
'''
#coding=utf-8
from math import sin,cos
from scipy import optimize
import numpy as np
class Scipy1(object):
    def f1(self,x):
        x0,x1,x2=x.tolist()        #非线性方程求解
        return[
            5*x1+3,
            4*x0*x0-2*sin(x1*x2),
            x1*x2-1.5
            ]
    def result(self):
        result=optimize.fsolve(self.f1, [1,1,1])
        print(result)
        print(self.f1(result))
                   
class least_square_fitting(object):
    def init(self):
        self.X=np.array([8.19,2.72,6.39,8.71,4.7,2.22,3.78])
        self.Y=np.array([7.01,2.87,6.47,6.71,4.1,4.23,4.05])
    def residuals(self,p):
        k,b=p
        return self.Y-(k*self.X+b)
    def result(self):
        r=optimize.leastsq(self.residuals,[1,0])
        k,b=r[0]
        print(k,b)
if __name__ == '__main__':
    S=Scipy1()
    S.result()
    l=least_square_fitting()
    l.result()
