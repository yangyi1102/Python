import requests,time,re
from suma import SuMa
from rk import RClient
import pymysql
from settings import *
import random
import string
import sys
import os
count = 4

class ZhiMa():
    def __init__(self):
        self.connect = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            db='brand',
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()

    def getPic(self):
        session = requests.Session()
        url = 'http://web.http.cnapi.cc/core/api/verify?&time0.3109564345412752'
        response = session.get(url)
        with open('a.png','wb') as f:
            f.write(response.content)
        return session

    def getVocde(self,mobile,vcode,session):
        url = 'http://web.http.cnapi.cc/index/users/get_phone_code?jsonpcallback=jQuery112408039848142913559_1531052161331&phone={mobile}&type=reg&reg_verfy={vcode}&_={times}'.format(
            mobile = mobile,vcode = vcode,times = round(time.time()*1000)
        )
        response = session.get(url)
        print(response.text)
        code = re.findall(r'\\"code\\":\\"(.*?)\\",',response.text)[0]
        print(repr(code))
        return code

    def login(self,mobile,vcode,phone_code,session):
        # session = requests.Session()
        reg_name = ''.join(random.sample(string.ascii_letters + string.digits,11))
        password = ''.join(random.sample(string.ascii_letters + string.digits,11))
        url = 'http://web.http.cnapi.cc/index/users/reg_do?jsonpcallback=jQuery112407751394446607325_1531090523021&reg_name={reg_name}&password={password}&re_password={password}&verfy={verfy}&phone={mobile}&phone_code={phone_code}&origin_tail=&expandsecret=&_={times}'.format(
            reg_name = reg_name,verfy = vcode,mobile = mobile,phone_code = phone_code,times = round(time.time()*1000),password = password
        )
        response = session.get(url)
        print(response.text)

        free_proxy_url = 'http://web.http.cnapi.cc/index/users/get_day_free_pack?jsonpcallback=jQuery112402688617050157798_1531091032844&_={times}'.format(times = round(time.time()*1000))
        response = session.get(free_proxy_url)
        print(response.text)

        get_api_url = 'http://web.http.cnapi.cc/index/users/user_info?jsonpcallback=jQuery112403700568020093141_1531091978447&_={times}'.format(times = round(time.time()*1000))
        response = session.get(get_api_url)
        mid = re.findall(r'\\"id\\":(\d+),', response.text)[0]

        url = 'http://web.http.cnapi.cc/index/api/get_package_info?jsonpcallback=jQuery1124004920459270050209_1531101857248&mid={mid}&_={times}'.format(mid = mid,times = round(time.time()*1000))
        response  = session.get(url)
        id = re.findall(r'data-id=\\\\\\"(\d+)\\\\\\"',response.text)[0]

        urls = 'http://web.http.cnapi.cc/index/api/new_get_ips?jsonpcallback=jQuery112408124116324249324_1531103092093&num=1&package_id={id}&type=1&pro_id=&port_type=1&city_id=&yys=0&time_show=false&city_show=false&yys_show=false&manyregions=&region_type=1&line_break=1&special_break=&port_bit=4&m_repeat=1&pack_type=pack&_={times}'.format(
            id = id,times = round(time.time()*1000)
        )
        response = session.get(urls)
        print(response.text)
        # urls = 'http://web.http.cnapi.cc/index/api/new_get_ips?jsonpcallback=jQuery112408124116324249324_1531103092093&num=1&package_id={id}&type=1&pro_id=&port_type=1&city_id=&yys=0&time_show=false&city_show=false&yys_show=false&manyregions=&region_type=1&line_break=1&special_break=&port_bit=4&m_repeat=1&pack_type=pack&_={times}'.format(
        #     id=id, times=round(time.time() * 1000)
        # )
        # response = session.get(urls)
        # print(response.text)

        api = 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=0&port=1&pack={id}&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='.format(id=id)
        cookie = 'PHPSESSID=' + session.cookies['PHPSESSID'] + ';'

        result = {
            'username':reg_name,
            'password':password,
            'mobile':mobile,
            'api':api,
            'cookie':cookie,
            'id':id,
        }
        print(result)
        self.insert_mysql(result)

    # def getFreeProxy(self):
    #     url = 'http://web.http.cnapi.cc/index/users/get_day_free_pack?jsonpcallback=jQuery112402688617050157798_1531091032844&_={times}'.format(times = round(time.time()*1000))
    #     response = requests.get(url)
    #     print(response.text)
    #
    # def getApi(self):
    #     url = 'http://web.http.cnapi.cc/index/users/user_info?jsonpcallback=jQuery112403700568020093141_1531091978447&_={times}'.format(times = round(time.time()*1000))
    #     response = requests.get(url)
    #     id = re.findall('\"id\":(\d+),',response.text)[0]

    def insert_mysql(self,result):
        self.cursor.execute(
            """insert into {table} (username, password, mobile, api, cookie, id)
            value (%s, %s, %s, %s, %s, %s)""".format(table=TABLE),
            (result['username'],
             str(result['password']),
             str(result['mobile']),
             result['api'],
             result['cookie'],
             result['id'])
        )
        self.connect.commit()

if __name__ == '__main__':
    while True:
        try:
            suma = SuMa()
            rc = RClient('tosshl1985', 'sa123456', '106174', '4a5d4d1e0d334a5b8f59e1ad94ada2cc')
            zhima = ZhiMa()
            mobile = suma.mobile
            session = zhima.getPic()
            vcode = rc.run()
            code = zhima.getVocde(mobile,vcode,session)
            if code == '1':
                print('ok')
                phone_code = suma.getVcodeAndHoldMobilenum()
                if phone_code:
                    zhima.login(mobile, vcode, phone_code,session)
            else:
                suma.addIgnoreList(mobile)
                pass
        except Exception as e:
            print(e)
        finally:
            time.sleep(100)
            # os.system('call f:\宽带连接.bat')


