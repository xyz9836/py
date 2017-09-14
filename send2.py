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
