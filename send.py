import urllib2
import urllib
req = urllib2.urlopen(
url= 'https://sc.ftqq.com/SCU10361T0a2416cf6a6ca09da852bf223a588c2f59776131cef7d.send',
data= urllib.urlencode('text=PYTHON&desp=主人，这是发送信息测试~~ ')
)
