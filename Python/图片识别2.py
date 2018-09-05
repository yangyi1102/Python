'''
Created on 2018年8月8日

@author: yangyi
'''
#coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
class Picture(object):
    def getPicture(self):
        filename = 'D:/m.jpg'
        self.img = cv2.imread(filename)
    def Px(self):
        px=self.img[100,100]
        print(px)
        blue=self.img[100,100,0]
        print(blue)
    def getPicinf(self):
        print(self.img.shape)
        print(self.img.size, self.img.dtype)
    def getinf(self):
        gray = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)
        dst = cv2.cornerHarris(gray,2,3,0.2)
        #result is dilated for marking the corners, not important
        dst = cv2.dilate(dst,None)
        # Threshold for an optimal value, it may vary depending on the image.
        self.img[dst>0.01*dst.max()]=[20,5,255]
        cv2.imshow('dst',self.img)
        if cv2.waitKey(0) & 0xff == 27:
            cv2.destroyAllWindows()
#     def getinf(self):
#         surf = cv2.xfeatures2d.SURF_create(400)
#         kp = surf.detect(self.img,None)
    def fazhi(self):
        ret,th1 = cv2.threshold(self.img,127,255,cv2.THRESH_BINARY)
        th2 = cv2.adaptiveThreshold(self.img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
        th3 = cv2.adaptiveThreshold(self.img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\cv2.THRESH_BINARY,11,2)
        titles = ['Original Image', 'Global Thresholding (v = 127)',
                    'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
        images = [self.img, th1, th2, th3]
        for i in range(4):
            plt.subplot(2,2,i+1),
            plt.imshow(images[i],'gray')
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])
        plt.show()
if __name__ == '__main__':
    P=Picture()
    P.getPicture()
    P.fazhi()
#     P.Px()
#     P.getPicinf()
#     P.getinf()