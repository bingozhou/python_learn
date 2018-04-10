"""
python，并提交username和password完成登录，并返回数据
"""

# coding=utf-8

import httplib
import json
import urllib

try:
    conn = httplib.HTTPConnection("127.0.0.1", 8080)
except Exception, e:
    print e
headers = {"Content-Type": "application/json;charset=utf-8"}
param = ({"username": "me", "password": "password"})
conn.request("POST", "/api/login", json.JSONEncoder().encode(param), headers)
response = conn.getresponse()
data = response.read()
print data
conn.close()