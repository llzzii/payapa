import scrapy
import json
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']
    list_url = 'https://www.zhihu.com/api/v4/search_v3?t=general&q=&correction=1&offset=0&limit=20&lc_idx=0&show_all_topics=0'

    # 伪装成浏览器
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
        'accept-encoding':'gzip, deflate, br',
        'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/ 537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
        'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}

    def start_requests(self):

        yield scrapy.Request(url=self.list_url, callback=self.parse_httpbin,  headers=self.headers,   errback=self.errback_httpbin,
                             )
        # return super().start_requests()

    def parse_httpbin(self, response):
        print(123)
        result = json.loads(response.text)
        print(result)
        # self.logger.info(
        #     'Got successful response from {}'.format(response.url))
        # do something useful here...

    def errback_httpbin(self, failure):
        print(11123)
        self.logger.info(repr(failure))
        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)
