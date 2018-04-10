"""
python 发送HTTP请求 post json 格式

"""

import httplib
import json

test_data = {'pictureName': '1.jpg'}

requrl = "http://10.1.24.88:8090/api/load_pic"
headerdata = {"Content-type": "application/json;charset=utf-8"}

conn = httplib.HTTPConnection("10.1.24.88", 8090)

conn.request('POST', requrl, json.dumps(test_data), headerdata)

response = conn.getresponse()

res = response.read()

print res