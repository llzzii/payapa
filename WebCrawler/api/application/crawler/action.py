
# from app import crawl_for_quotes
from flask_restful import Resource
from flask import Flask, jsonify, request
import json
from multiprocessing import Process
import time
from scrapy import cmdline
import os
from application.crawler.crawler import spiders


class ActionApi(Resource):
    def get(self):
        # crawl_for_quotes()
        pId = request.args.get("pId")
        old_path = os.getcwd()
        # 在进程中启动爬虫

        crawl_threads = Process(
            target=start_crawl, args=(pId,))
        crawl_threads.start()
        os.chdir(old_path)

        return {'code': 10000, 'msg': 'add user success', 'data': 'json_data'}


def start_crawl(spider_arg):
    b = 'scrapy crawl project_crawler -a pId='
    c = b + spider_arg
    os.chdir((os.path.dirname(spiders.__file__)))
    cmdline.execute(c.split())
