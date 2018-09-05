'''
Created on 2018.7.23

@author: yangyi
'''
#coding=utf-8
import re
import requests
from pyquery import PyQuery
import time
import json
import threading
import pymysql
from settings import *
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'referer':'https://item.taobao.com/item.htm?spm=a2106.m885.1000384.64.yzNkXC&id=35833855642&scm=1029.newlist-0.1.50002766&ppath=&sku=&ug=',
            # 'cookie':'cna=Yq2PE0B/XE4CASe0OitNiBWN; t=b17b52ede300bee6c54ee013b183449d; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; uc3=nk2=sFZaPE%2Bm3SI9uw%3D%3D&id2=UUwZ%2BPWd90FAgw%3D%3D&vt3=F8dBz491y%2BnCZWiRqvk%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; lgc=%5Cu53C8%5Cu88AB%5Cu5751%5Cu4E86%5Cu4E36; tracknick=%5Cu53C8%5Cu88AB%5Cu5751%5Cu4E86%5Cu4E36; _cc_=VT5L2FSpdA%3D%3D; tg=0; enc=Yzg7PtRe2yytyO0uYcq7zJRx5GM5NyJL4poDby%2BsCusYbBxlYPNvpv5urYCeZjd8HDFXLaUmxv9%2BX0vrLAdNTA%3D%3D; UM_distinctid=1639ad241713ff-02ea76af211028-39614807-144000-1639ad24172ae9; ubn=p; ucn=center; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; miid=8162144401555698145; mt=ci=-1_0; cookie2=1c9c066c3d9090d09aadbb43790c037b; v=0; _tb_token_=e3d7717e3b1db; uc1=cookie14=UoTeOZ1Sg3PisA%3D%3D; isg=BBQUzwFFM9W6ZqcD4Yf-g7Dx5VJGxTgh1nZsoK71lh8imbTj1n0I58r4nZEBYXCv',
        }

connect = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            db=MYSQL_DBNAME,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
cursor =  connect.cursor()

tasks = []
coll = []
proxy_coll = []
session = requests.Session()


def get_kuaidaili():
    THREADS = 100
    data = "{\"count\":" + str(THREADS) + ",\"ippoolName\":\"tb\"}"
    url = 'http://ippool.bss360.cn/ippool/getdata'
    try:
        if len(proxy_coll):
            pro = proxy_coll.pop()
            # print(pro)
            return pro
        else:
            response = requests.post(url, data=data)
            text = response.text
            proxies = json.loads(text)['data'][0]['ips']
            for proxy in proxies:
                proxy_coll.append(proxy)
            pro = proxy_coll.pop()
            # print(pro)
            return pro
    except Exception as e:
        pass

def retry( url, header, ):
    try:
        proxy =get_kuaidaili()
        real_proxy = {
            "http": proxy,
            "https": proxy,
        }
        response = requests.get(url, headers=header, proxies=real_proxy, timeout=5)
        # print(proxy,response.status_code)
        if response.status_code == 200:
            text = re.findall('onSibRequestSuccess\((.*?)\)', response.text)[0]
            text = json.loads(text)
            c = text['data']['deliveryFee']['data']['sendCity']
            proxy_coll.append(proxy)
            return response
        else:
            return retry(url, header, )
    except Exception as e:
        # print(e)
        return retry(url, header, )

def get_result(href,model,price):
    # href = 'https://item.taobao.com/item.htm?spm=a2106.m885.1000384.64.yzNkXC&id=35833855642&scm=1029.newlist-0.1.50002766&ppath=&sku=&ug=#detail'
    href = 'https://item.taobao.com/item.htm?id=10274337544&scm=1029.newlist-0.1.50002766&ppath=&sku=&ug=#detail'
    response = requests.get(href,headers = headers)
    # print(response.text)
    doc = PyQuery(response.text)
    id = re.findall('id=(.*?)&s', href)[0]
    img_lis = []
    imgs = doc('#J_UlThumb > li  a > img')
    for img in imgs.items():
        img_lis.append(img.attr('data-src'))
    img_lis = ','.join(img_lis)

    result = {
        'url': href,
        'id': id,
        'price': price,
        'title': doc('title').text(),
        'img': img_lis,
        'seller': re.findall('shopName\s+:\s\'(.*?)\',',response.text)[0].encode('utf-8').decode('unicode-escape'),
        'createtime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        'brand': '',
        'wangwang': re.findall('sellerNick\s+:\s\'(.*?)\',',response.text)[0],
        'model': model,
        'area': doc('input[name="region"]').attr('value'),
        'status': '0',
        'remark': '',
        'goods': '',
        'yxl': '',
        'sales': '',
    }
    if re.findall('(此宝贝已下架)',response.text):
        result['status'] = '1'
    xianxi = doc('ul.attributes-list li').items()
    xianxi_dict = {}
    for x in xianxi:
        a = x.text().split(r'：')
        if len(a) == 2:
            xianxi_dict[a[0].strip()] = a[1].strip()
        elif len(a) > 2:
            pass
        else:
            a = a[0].split(r':')
            xianxi_dict[a[0].strip()] = a[1].strip()
    validity = doc('div.tb-validity').text()
    a = validity.split(':')
    if len(a) == 2:
        xianxi_dict[a[0].strip()] = a[1].strip()
    elif len(a) > 2:
        pass
    else:
        a = a[0].split(r':')
        if len(a) == 2:
            xianxi_dict[a[0].strip()] = a[1].strip()
    if '品牌' in xianxi_dict.keys():
        result['brand'] = xianxi_dict['品牌']
    goods_lis = []
    for k, v in xianxi_dict.items():
        goods_lis.append(k + ':' + v)
    result['goods'] = ';'.join(goods_lis)
    # print(result)
    url = 'https://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId={id}&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract&callback=onSibRequestSuccess'.format(id=id)
    response = requests.get(url,headers = headers)
    text = re.findall('onSibRequestSuccess\((.*?)\)',response.text)[0]
    text = json.loads(text)
    result['area'] = text['data']['deliveryFee']['data']['sendCity']
    result['yxl'] = text['data']['soldQuantity']['confirmGoodsCount']
    remark_list = []
    if text['data']['couponActivity']['coupon'] == {}:
        pass
    else:
        for remark in text['data']['couponActivity']['coupon']['couponList']:
            remark_list.append(remark['title'])
        if remark_list:
            result['remark'] = ','.join(remark_list)
    # print(result)
    urls = 'https://rate.taobao.com/detailCount.do?_ksTS=1527932960890_157&callback=jsonp158&itemId={id}'.format(id = id)
    response = requests.get(urls,headers = headers)
    result['sales'] = re.findall('\({\"count\":(\d+)}\)',response.text)[0]
    print(result)

def get_results(href,model,price):
    response = requests.get(href, headers=headers)
    doc = PyQuery(response.text)
    id = re.findall('id=(.*?)&s', href)[0]
    img_lis = []
    imgs = doc('#J_UlThumb > li  a > img')
    for img in imgs.items():
        img_lis.append(img.attr('data-src'))
    img_lis = ','.join(img_lis)

    result = {
        'url': href,
        'id': id,
        'price': price,
        'title': doc('title').text(),
        'img': img_lis,
        'seller': re.findall('shopName\s+:\s\'(.*?)\',', response.text)[0].encode('utf-8').decode('unicode-escape'),
        'createtime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        'brand': '',
        'wangwang': re.findall('sellerNick\s+:\s\'(.*?)\',', response.text)[0],
        'model': model,
        'area': doc('input[name="region"]').attr('value'),
        'status': '0',
        'remark': '',
        'goods': '',
        'yxl': '',
        'sales': '',
    }
    if re.findall('(此宝贝已下架)', response.text):
        result['status'] = '1'
    xianxi = doc('ul.attributes-list li').items()
    xianxi_dict = {}
    for x in xianxi:
        a = x.text().split(r'：')
        if len(a) == 2:
            xianxi_dict[a[0].strip()] = a[1].strip()
        elif len(a) > 2:
            pass
        else:
            a = a[0].split(r':')
            xianxi_dict[a[0].strip()] = a[1].strip()
    validity = doc('div.tb-validity').text()
    a = validity.split(':')
    if len(a) == 2:
        xianxi_dict[a[0].strip()] = a[1].strip()
    elif len(a) > 2:
        pass
    else:
        a = a[0].split(r':')
        if len(a) == 2:
            xianxi_dict[a[0].strip()] = a[1].strip()
    if '品牌' in xianxi_dict.keys():
        result['brand'] = xianxi_dict['品牌']
    goods_lis = []
    for k, v in xianxi_dict.items():
        goods_lis.append(k + ':' + v)
    result['goods'] = ';'.join(goods_lis)
    # print(result)
    url = 'https://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId={id}&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract&callback=onSibRequestSuccess'.format(
        id=id)
    # response = requests.get(url, headers=headers)
    response = retry(url,headers)
    print(response.text)
    text = re.findall('onSibRequestSuccess\((.*?)\)', response.text)[0]
    text = json.loads(text)
    result['area'] = text['data']['deliveryFee']['data']['sendCity']
    result['yxl'] = text['data']['soldQuantity']['confirmGoodsCount']
    remark_list = []
    if text['data']['couponActivity']['coupon'] == {}:
        pass
    else:
        for remark in text['data']['couponActivity']['coupon']['couponList']:
            remark_list.append(remark['title'])
        if remark_list:
            result['remark'] = ','.join(remark_list)
    # print(result)
    urls = 'https://rate.taobao.com/detailCount.do?_ksTS=1527932960890_157&callback=jsonp158&itemId={id}'.format(id=id)
    response = requests.get(urls, headers=headers)
    result['sales'] = re.findall('\({\"count\":(\d+)}\)', response.text)[0]
    # print(result)
    coll.append(result)

def get_task():
    global tasks
    query = 'SELECT href,model,price from dalianhuazhuang WHERE href LIKE "%taobao%"'
    # query = 'SELECT href,model,price from dalianhref WHERE model = "水果蔬菜/水产肉类/熟食" AND href LIKE "%taobao%"'
    # query = 'SELECT href,model,price from dalianhref WHERE model = "零食/坚果/特产" AND href LIKE "%taobao%"'
    # query = 'SELECT href,model,price from dalianhref WHERE model = "保健滋补医药器械" AND href LIKE "%taobao%"'
    # query = 'SELECT href,model,price from dalianhref WHERE model = "茶/咖啡/冲饮/饮料" AND href LIKE "%taobao%"'
    # query = 'SELECT href,model,price from dalianhref WHERE model = "参茸滋补" AND href LIKE "%taobao%"'
    # query = 'SELECT href,model,price from dalianhref WHERE model = "酒类" AND href LIKE "%taobao%"'
    cursor.execute(query)
    connect.commit()
    for x in cursor:
        print(x)
        tasks.append(x)
    # tasks = tasks[0:2200]
def execute():
    time.sleep(5)
    while True:
        try:
            if len(tasks):
                task = tasks.pop()
                print(task,len(tasks))
                if re.findall('taobao', task[0]):
                    get_results('https:' + task[0],task[1],task[2])
            else:
                time.sleep(1)
            # time.sleep(1)
        except Exception as e:
            print(e)

def insert_sql():
    time.sleep(7)
    while True:
        try:
            if len(coll):
                result = coll.pop()
                cursor.execute(
                    """insert into dalianbeauty (id,sales,title,img,seller,createtime,price,brand,model,wangwang,goods,url,area,status,remark,yxl)
                    value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (result['id'],
                     result['sales'],
                     result['title'],
                     result['img'],
                     result['seller'],
                     result['createtime'],
                     result['price'],
                     result['brand'],
                     result['model'],
                     result['wangwang'],
                     result['goods'],
                     result['url'],
                     result['area'],
                     result['status'],
                     result['remark'],
                     result['yxl']
                     ))
                connect.commit()
                print('insert',result)
        except Exception as e:
            print(e)
def reConnect():
    global connect
    try:
        connect.ping()
    except Exception as e:
        connect = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            db=MYSQL_DBNAME,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
def main():
    get_result('','','')

if __name__ == '__main__':
    get_task()
    time.sleep(5)
    for x in range(0,100):
        t = threading.Thread(target=execute)
        t.start()
    i = threading.Thread(target=insert_sql)
    i.start()
    # get_results('https://item.taobao.com/item.htm?id=8840528772&scm=1029.newlist-0.1.50035978&ppath=&sku=&ug=#detail','','')
