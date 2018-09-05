# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 14:44:44 2018

@author: 17549
"""
import requests as Re
from bs4 import BeautifulSoup
import re
import time
from bokeh.util.session_id import random
from astroid.tests.testdata.python2.data.all import name
class SuMaAPI():
    def getMobilenum(self):
            LoginInurl = Re.get("http://api.eobzz.com/httpApi.do?action=loginIn&uid=bssbss360&pwd=bssbss360")
            print(repr(LoginInurl.text))
            Login= LoginInurl.text.split('|')
            uid=Login[0]
            token=Login[1]
            Mobileurl = Re.get('http://api.eobzz.com/httpApi.do?action=getMobilenum&pid=13964&uid='+uid+'&token='+token+'&mobile=&size=1')
            Mobile=Mobileurl.text.split('|')
            print(Mobile[0])
    def getVcodeAndHoldMobilenum(self):
            time.sleep(random(0,10))
            Vcodeurl = Re.get("http://api.eobzz.com/httpApi.do?action=getVcodeAndHoldMobilenum&uid="+self.uid+"&token="+self.token+"&mobile="+self.Mobile[0])
            Vcode=Vcodeurl.text.split('|')
            print("http://api.eobzz.com/httpApi.do?action=getVcodeAndHoldMobilenum&uid="+self.uid+"&token="+self.token+"&mobile="+self.Mobile[0])            
            if (Vcode[0] == "not_receive"):                
                time.sleep(5)
                Vcode = Re.get('http://api.eobzz.com/httpApi.do?action=getVcodeAndHoldMobilenum&uid='+self.uid+'&token='+self.token+"&mobile="+self.Mobile[0])
            else:
                return Vcode[0]
    def getRecvingInfo(self):
            RecvingINfourl = Re.get('http://api.eobzz.com/httpApi.do?action=getRecvingInfo&uid='+self.uid+'&pid=1396ID&token='+self.token)
            RecvingINfourl.text
if __name__ == '__main__':
    s = SuMaAPI()
    s.getMobilenum()