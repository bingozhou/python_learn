import os
import sys
import pymysql

"""

模拟银行转账，从源帐号转账到目标帐号，对源帐号和目标帐号有效性进行检查
源帐号需要减掉金额
目标帐号需要增加金额

用法：
python bank.py 1 2 5
从帐号1转5块钱给帐号2

"""


class transferMoney(object):
    def __init__(self, conn):
        self.conn = conn
# 转账
    def transfer(self, sourceID, targetID, money):
        #   其他函数中若是有错会抛出异常而被检测到。
        try:
            self.checkIdAvailable(sourceID)
            self.checkIdAvailable(targetID)
            self.ifEnoughMoney(sourceID, money)
            self.reduceMoney(sourceID, money)
            self.addMoney(targetID, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
# 检查帐号是否有效
    def checkIdAvailable(self, ID):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where id = %d" % ID  # select语句判断可以用len(rs)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:  # 数据库类思想的报错模式，检查操作对数据库的影响条目。没有达到目标，抛出异常
                raise Exception("账号 %d 不存在" % ID)
        finally:
            cursor.close()
# 检查源帐号是否有足够的钱
    def ifEnoughMoney(self, ID, money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where id = %d and money>=%d" % (ID, money)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号 %d 不存在 %d Yuan" % (ID, money))
        finally:
            cursor.close()
# 减去源帐号的钱
    def reduceMoney(self, ID, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money = money-%d where id=%d" % (money, ID)
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("失败减钱")
        finally:
            cursor.close()
# 增加目标帐号的钱
    def addMoney(self, ID, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money = money+%d where id=%d" % (money, ID)
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("失败加款")
        finally:
            cursor.close()


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        sourceID = int(sys.argv[1])
        targetID = int(sys.argv[2])
        money = int(sys.argv[3])

        conn = pymysql.Connect(host='192.168.x.x', port=3306, user='xxx', passwd='xxx', db='test', charset='utf8')
        trMoney = transferMoney(conn)

        try:
            trMoney.transfer(sourceID, targetID, money)
        except  Exception as e:
            print("出现问题" + str(e))
        finally:
            conn.close()
