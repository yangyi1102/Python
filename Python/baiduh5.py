from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from pyquery import PyQuery
import time
from selenium.webdriver.common.keys import Keys
import re
from base import Base
import json
from img import add_text,b64

chrome_options = webdriver.ChromeOptions()
mobile_emulation = {"deviceName":"iPhone 6"}
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

class BDH5(Base):

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options = chrome_options)
        self.wait = WebDriverWait(self.browser,10)

    def paser_detail(self,task):
        try:
            if task:
                task = task
            else:
                task = self.get_testtask('2', '11', 'h5')
            # task = {"ext":{"jobid":27065},"citycode":"130100","tasktype":1,"pt":2,"poistype":3,"yxl":"","datasource":"h5","shopname":"可欣小吃","shopid":"2022636969","geo":{"longitude":12748300.0,"latitude":4564330.0,"geohash":"2b166a17c6cbdfb6","address":""}}
            shopid = task['shopid']
            latitude = task['geo']['latitude']
            longitude = task['geo']['longitude']
            address = ''
            url = 'http://waimai.baidu.com/mobile/waimai?qt=shopmenu&is_attr=1&shop_id={shopid}&address={address}&lat={latitude}&lng={longitude}'.format(shopid = shopid,address = address,latitude =latitude,longitude =longitude)
            urls = 'http://waimai.baidu.com/mobile/waimai?qt=shopdetail&shop_id={shopid}&address=&lat={latitude}&lng={longitude}'.format(shopid = shopid,latitude = latitude,longitude = longitude)
            self.browser.get(url)
            time.sleep(3)
            doc = PyQuery(self.browser.page_source.replace('xmlns', 'another_attr'))
            not_exist = doc('#market-menu > secion').text()
            if not not_exist == '本店休息中，暂不接受订单':
                self.browser.get(urls)
                time.sleep(5)
                doc = PyQuery(self.browser.page_source.replace('xmlns','another_attr'))
                result = {
                    'platform': task['pt'],
                    'ext': task['ext'],
                    'shopid':task['shopid'],

                    'shopname_snap': doc('div.top-div > div.center-title').text(),
                    'shoppytime_snap':doc('div.time.shopinfo-row > p').text(),
                    'shopaddress_snap':doc('div.address.shopinfo-row > p').text(),
                    'shopphone_snap':doc('div.phone.shopinfo-row > p').text(),
                }
                licenses = re.findall(r'\"shop_certification_info\":\[(.*?)\]',self.browser.page_source)[0]
                licenses_list = licenses.split(',')
                if licenses_list:
                    try:
                        result['shopBimg'] = eval(licenses_list[0]).replace(r'\/', '/')
                        result['shopCimg'] = eval(licenses_list[1]).replace(r'\/', '/')
                        result['shopBimg_snap'] = eval(licenses_list[0]).replace(r'\/','/')
                        result['shopCimg_snap'] = eval(licenses_list[1]).replace(r'\/','/')
                    except Exception as e:
                        pass

                if 'shopBimg_snap' in result.keys():
                    if result['shopBimg_snap']:
                        result['shopBimg_snap'] = b64(result['shopBimg_snap'])
                if 'shopCimg_snap' in result.keys():
                    if result['shopCimg_snap']:
                        result['shopCimg_snap'] = b64(result['shopCimg_snap'])
                time.sleep(2)
                name = 'static/' + str(task['shopid']) + task['datasource'] + 'bd1.png'
                self.browser.get_screenshot_as_file(name)
                result['snapshot1'] = add_text(name)
                data = json.dumps(result)
                # print(data)
                self.upload_testdatas(data)
                self.browser.quit()
            else:
                result = {
                    'platform': task['pt'],
                    'ext': task['ext'],
                    'shopid':task['shopid'],
                }
                name = 'static/' + str(task['shopid']) + task['datasource'] + 'bd4.png'
                self.browser.get_screenshot_as_file(name)
                result['snapshot1'] = add_text(name)
                data = json.dumps(result)
                # print(data)
                self.upload_testdatas(data)
                self.browser.quit()
        except Exception as e:
            self.browser.quit()
            print(e)
            time.sleep(3)
            bdh5 = BDH5()
            return bdh5.paser_detail(task)

if __name__ == '__main__':
    while True:
       bdh5 = BDH5()
       bdh5.paser_detail('')
