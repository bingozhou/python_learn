"""
更新数据库insert/update/delete

不同于select操作，这三个操作修改了数据库内容，所以需要commit()，否则数据库没有做相应的更改，但是也不会报错。

按照一般的思路，一般是以下套路：

关闭自动commit:conn.autocommit(False)
出现：conn.rowback()回滚
未出现：conn.commit()

"""
import pymysql

conn = pymysql.Connect(host='0.0.0.0', port=3306, user='bingo', passwd='bingo', db='test', charset='utf8')
conn.autocommit(False)
cursor = conn.cursor()

sqlInsert = "INSERT INTO user(userid,username) VALUES('6','name6')"
sqlUpdate = "UPDATE user SET username='name41' WHERE userid='4'"
sqlDelete = "DELETE FROM user WHERE userid='1'"
try:
    cursor.execute(sqlInsert)
    print(cursor.rowcount)
    cursor.execute(sqlUpdate)
    print(cursor.rowcount)
    cursor.execute(sqlDelete)
    print(cursor.rowcount)

    conn.commit()
except Exception as e:
    print("Reason:", e)
    conn.rollback()

cursor.close()
conn.close()
