# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 23:53:36 2017

@author: 17549
"""

import itchat
from echarts import Echart,Legend,Pie
itchat.login()
friends=itchat.get_friends(update=True)
male=female=other=0
for i in friends[1:]:
    sex=i["Sex"]
    if sex==1:
        male+=1             
    elif sex==2:
        female+1
    else:
        other+=1
total=len(friends[1:])
chart=Echart(u'%s的微信好友性别比列' % (friends[0]['NickName']),'from WeChat')
chart.use(Pie('WeChat',
              [{'value':male,'name':u'男性 %.2f%%' % (float(male)/total*100)},
               {'value':female,'name':u'女性 %.2f%%' % (float(female)/total*100)},
               {'value':other,'name':u'其他 %.2f%%' % (float(other)/total*100)}]
              ))
chart.use(Legend(["male","female","other"]))
del chart.json["xAxis"]
del chart.json["yAxis"]
chart.plot()
