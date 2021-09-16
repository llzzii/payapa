import scrapy


class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['www.csdn.net']
    start_urls = ['http://www.csdn.net/']

    def parse(self, response):
        # print(11)
        # print(response.css("span.blog-text::text").getall())
        # print(response.xpath(
        #     "//div['blog']/span['blog-text']/text()").getall())
        for quote in response.css('a.blog'):
            yield {
                'text': quote.css('span.blog-text::text').get(),
                'tag': quote.css('span.blog-title::text').get(),
                'desc': quote.css('p.desc::text').getall(),
            }
        pass
    # scrapy crawl csdn  --set FEED_URI=items.json --set FEED_FORMAT=json
