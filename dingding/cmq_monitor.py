#coding=utf-8
import logging

from cmq.account import Account
from cmq.queue import QueueMeta
from cmq.cmq_exception import CMQExceptionBase
import time
import urllib2
import json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def send_msg(msg):

	url = 'https://oapi.dingtalk.com/robot/send?access_token=your_token'

	#msg = 'this is message from bingo'

	data = {
	"msgtype": "text",
	"text": {"content": msg},
	"at": {"isAtAll": True}
	}


	headers = {'Content-Type': 'application/json;charset=utf-8'}
	request = urllib2.Request(url=url, headers=headers, data=json.dumps(data))
	response = urllib2.urlopen(request)



secretId = 'your id'
secretKey = 'your key'
endpoint = 'http://cmq-queue-region.api.tencentyun.com'


my_account = Account(endpoint, secretId, secretKey, debug=True)

my_account.set_log_level(logging.DEBUG)
#queue_name = sys.argv[1] if len(sys.argv) > 1 else "MySampleQueue"

#print dir(my_account)

total_queues =  my_account.list_queue()[0]

#print 'total_queues: %d' % total_queues

queues_list = my_account.list_queue(limit=total_queues)[1]

#print 'queues_list: %s' % queues_list

i = 0
queue_name = []

while i < len(queues_list):

	queue_name.append(queues_list[i]['queueName'])
        i+=1

#print queue_name[0]

for i in range(len(queue_name)):
	my_queue = my_account.get_queue(queue_name[i])
 #       print dir(my_queue)
        queue_meta = my_queue.get_attributes()
        print queue_name[i],queue_meta.activeMsgNum,queue_meta.inactiveMsgNum
        if (queue_meta.activeMsgNum >= 500 or queue_meta.inactiveMsgNum >= 1000 ):
		msg = "生产环境队列阻塞告警:\n队列名称:%s\n可见消息数量:%d\n不可见消息数量:%d\n" % (queue_name[i],queue_meta.activeMsgNum,queue_meta.inactiveMsgNum)
                send_msg(msg)
        i+=1
        time.sleep(1)

print "上一次运行时间：%s" % time.ctime()
