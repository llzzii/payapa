import logging
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
from flask.json import jsonify
from application.common.common import data_conversion
import scrapy
import json
from application.models import MongoDB
from bson.objectid import ObjectId


class ProjectCrawlerSpider(scrapy.Spider):
    name = 'project_crawler'
    allowed_domains = ['']
    start_urls = ['http:///']

    def __init__(self, **kwargs):
        # 字段
        self.pId = kwargs['pId']
        obj = MongoDB['project'].find_one({'_id': ObjectId(self.pId)})
        self.obj = obj

    def start_requests(self):
        print(1223)
        header = {}
        body = {}
        param = ""
        for head in self.obj['headerList']:
            if head['keys'] != None and head['keys'] != "":
                val = data_conversion(head['val'], head['type'])
                header[head['keys']] = val

        for body_item in self.obj['bodyList']:
            if body_item['keys'] != None and body_item['keys'] != "":
                val = data_conversion(body_item['val'], body_item['type'])
                body[body_item['keys']] = val

        for param_item in self.obj['paramList']:
            if param_item['keys'] != None and param_item['keys'] != "":
                val = data_conversion(param_item['val'], param_item['type'])
                param = param + param_item['keys']+'=' + val+"&&"
        if '?' in self.obj['url']:
            self.obj['url'] = self.obj['url']+"&&"+param
        else:
            self.obj['url'] = self.obj['url']+"?"+param
        yield scrapy.Request(url=self.obj['url'], callback=self.parse_httpbin, method=self.obj['method'], headers=header,  body=json.dumps(body), errback=self.errback_httpbin)
        # yield scrapy.Request(url=self.alllist_url, callback=self.parse_httpbin, method="POST", headers=self.headers,  body=json.dumps(allbody), errback=self.errback_httpbin)
        # return super().start_requests()

    def parse_httpbin(self, response):
        result = json.loads(response.text)
        self.log("数据处理开始", logging.INFO)
        datas = result
        for dataLocation in self.obj['dataLocation']:
            result = result.get(dataLocation['val'])
        fileds = []
        if len(result) > 0:
            for item in result:
                filed = {}
                try:
                    for field_item in self.obj['fieldsList']:
                        if (len(field_item['field']) == 0 or field_item['field'][0]["val"] == ""):
                            continue
                        if field_item['type'] == "List":
                            list_arr = []
                            field_list_len = len(field_item['field'])-1
                            field_list_data = item
                            for field_list_item_val in field_item['field']:
                                if isinstance(field_list_data, list):
                                    break
                                field_list_data = field_list_data.get(
                                    field_list_item_val["val"])
                            for list_data in field_list_data:
                                list_arr.append(
                                    list_data.get(field_item['field'][field_list_len]["val"]))
                            filed[field_item['field']
                                  [field_list_len]["val"]] = list_arr
                        if field_item['type'] != "List":
                            field_len = len(field_item['field'])-1
                            field_data = item
                            for field_item_val in field_item['field']:
                                field_data = field_data.get(
                                    field_item_val["val"])
                            filed[field_item['field']
                                  [field_len]["val"]] = field_data
                    fileds.append(filed)
                    yield filed
                except Exception as e:
                    self.log("数据处理失败" +
                             ",失败原因"+str(e), logging.ERROR)
                    pass
        self.log("数据处理结束", logging.INFO)

        if datas.get("has_more"):
            body = {"id_type": 2, "sort_type": 200,
                    "cate_id": "6809637767543259144", "cursor": datas.get("cursor"), "limit": 20000}
            # 爬每一页
            # yield scrapy.Request(url=self.list_url, callback=self.parse_httpbin, method="POST", headers=self.headers,  body=json.dumps(body), errback=self.errback_httpbin)

        # self.logger.info(
        #     'Got successful response from {}'.format(response.url))
        # do something useful here...

    def errback_httpbin(self, failure):
        self.logger.info(repr(failure))
        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            MongoDB['log'].insert(
                dict({'err_status': 'HttpError', 'content': json.loads(response.text), 'crawler_name': self.obj['name']}))
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            MongoDB['log'].insert(
                dict({'err_status': 'DNSLookupError', 'content': request, 'crawler_name': self.obj['name']}))
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            MongoDB['log'].insert(
                dict({'err_status': 'TimeoutError', 'content': request, 'crawler_name': self.obj['name']}))
            self.logger.error('TimeoutError on %s', request.url)
