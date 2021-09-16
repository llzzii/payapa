import scrapy


class BkySpider(scrapy.Spider):
    name = 'bky'
    allowed_domains = ['www.cnblogs.com']
    start_urls = ['http://https://www.cnblogs.com/']

    def parse(self, response):
        pass
