import urllib2
import json

data = {
    'a': 123,
    'b': 456
}
headers = {'Content-Type': 'application/json;charset=utf-8'}
request = urllib2.Request(url='url', headers=headers, data=json.dumps(data))
response = urllib2.urlopen(request)