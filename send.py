import urllib2
import urllib
req = urllib2.urlopen(
url= 'https://sc.ftqq.com/SCU10361T0a2416cf6a6ca09da852bf223a588c2f59776131cef7d.send',
data= urllib.urlencode('text=PYTHON&desp=sending tese1~~ ')
)


#  File "send2.py", line 3
#SyntaxError: Non-ASCII character '\xe4' in file send2.py on line 3, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details
