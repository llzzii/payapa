import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast2'  # 爬虫名
    allowed_domains = ['itcast.cn']  # 允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']  # 最开始请求的url地址

    def parse(self, response):
        # 处理start_urls地址对应的响应
        res1 = response.xpath('//div[@class="maincon"]//h2/text()').extract()
        print(res1)
