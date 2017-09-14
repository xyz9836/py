import urllib
import urllib2
test_data = {'text':'PYTHON','desp':'sending tese2~~'}
test_data_urlencode = urllib.urlencode(test_data)
requrl = "https://sc.ftqq.com/SCU10361T0a2416cf6a6ca09da852bf223a588c2f59776131cef7d.send"
req = urllib2.Request(url = requrl,data =test_data_urlencode)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res


#  File "send2.py", line 3
#SyntaxError: Non-ASCII character '\xe4' in file send2.py on line 3, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details
