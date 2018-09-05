# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 08:49:22 2018

@author: yangyi
"""


import time
import random
import json
#import cv2
import numpy as np
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt

import requests
from bs4 import BeautifulSoup
class Gov_crawl(object):
    def crawl(self):
        url='https://hy.captcha.qq.com/hycdn_1_1657980239702868736_0?aid=2000100680&clientype=2&accver=1&ua=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgNi4yOyBXT1c2NCkgQXBwbGVXZWJLaXQvNTM4LjEgKEtIVE1MLCBsaWtlIEdlY2tvKSBQaGFudG9tSlMvMi4xLjEgU2FmYXJpLzUzOC4x&fpinfo=fpsig%3D1100198FDF86A4FF2BAFD4E24C77E65A891AE0C22906A4BD67E2FA82CC2D38E9B7F99E8082ED264A3A0A55B9DAB79B17EA5F&tkid=1404983276&sess=ue0qK6EO8ZuWyFWLJ5mgXtI5-4qumlrWHyXKoag6jG5cg6riCeggsWkqK30tu6kRY1MhhJLnVQB2V1bLa-DK-zOcDSHB6_OdU_qpkecZs-qBqAg2mZscShLmB3bgCsx2o86GCY5TS3vjmAIQhFFj1aF1GuuLF9Srj-6-x1bpLx7lHWchLlarmzNoqjSxgCZzlNeykNFL1chbcHyLukTwaQ**&theme=undefined&sid=6594677355597549967&showtype=popup&fb=1&forcestyle=undefined&subsid=3&uid=&cap_cd=&lang=2052&rnd=486307&TCapIframeLoadTime=undefined&prehandleLoadTime=63&createIframeStart=1535442972187&rand=0.8864162883255631&websig=4bbf9d631ae71593a25891aebf2d21fd3a59ddb51f1a75dbca0195156e4e7a8f26a88bff65af2b1218ee8149462c4b3bd11a9306a48eac3c4096c03f125fa6bd&vsig=c01InCm42PT4yx-xz1wK3oTM2e5KftV3lLaNrmcaFucJvVqqBLPFhvi06liNEDzQFZxuHQi49GJlrgXloZBJ1CTd53Q6tSpJbT1aG4RusmILmVsygMq1wxU-AhKPMlV_P9_7x5s39M-MgVdlwffPlXpBqF2y4Z7q3LRIQY5QpWdo24*&img_index=1'
        response=requests.get(url)                                                                   #请求获得验证码
        with open('D:/t.png','wb') as f:                                                                   #保存验证码
            f.write(response.content)
        
#         self.driver.save_screenshot('D://aa.png')
#         imgelement = self.driver.find_element_by_xpath('//*[@id="slideBkg"]')  #定位验证码
#         location = imgelement.location  #获取页面的坐标
#         print(location)
#         size=imgelement.size  #获取验证码的长宽
#         print(size)
#         rangle=(int(location['x'+10]),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))              #写成我们需要截取的位置坐标
#         i=Image.open("D://aa.png") #打开截图
#         i.show()
#         frame=i.crop(rangle)                                                                                                                                                                 #使用Image的crop函数，从截图中再次截取我们需要的区域
#         frame.save('D://frame.png')
        
    def Get(self):
        otemp = 'D:\m.png'
        oblk = 'D:\m1.png'
        target = cv2.imread(otemp, 0)
        template = cv2.imread(oblk, 0)
        w, h = target.shape[::-1]
        temp = 'temp.jpg'
        targ = 'targ.jpg'
        cv2.imwrite(temp, template)
        cv2.imwrite(targ, target)
        target = cv2.imread(targ)
        target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
        target = abs(255 - target)
        cv2.imwrite(targ, target)
        target = cv2.imread(targ)
        template = cv2.imread(temp)
        result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)
        x, y = np.unravel_index(result.argmax(), result.shape)
        print(x,y)
        cv2.rectangle(template, (y, x), (y + w, x + h), (0, 249, 0), 1)                                       # 展示圈出来的区域
        cv2.imshow('Show', template)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
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
    c.crawl()
   # c.Get()