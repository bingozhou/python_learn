import json
import urllib

url='https://api.weixin.qq.com/cgi-bin/groups/members/update?access_token='+access_token
data={'openid':str(openid),'to_groupid':str(groupid)}
data = json.dumps(data)
data=bytes(data,'utf8')
request=urllib.request.Request(url)
result=urllib.request.urlopen(request,data).read()
print(result)