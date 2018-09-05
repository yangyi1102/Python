# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 16:20:55 2018

@author: 17549
"""

import requests as Re
from bs4 import BeautifulSoup
from lxml import etree
from pyquery import PyQuery as PQ
import json
import demjson
import re
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Referer':'https://shopsearch.taobao.com/search?app=shopsearch&q=%E8%BF%90%E5%8A%A8&js=1&initiative_id=staobaoz_20180709&ie=utf8&loc=%E6%B9%96%E5%B7%9E'
        }
headers['cookie'] = 'thw=cn; cna=Q9fFE/ag00QCAXr2NFx685jZ; t=df2b9cd02bf64c2d0ae70f99649fe2cf; ali_ab=122.246.52.92.1531114009052.6; _m_h5_tk=6b527153b15b9924daa9fd9a03c47502_1531115809860; _m_h5_tk_enc=4bb05a8ff985548a04394bee9982ff57; mt=ci%3D-1_0; JSESSIONID=512BD6FF5725878C2661A35B332A6200; isg=BJycKz0XK-2MgN8x1I_OBN3nbbqOvUyV4SDVRnadqAdqwTxLniUQzxJzJWmc0niX'
page=Re.get('https://shopsearch.taobao.com/search?app=shopsearch&q=%E8%BF%90%E5%8A%A8&js=1&initiative_id=staobaoz_20180709&ie=utf8&loc=%E6%B9%96%E5%B7%9E&s=40',headers=headers)
#hjson=json.dumps(page.text)
#text = re.findall(r'(\"userRateUrl\":.*?\"auctionsInshop\")',page.text)
pattern=re.compile(r'{\"uid\":.*?}')
text = re.findall(pattern,page.text)
a=text[0]
pattern1=re.compile(r'\"uid\":.*?')
b=re.findall(pattern1,a)
print(repr(b))

#b = json.loads(a)
#print(b['title'])
#print(a['title'])
   
#for i in text:
 #    print(text[i])
 #   print('''''''''''''''''''''''''''''''''''''''''''''''''''''''''''')
#print(page.text)