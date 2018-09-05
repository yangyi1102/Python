'''
Created on 2018年8月6日

@author: yangyi
'''
#coding=utf-8
import requests
from bs4 import BeautifulSoup
import pymysql
import re
class Tongji(object):
    def __init__(self):
        self.header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36',
            'Referer': 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/11.html',
            'Host': 'www.stats.gov.cn',
            }
    def PHtmlDown(self,url):                                     #省
        html=requests.get(url,headers=self.header)
        html.encoding='gb2312'
        soup=BeautifulSoup(html.text,'lxml')
        href=[]
        provice=[]
        for i in soup.find_all('a'):
            href.append(i['href'])
            provice.append(i.text)
        href.pop()
        provice.pop()
        return href,provice
    def SHtmlDownLoad(self,lis,prolis):
        j=0
        count1=0    
        for i in lis:   
            src=[]
            city=[]
            pattern = re.findall(r'\d+',i)
            s=pattern[0]+'0000'
            self.Save(j,s,prolis[count1],'0','1','省')
            count1=count1+1
            url='http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/'+i
            html=requests.get(url,headers=self.header)
            html.encoding='gb2312'
            soup=BeautifulSoup(html.text,'lxml')
            for i in soup.find_all('a'):
                src.append(i['href'])
                city.append(i.text)
            src.pop()
            city.pop()
            src1 = list(set(src))
            src1.sort(key=src.index)
            list1=city[::2]
            list2=city[1::2]
            print(list1,list2)
            count=0
            for i in list1:
                self.str=i[0:6]
                print('zhegeshi:'+self.str)
                print(j,self.str,list2[count],'1','2','市',src[count]) 
                self.Save(j,self.str,list2[count],'1','2','市')
                self.QhtmlDownLoad(src1[count],j)
                count=count+1
            j=j+1
    def QhtmlDownLoad(self,li,j):
            town=[] 
            url='http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/'+li
            html=requests.get(url,headers=self.header)
            html.encoding='gb2312'
            soup=BeautifulSoup(html.text,'lxml')
            for i in soup.find_all('a'):
                town.append(i.text)
                print(i.text)
            town.pop()
            list1=town[::2]
            list2=town[1::2]
            print('ok')
            print(list1,list2)
            count=0
            for i in list1:
                str0=list1[count][0:6]
                str1=list2[count][-1]
                print(str0,str1)
                self.Save(j,str0,list2[count],self.str,'3',str1)
                count=count+1      
    def Save(self,domainld,areano,areaname,parentno,arealevel,typename):
        print(domainld,areano,areaname,parentno,arealevel,typename)
        db=pymysql.connect(host='bsswaiwang.mysql.rds.aliyuncs.com',port=3306,user= 'sp_data_group',password = '4ydEe7EfrzEH',database='brand')
        cur=db.cursor()
        sql='INSERT INTO Administrative_code(domainld,areano,areaname,parentno,arealevel,typename) VALUES(%s,%s,%s,%s,%s,%s);'       
        cur.execute(sql, [domainld,areano,areaname,parentno,arealevel,typename])
        db.commit()
        print('提交成功!')
if __name__ == '__main__':
    t=Tongji()
    lis,lis1=t.PHtmlDown('http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html')
#     count=0
#     for i in lis:
#         pattern = re.findall(r'\d+',i)
#         str=pattern[0]+'0000'
#         print(str)
#         print(lis1[count])
#         count=count+1
    t.SHtmlDownLoad(lis,lis1)