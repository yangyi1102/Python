'''
Created on 2018.7.23

@author: yangyi
'''
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.keys import Keys
import time,datetime
import random
import pyautogui
import pymysql
#from settings import browser
class MeiTuanLogic():
    def Chrome_option(self):
        chrome_options = webdriver.ChromeOptions()
        mobile_emulation = {"deviceName": "iPhone 6"}
        browser=chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.browser=webdriver.Chrome(chrome_options=chrome_options)                            
        return self.browser
    def Logic(self,account):
        self.browser.get('https://i.meituan.com/account/login?backurl=http%3A%2F%2Fi.waimai.meituan.com%2Faccount%2FaccountCenter%3Fsource%3D1')
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/div[2]/dl/dd/ul/li[2]/a').click()        
        username=account
        for i in username:
            Mobile=self.browser.find_element_by_xpath('//*[@id="username"]').send_keys(i)        
            time.sleep(0.1)
        password='bssbss360'
        for i in password:
            Vcode=self.browser.find_element_by_xpath('//*[@id="password"]').send_keys(i)         
            time.sleep(0.1)
        time.sleep(random.randint(0,5))
        a = self.browser.find_element_by_xpath('/html/body/div[2]/form[1]/div[1]/button')
        a.send_keys(Keys.ENTER)
        time.sleep(3)
    def Exploit(self):
        pyautogui.press('f12')               
        time.sleep(2)
        pyautogui.keyDown('CTRL')  
        pyautogui.hotkey('shift','m')
        pyautogui.keyUp('CTRL')              
        time.sleep(2)                         
        pyautogui.moveTo(200,650)             
        pyautogui.dragTo(460,650,duration=0.4) 
        time.sleep(2) 
        pyautogui.press('f12') 
        print('ok')
    def Cookies(self):
        Cookie_List=self.browser.get_cookies()
        co=[]
        for i in Cookie_List:
            c=i['name']+'='+i['value']
            co.append(c)
        return ';'.join(co),Cookie_List
    def Save(self,phone,cookie,cookie1):
        password='bssbss360'
        print(cookie)
        lis=str(cookie1)
        print(lis)
        db=pymysql.connect(host='bsswaiwang.mysql.rds.aliyuncs.com',port=3306,user= 'sp_data_group',password = '4ydEe7EfrzEH',database='brand')
        cur=db.cursor()
        sql='INSERT INTO yangmeituancookie_copy(PhoneNumber,password,Cookies,Cookies1,Time) VALUES(%s,%s,%s,%s,%s);'       
        t=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(t)
        cur.execute(sql, [phone,password,cookie,lis,t])
        db.commit()
        print('ok')
    def OpenPhoneNumList(self):
        with open("phone1.txt","r") as f:
            Phones=f.read()
            List_Num=Phones.split('\n')
        return List_Num       
if __name__ == '__main__':
    M=MeiTuanLogic()
    NUM=M.OpenPhoneNumList()
    print(NUM)
    for i in NUM:
        print()
        M.Chrome_option()                  
        M.Logic(i)
        time.sleep(3)
        M.Exploit()
        time.sleep(2)
        cookie,cls=M.Cookies()
        M.Save(i,cookie,cls)
        time.sleep(4) 
        M.Chrome_option().close()








