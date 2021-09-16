from pymongo import MongoClient

MC = MongoClient('127.0.0.1', 27017)
MongoDB = MC['payapa']  # 创建数据库（内存中）
