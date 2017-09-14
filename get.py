import httplib
url = "http://sc.ftqq.com/SCU10361T0a2416cf6a6ca09da852bf223a588c2f59776131cef7d.send?text=PYTHON&desp=主人，这是发送信息测试~~"
conn = httplib.HTTPConnection("http://sc.ftqq.com")
conn.request(method="GET",url=url)
response = conn.getresponse()
res= response.read()
print res
