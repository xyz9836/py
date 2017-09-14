import httplib
url = "http://sc.ftqq.com/SCU10361T0a2416cf6a6ca09da852bf223a588c2f59776131cef7d.send?text=PYTHON&desp=getting test1~~"
conn = httplib.HTTPConnection("http://sc.ftqq.com")
conn.request(method="GET",url=url)
response = conn.getresponse()
res= response.read()
print res




  #File "get.py", line 2
#SyntaxError: Non-ASCII character '\xe4' in file get.py on line 2, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details


Traceback (most recent call last):
  File "get.py", line 3, in <module>
    conn = httplib.HTTPConnection("http://sc.ftqq.com")
  File "/usr/lib/python2.7/httplib.py", line 739, in __init__
    self._set_hostport(host, port)
  File "/usr/lib/python2.7/httplib.py", line 767, in _set_hostport
    raise InvalidURL("nonnumeric port: '%s'" % host[i+1:])
httplib.InvalidURL: nonnumeric port: '//sc.ftqq.com'
