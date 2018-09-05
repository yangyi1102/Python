# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 17:07:02 2018

@author: 17549
"""

import requests
from bs4 import BeautifulSoup
import json
import re
from nltk.tokenize import word_tokenize,regexp_tokenize
import json
class alibb(object):
    def __init__(self):
        self.header={
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36',
            'template_path': 'mNJ82OKsx5s2joeKgTh0i1G0U4Q2ouVLv8Ws7eQmXS2C7sJaeRYoU++E41/G5bjA',
            'cookie': '__sw_newuno_count__=1; UM_distinctid=1651dbce6962a4-046e9a983493c-7d12364c-144000-1651dbce697c81; cna=BOXyE30SEV0CAXr2Mzb14DSP; ali_ab=122.246.51.54.1533802244251.5; JSESSIONID=9L78A7N92-6m9al2RFpcXT3vRl09-eIuFD0R-op0V; cookie2=1f5e976a25f11a22af4f171413ad8a77; t=b609b5fdb4d9e82cc4653300aa958216; _tb_token_=f87b1375b31ee; cookie1=VTrgqrtmSEkb1vW9bLIn%2F%2BnNw%2BKBZf5Ur5Noef3xlUQ%3D; cookie17=UNX57RsrJgaEtQ%3D%3D; sg=469; csg=3b0a5363; lid=weiteniu4; __cn_logon__=true; __cn_logon_id__=weiteniu4; ali_apache_track=c_mid=b2b-3527265906b3cc4|c_lid=weiteniu4|c_ms=1; ali_apache_tracktmp=c_w_signed=Y; LoginUmid=%2BrCFOTWmtzucC%2FE3zxiOV1OGGXDrW0klxXUL9cXapyZqJGrd38HGVQ%3D%3D; unb=3527265906; tbsnid=WeSlDCFaf17nfBs0kCjPuNt4G10Mq7t5uL42H6KzfUE6sOlEpJKl9g%3D%3D; cn_tmp="Z28mC+GqtZ3pVcpj1FDJbylKVPNhjM+1HZotR6rW4IL9ihNX6MHJO2LVMC4AHHiVloe6fXT3DVkXtem4OH0fJaXfhJ84mf8MVnbUa2TTrHIqszRXV4cCcZ1nu6KaYYMvq9FvV62uwyIC12H8rsCXE2nH1bfYTqkxEoaC2T3pgjzVPY65X0hLNDWNPScfy3veOEagmBNKedDgTHaojf7v2visbfS90ud9JjWsgHn+xLfusOferB6bvZ7ZeZj18BXU12c4aJgNgZo="; login=kFeyVBJLQQI%3D; userID=FRXpE4wIc%2FDm%2BQ33NaABoQlk57C%2FZn5J6LyWy9BGNDk6sOlEpJKl9g%3D%3D; _nk_=%2B01ddgv%2FKXgDBPJBu4sTUQ%3D%3D; userIDNum=E4BejoMSHJPTREwxOZGXtg%3D%3D; last_mid=b2b-3527265906b3cc4; __last_loginid__=weiteniu4; _cn_slid_=q6ihNvlWbb; _tmp_ck_0=ekwXrK5b5k3NtG%2BeBFSpxKovo6gROS3KavhmXHsMr53Lswj64nct%2FCidXSaIfqZeRbqHPxoVCICeoyLgtLCpah9KOXtyx6g3WZ4t1ALtMJE0gt2%2BuGNh3KP8bwpDzvZa57%2B7%2BycD8w3BxlOUAFYLuMkACYSyeVUbGaUNltNfT7aoQgBhbXFYf3EnbL9ogpXcg07qI%2FmdP4S6uT14dW2%2BCLrhW7GYFUOJjN1Q40bgFP8pksy374hWExxxMbkJ%2Bojjrj01vO6APuZS8EnPciBFF41Fk0gRdTETjHfyubOPuKM9ctCO%2FZsNsEUdShCx7TJMS3Hh%2FJyTI8Cm33PWc3HMq2Z2vTaUBYXm%2B6rHue5xgTDqnAhn1bg2x4eUJCBcK%2FLY17gDZmm4jYbSof6Q6SkxDBSsRyfT7agxRcD5oOlB2uY7K1XGlhJ%2FUG51TLud2SVOseervT8uKzpL8%2BppLJz0ed6KaL%2Fn90kiTOxpJqYqtBC1o5HmAVqchDBzd8QqeGTwvqwoTVKMBrVACFQ36hpzyg%3D%3D; _csrf_token=1533802274542; h_keys="%u8863%u670d"; alisw=swIs1200%3D1%7C; _is_show_loginId_change_block_=b2b-3527265906b3cc4_false; _show_force_unbind_div_=b2b-3527265906b3cc4_false; _show_sys_unbind_div_=b2b-3527265906b3cc4_false; _show_user_unbind_div_=b2b-3527265906b3cc4_false; __rn_alert__=false; alicnweb=homeIdttS%3D02852562865789933537399413842419099810%7ChomeIdttSAction%3Dtrue%7Ctouch_tb_at%3D1533802253693%7Clastlogonid%3Dweiteniu4%7Cshow_inter_tips%3Dfalse; ad_prefer="2018/08/09 16:54:08"; isg=BFtbdMdZhI5YPfjIkyn5TUVq6r8FmGPuBq5X302akNqZLHsO1QK9gr3uwswHaMcq',
            #'cookie': '__sw_newuno_count__=1; UM_distinctid=1651dbce6962a4-046e9a983493c-7d12364c-144000-1651dbce697c81; cna=BOXyE30SEV0CAXr2Mzb14DSP; ali_ab=122.246.51.54.1533802244251.5; JSESSIONID=9L78A7N92-6m9al2RFpcXT3vRl09-eIuFD0R-op0V; cookie2=1f5e976a25f11a22af4f171413ad8a77; t=b609b5fdb4d9e82cc4653300aa958216; _tb_token_=f87b1375b31ee; cookie1=VTrgqrtmSEkb1vW9bLIn%2F%2BnNw%2BKBZf5Ur5Noef3xlUQ%3D; cookie17=UNX57RsrJgaEtQ%3D%3D; sg=469; csg=3b0a5363; lid=weiteniu4; __cn_logon__=true; __cn_logon_id__=weiteniu4; ali_apache_track=c_mid=b2b-3527265906b3cc4|c_lid=weiteniu4|c_ms=1; ali_apache_tracktmp=c_w_signed=Y; LoginUmid=%2BrCFOTWmtzucC%2FE3zxiOV1OGGXDrW0klxXUL9cXapyZqJGrd38HGVQ%3D%3D; unb=3527265906; tbsnid=WeSlDCFaf17nfBs0kCjPuNt4G10Mq7t5uL42H6KzfUE6sOlEpJKl9g%3D%3D; cn_tmp="Z28mC+GqtZ3pVcpj1FDJbylKVPNhjM+1HZotR6rW4IL9ihNX6MHJO2LVMC4AHHiVloe6fXT3DVkXtem4OH0fJaXfhJ84mf8MVnbUa2TTrHIqszRXV4cCcZ1nu6KaYYMvq9FvV62uwyIC12H8rsCXE2nH1bfYTqkxEoaC2T3pgjzVPY65X0hLNDWNPScfy3veOEagmBNKedDgTHaojf7v2visbfS90ud9JjWsgHn+xLfusOferB6bvZ7ZeZj18BXU12c4aJgNgZo="; login=kFeyVBJLQQI%3D; userID=FRXpE4wIc%2FDm%2BQ33NaABoQlk57C%2FZn5J6LyWy9BGNDk6sOlEpJKl9g%3D%3D; _nk_=%2B01ddgv%2FKXgDBPJBu4sTUQ%3D%3D; userIDNum=E4BejoMSHJPTREwxOZGXtg%3D%3D; last_mid=b2b-3527265906b3cc4; __last_loginid__=weiteniu4; _cn_slid_=q6ihNvlWbb; _tmp_ck_0=ekwXrK5b5k3NtG%2BeBFSpxKovo6gROS3KavhmXHsMr53Lswj64nct%2FCidXSaIfqZeRbqHPxoVCICeoyLgtLCpah9KOXtyx6g3WZ4t1ALtMJE0gt2%2BuGNh3KP8bwpDzvZa57%2B7%2BycD8w3BxlOUAFYLuMkACYSyeVUbGaUNltNfT7aoQgBhbXFYf3EnbL9ogpXcg07qI%2FmdP4S6uT14dW2%2BCLrhW7GYFUOJjN1Q40bgFP8pksy374hWExxxMbkJ%2Bojjrj01vO6APuZS8EnPciBFF41Fk0gRdTETjHfyubOPuKM9ctCO%2FZsNsEUdShCx7TJMS3Hh%2FJyTI8Cm33PWc3HMq2Z2vTaUBYXm%2B6rHue5xgTDqnAhn1bg2x4eUJCBcK%2FLY17gDZmm4jYbSof6Q6SkxDBSsRyfT7agxRcD5oOlB2uY7K1XGlhJ%2FUG51TLud2SVOseervT8uKzpL8%2BppLJz0ed6KaL%2Fn90kiTOxpJqYqtBC1o5HmAVqchDBzd8QqeGTwvqwoTVKMBrVACFQ36hpzyg%3D%3D; _csrf_token=1533802274542; h_keys="%u8863%u670d"; alisw=swIs1200%3D1%7C; _is_show_loginId_change_block_=b2b-3527265906b3cc4_false; _show_force_unbind_div_=b2b-3527265906b3cc4_false; _show_sys_unbind_div_=b2b-3527265906b3cc4_false; _show_user_unbind_div_=b2b-3527265906b3cc4_false; __rn_alert__=false; alicnweb=homeIdttS%3D02852562865789933537399413842419099810%7ChomeIdttSAction%3Dtrue%7Ctouch_tb_at%3D1533802253693%7Clastlogonid%3Dweiteniu4%7Cshow_inter_tips%3Dfalse; isg=BM7Ogl8lGVIjxa1Dhma0hpj9H6RQ556Vy_kiFPgWO1HeW261YdxSWdkRl8eSp4ph; ad_prefer="2018/08/09 16:11:50',
            'referer':'https://www.1688.com/?spm=b26110380.sw1688.2.1.3f734220qNnN6M',
        }
    def Get_Url_list(self):
        url='https://s.1688.com/selloffer/offer_search.htm?keywords=%D2%C2%B7%FE&n=y&spm=a260k.635.3262836.d102&sug=1_0&beginPage=1&offset=9&filterP4pIds=571721145180,569267700356,569177624624,564909632536,568274297688,554912213310,549172838285,541717283914'
        respone=requests.get(url,headers=self.header)
        respone.encoding='gbk'
        soup=BeautifulSoup(respone.text,'lxml')
        print(soup)
    def Get_url_lis(self):
        lis=[]
        url='https://s.1688.com/selloffer/rpc_async_render.jsonp?keywords=%B4%B4%BA%E3&qrwRedirectEnabled=false&n=y&uniqfield=pic_tag_id&leftP4PIds=42313419257%2C564032621329%2C541319297957&filterP4pIds=42313419257%2C564032621329%2C541319297957&beginPage=3&templateConfigName=marketOfferresult&offset=4&pageSize=60&asyncCount=60&startIndex=40&async=true&enableAsync=true&rpcflag=new&_pageName_=market&callback=jQuery17208370595274004546_1534145963209'
        response=requests.get(url,headers=self.header)
        
        html=re.findall(r'<a tclick.*/a>',response.text)[0]
        text = html.replace('\\\"','').replace('\\n','').replace('\\','')
        soup=BeautifulSoup(text,'lxml')
        for i in soup.find_all("a",attrs={'href':re.compile(r'^https://deta')}):  
            lis.append(i['href'])
        ids = list(set(lis))
        for i in ids:
            print(i)
        print(len(ids))
    def Get_Goods_inf(self):
        url='https://detail.1688.com/offer/44716734787.html'
        response=requests.get(url,headers=self.header)
        soup=BeautifulSoup(response.text,'lxml')
        print(soup)
        title=soup.find('title').text
        Area=soup.find('meta',{'name':'location'})
        shopurl=soup.find('div',{'class':'base-info'}).a['href']
        CompanyName=soup.find('div',{'class':'base-info'}).text
        img=soup.find('a',{'class':'box-img'})['href']
        Title=soup.find('h1',{'class':'d-title'}).text
        brand=soup.find_all('td',{'class':'de-value'})[0].text
        prices1=soup.find_all('div',{'class':'d-content'})[2]['data-price']
        prices=soup.find_all('span',{'class':'value'})
        sales=soup.find('div',{'class':'mod-detail-dealrecord mod-info'})['data-mod-config']
        sales=eval(sales)
        ti=re.findall(r'\d+',sales['title'])[0]
        name=soup.find('a',{'class':'link name'}).text
        lowprice=prices[0].text
        highprice=prices[1].text
        print(lowprice)
        print(highprice)
        print(CompanyName)
        print(Title)
        print(title.strip('- 阿里巴巴'))
        print(Area.get('content'))
        print(shopurl)
        print(img)
        print(brand)
        print(name)
        print(ti)
    def get_json(self):
        url='https://detail.1688.com/offer/525467996469.html'
        response=requests.get(url,headers=self.header)
        soup=BeautifulSoup(response.text,'lxml')
        for i in soup.find_all('script',{'type':'text/javascript'}):
            print(i)
        shopuid=soup.find('meta',{'property':'og:product:nick'})
        print(shopuid)
        #pattern=re.compile(r'\{.*\}')
        #n=re.findall(pattern, m)[1]
        #n=json.loads(n)
        #print(type(n))
       # for k,v in n.items():
          #  print(re.findall(r'\d.*',k)[0])
           # print(v['price'])

        #for i in soup.find_all('script',{'type':'text/javascript'}):
           # print('>>>>>>>>>>>>>>')
         #   print(i.text)
        
      #  a=soup.find_all('script',type="text/javascript")
       # j=re.match(r'\{.*+\}', a)
       # print(j)
    def Get_Error(self):
        url='https://shop8579455191245.1688.com/'
        response=requests.get(url,headers=self.header)
        soup=BeautifulSoup(response.text,'lxml')
        #print(soup)

        #sales=soup.find('div',{'class':'mod-detail-dealrecord mod-info'})['data-mod-config']
        #print(sales)
    def Get_er(self):
        url='https://s.1688.com/selloffer/offer_search.htm?keywords=%B4%B4%BA%E3&n=y&spm=a260k.635.3262836.d102&beginPage=1&offset=4&filterP4pIds=42313419257,44717538257,44760313364'
        response=requests.get(url,headers=self.header)
        soup=BeautifulSoup(response.text,'lxml')
       # print(soup.find('div',{'class':'base-info'}).a['href'])
       # print(soup.find('li',{'class':'index-page'}).a['href'])
        li=soup.find_all('a',{'data-spm':'of0'})
        lim=soup.find_all('a',{'data-spm':'of0'})[0]
        count=0
        for i in li[3::]:
            print(count)
            print(i['href'])
            print(i['title'])
            count=count+1
        #count=0
      # m=soup.find_all('script',{'type':'text/javascript'})[7].text
     #   print(m)
      #  s=soup.find_all('input',{'id':'memberId'})[0]['value'] 
       # print(s)
        #print(soup)
       # m=soup.find_all('td',{'class':'de-value'})
       # print(s)
        
if __name__ == '__main__':
    a=alibb()
   # a.Get_Url_list()
   # a.Get_url_lis()
   #a.Get_Goods_inf()
    #a.get_json()
   # a.Get_Error()
    a.Get_er()