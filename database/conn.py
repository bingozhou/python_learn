import pymysql

# 数据库连接对象

"""
介绍一下connection的参数

host mysql服务器地址
port 数字类型 端口
user 用户名
passwd 密码
db 数据库名称
charset 连接编码，需要显式指明编码方式 比如  utf8

"""

conn = pymysql.connect(host='127.0.0.1',port=3306,user='bingo',passwd='bingo',db='test',charset='utf8')

cursor = conn.cursor()

print(conn)

print(cursor)

cursor.close()

conn.close()