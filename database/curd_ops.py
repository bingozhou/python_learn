import pymysql


class Mysql(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host='192.168.6.112',
                port=3306,
                user='bingo',
                passwd='bingo',
                db='test',
                charset='utf8'
            )
        except Exception as e:
            print(e)
        else:
            print('连接成功')
            self.cur = self.conn.cursor()

    def create_table(self):
        sql = 'CREATE TABLE testtb(id INT, name VARCHAR(10),age INT)'
        res = self.cur.execute(sql)
        print(res)

    def close(self):
        self.cur.close()
        self.conn.close()

    def add(self):  # 增
        sql = 'INSERT INTO testtb VALUES(1,"Tom",18),(2,"Jerry",16),(3,"Hank",24)'
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()
        print(res)

    def rem(self):  # 删
        sql = 'DELETE FROM testtb WHERE id=1'
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()
        print(res)

    def mod(self):  # 改
        sql = 'UPDATE testtb SET name="Tom Ding" WHERE id=2'
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()
        print(res)

    def show(self):  # 查
        sql = 'SELECT * FROM testtb'
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print(i)


if __name__ == "__main__":
    mysql = Mysql()
    mysql.create_table()
    mysql.add()
    mysql.mod()
    mysql.rem()
    mysql.show()
    mysql.close()
