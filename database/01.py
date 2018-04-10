import pymysql

conn = pymysql.connect(host='192.168.6.112',user='bingo',passwd='bingo',db='test',port=3306,charset='utf8')

cur = conn.cursor()

sql = "select * from stu"

cur.execute(sql)

data = cur.fetchall()

for i in range(len(data)):
    print(data[i])

conn.commit()
cur.close()
conn.close()