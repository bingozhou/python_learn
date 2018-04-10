"""
数据库游标对象

Function	        描述
execute(op[,args])	执行一个数据库查询和命令
fetchone()	        取得结果集下一行
fetchmany(size)	    取得结果集size行
fetchall()	        取得结果集剩下所有行
rowcount	        最近一次execute返回数据的行数或影响行数
close()	            关闭cursor

"""

import pymysql

conn = pymysql.Connect(host='127.0.0.1',port=3306,user='bingo',passwd='bingo',db='test',charset='utf8')
cursor = conn.cursor()
sql = "select * from stu"
cursor.execute(sql)
print("cursor.excute:",cursor.rowcount)   #  输出受影响的行数

rs = cursor.fetchone()    # 游标输出一行记录
print("rs:",rs)

for each in cursor.fetchmany(2):   #  游标输出接下来的两行的记录
    print(each)
print()
for each in cursor.fetchall():   # 游标输出剩下的所有的记录
    print(each)
