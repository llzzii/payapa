
from itemadapter import ItemAdapter
import json
import pymysql


class JuejinPipeline:
    def process_item(self, item, spider):
        # 将item里的数据拿出来
        categoryName = str(item["categoryName"])
        title = str(item["title"])
        tags = str(item["tags"])
        userName = str(item["userName"])
        briefContent = str(item["briefContent"])
        # 和本地的mysql数据库建立连接
        db = pymysql.connect(
            host="127.0.0.1",
            user="root",
            passwd="123456",
            db="payapa",
            charset="utf8mb4",
            # cursorclass=pymysql.cursors.DictCursor
        )
        try:
            # 使用cursor()方法获取操作游标
            cursor = db.cursor()
            # SQL 插入语句
            # sql = "INSERT INTO juejin(categoryName, title, tags, userName, briefContent) \
            #       VALUES (%s,%s,%s,%s,%s)".format(categoryName, title, tags, userName, briefContent)
            sql = "INSERT INTO juejin(categoryName, title, tags, userName, briefContent)  VALUES (%s,%s,%s,%s,%s)"
            # 执行SQL语句
            cursor.execute(sql, (categoryName, title,
                                 tags, userName, briefContent))
            # 提交修改
            db.commit()
        finally:
            # 关闭连接
            db.close()
        return item
