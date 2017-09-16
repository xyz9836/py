# -*- coding: utf-8 -*-
import urllib
import urllib2
import requests

def send_offline():
    test_data = {'text':'监工报告','desp':'有设备状态异常'}
    test_data_urlencode = urllib.urlencode(test_data)
    requrl = "https://sc.ftqq.com/SCU10361T0a2416cf6a6ca09da852bf223a588c2f59776131cef7d.send"
    req = urllib2.Request(url = requrl,data =test_data_urlencode)

    print req
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res

'''
def send_ipchange():
    test_data = {'text':'WARRING','desp':'IP has been changed'}
    test_data_urlencode = urllib.urlencode(test_data)
    requrl = "https://sc.ftqq.com/SCU10361T0a2416cf6a6ca09da852bf223a588c2f59776131cef7d.send"
    req = urllib2.Request(url = requrl,data =test_data_urlencode)

    print req
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res


def send_restart():
    result = requests.post('https://openapi.daocloud.io/v1/apps/28908fa3-d32e-4cc6-aecf-3ef906525b35/actions/restart',
      headers={"Authorization": "ns7i54n3iuln78dtot936b4sjknjaoxr93po8hsw"})
    print(result.json())

'''



'''
import urllib
import urllib2
test_data = {'text':'PYTHON','desp':'主人，这是发送信息测试~~'}
test_data_urlencode = urllib.urlencode(test_data)
requrl = "https://sc.ftqq.com/SCU10361T0a2416cf6a6ca09da852bf223a588c2f59776131cef7d.send"
req = urllib2.Request(url = requrl,data =test_data_urlencode)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res
'''
