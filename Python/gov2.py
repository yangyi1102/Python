'''
Created on 2018年8月28日

@author: yangyi
'''
#coding=utf-8
import time
import random
import json

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

import cv2
import numpy as np
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt

import requests
from bs4 import BeautifulSoup
class Gov_crawl(object):
    def __init__(self):
        self.driver=webdriver.Chrome()         #打开Google chrome
        self.wait=WebDriverWait(self.driver,100000)
    def Geturl(self):
        self.driver.maximize_window()
        url='https://www.tm.cn/search'
        self.driver.get(url)
        enterword=self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#searchvalue")))
        enterword.send_keys("歌乐")
        self.driver.find_element_by_xpath('//*[@id="TencentCaptcha"]').click()
        time.sleep(4)
        ifame=self.driver.find_element_by_xpath('//*[@id="tcaptcha_popup"]')
        self.driver.switch_to_frame(frame_reference=ifame)
        time.sleep(5)
        for element in self.driver.find_elements_by_xpath('//*[@id="slideBkg"]'):
            Bkg_url = element.get_attribute('src')
            print(Bkg_url)
            Bkg_response=requests.get(Bkg_url)
            with open('D:/1.png','wb') as f:                                                                      #保存背景图
                f.write(Bkg_response.content)
            img = Image.open('D:/1.png')
            out = img.resize((340, 195),Image.ANTIALIAS) #resize image with high-quality
            out.save('D:/1.png')
        for element in self.driver.find_elements_by_xpath('//*[@id="slideBlock"]'):
            Block_url=element.get_attribute('src')                                
            Block_response=requests.get(Block_url)                                                    #保存背景图
            with open('D:/2.png','wb') as f:                                                                   
                f.write(Block_response.content)
            img = Image.open('D:/2.png')
            out = img.resize((64,64),Image.ANTIALIAS) #resize image with high-quality
            out.save('D:/2.png')
        #self.driver.save_screenshot('D://aa.png')
#         i=Image.open("D://aa.png") #打开截图
#         x = 791
#         y = 347
#         w = 340
#         h = 195
#         frame=i.crop((x, y, x+w, y+h))                                                                                                                                                            #使用Image的crop函数，从截图中再次截取我们需要的区域
#         frame.save('D:/1.png')
#         imgelement = self.driver.find_element_by_xpath('//*[@id="slideBkg"]')  #定位验证码
#         location = imgelement.location  #获取页面的坐标
#         print(location)
#         size=imgelement.size  #获取验证码的长宽
#         print(size)
#         rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))              #写成我们需要截取的位置坐标
#         i=Image.open("D://aa.png") #打开截图
#         i.show()
#         frame=i.crop(rangle)
#         frame.show()                                                                                                                                                              #使用Image的crop函数，从截图中再次截取我们需要的区域
#         frame.save('D://frame.png')
    def Get(self):
        otemp = 'D:/2.png'                     #小图
        oblk = 'D:/1.png'                 #背景图
        target = cv2.imread(otemp, 0)           #打开图片
        template = cv2.imread(oblk, 0)         #打开图片
        w, h = target.shape[::-1]                         ##获得小方块
        print(w,h)
        temp = 'temp.jpg'
        targ = 'targ.jpg'
        cv2.imwrite(temp, template)              
        cv2.imwrite(targ, target)
        target = cv2.imread(targ)
        target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)   #颜色转换成灰度
        target = abs(255 - target)                                                    
        cv2.imwrite(targ, target)
        target = cv2.imread(targ)
        template = cv2.imread(temp)
        result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)      #两张图片对比获取缺口                                                    
        x, y = np.unravel_index(result.argmax(), result.shape)
        print(x,y)
        cv2.rectangle(template, (y, x), (y + w, x + h), (0, 249, 0), 1)                                                                              # 展示圈出来的区域
        cv2.imshow('Show', template)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        source=self.driver.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
        
        ActionChains(self.driver).drag_and_drop_by_offset(source,y-21+7,0).perform()
#         action = ActionChains(self.driver)
#         action.move_to_element(source)
#         action.click_and_hold().perform()
#         self.driver.switch_to_default_content()
#         action = ActionChains(self.driver)
#         action.move_by_offset(0.1,0).perform()
#         time.sleep(1)
#         action.move_by_offset(0.2,0).perform()
#         time.sleep(0.5)
#         action.move_by_offset(0.3,0).perform()
#         time.sleep(1)
#         action.move_by_offset(0.3,0).perform()
#         time.sleep(1)
#         action.move_by_offset(0.3,0).perform()
#         time.sleep(1)
#         action.move_by_offset(0.3,0).perform()
#         time.sleep(1)
#         action.move_by_offset(y-21+7,0).perform()
#         time.sleep(1)
#         action.move_by_offset(0.01,0).perform()
#         time.sleep(1)
#         action.release().perform()
#         action.move_by_offset(20, 0).perform()
#         time.sleep(1)
#         action.move_by_offset(y-21-20-20+7, 0).perform()
#         action.release().perform()
#         canvas_img=self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#slideBkg")))
#         print(canvas_img)
#         position=self.get_position(canvas_img)
#         befor_screenshot=self.get_screenshot()
#         befor_img=befor_screenshot.crop(position)
#         befor_img.save("befor_click.png")
#         btn_slide=self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,"#slideBkg")))
#         self.action.click_and_hold(btn_slide).perform()
#         after_screenshot=self.get_screenshot()
#         after_img=after_screenshot.crop(position)
#         after_img.save("after_click.png")
    
        
        
        
if __name__ == '__main__':
    c=Gov_crawl()
    c.Geturl()
    x,y=c.Get()
#   c.Get_page()
