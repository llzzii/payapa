

import pymysql


class JuejinDao:
    def __init__(self):
        pass

    def connection(self):
        self.db = pymysql.connect(
            host="127.0.0.1",
            user="root",
            passwd="123456",
            db="payapa",
            charset="utf8mb4",
            # cursorclass=pymysql.cursors.DictCursor
        )
        return self.db.cursor()

    def findUsers(self):
        sql = "select userName from juejin"
        cursor = self.connection()
        result = cursor.execute(sql)
        self.db.commit()
        return cursor.fetchall()
        pass

    def findTags(self):
        sql = "select tags from juejin"
        cursor = self.connection()
        result = cursor.execute(sql)
        self.db.commit()
        return cursor.fetchall()
        pass
