import urllib
import httplib
#test_data = {'ServiceCode':'aaaa','b':'bbbbb'}
#test_data_urlencode = urllib.urlencode(test_data)
requrl = "https://openapi.daocloud.io/v1/apps/922fc621-dec5-45ce-beb1-5279d5b278d6/actions/restart"
headerdata = {"Authorization":"ns7i54n3iuln78dtot936b4sjknjaoxr93po8hsw"}
conn = httplib.HTTPConnection("https://openapi.daocloud.io")
conn.request(method="POST",url=requrl,headers = headerdata)
response = conn.getresponse()
res= response.read()
print res



#  File "send2.py", line 3
#SyntaxError: Non-ASCII character '\xe4' in file send2.py on line 3, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details
