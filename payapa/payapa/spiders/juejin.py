import json
from payapa.juejinItem import JuejinItem
import scrapy
from scrapy import Spider, Request


class JuejinSpider(scrapy.Spider):
    name = 'juejin'
    # allowed_domains = ['juejin.com']
    start_urls = [
        'https://api.juejin.cn/']
    list_url = 'https://api.juejin.cn/recommend_api/v1/article/recommend_cate_feed'
    alllist_url = 'https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed'
    # 伪装成浏览器
    headers = {
        "X-Agent": "Juejin/Web",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Content-Type": "application/json",
    }

    def start_requests(self):
        body = {"id_type": 2, "sort_type": 200,
                "cate_id": "6809637767543259144", "cursor": "0", "limit": 10}
        allbody = {"id_type": 2, "client_type": 2608,
                   "sort_type": 300, "cursor": "0", "limit": 200}
        yield scrapy.Request(url=self.list_url, callback=self.parse_httpbin, method="POST", headers=self.headers,  body=json.dumps(body), errback=self.errback_httpbin)
        # yield scrapy.Request(url=self.alllist_url, callback=self.parse_httpbin, method="POST", headers=self.headers,  body=json.dumps(allbody), errback=self.errback_httpbin)
        # return super().start_requests()

    def parse_httpbin(self, response):
        print(123)
        result = json.loads(response.text)
        if result.get("err_msg") == 'success':
            data = result.get("data")
            fileds = []
            if len(data) > 0:
                for item in data:
                    filed = JuejinItem()
                    filed["title"] = item.get("article_info").get("title")
                    filed["categoryName"] = item.get(
                        "category").get("category_name")
                    # filed["tags"] = item.get("tags").get("tag_name")
                    tagValue = []
                    for tag in item.get("tags"):
                        tagValue.append(tag.get("tag_name"))
                    filed["tags"] = json.dumps(tagValue, ensure_ascii=False)
                    filed["briefContent"] = item.get(
                        "article_info").get("brief_content")
                    filed["userName"] = item.get(
                        "author_user_info").get("user_name")
                    fileds.append(filed)
                    yield filed
        # 翻页
        if result.get("has_more"):
            body = {"id_type": 2, "sort_type": 200,
                    "cate_id": "6809637767543259144", "cursor": result.get("cursor"), "limit": 20000}
            # 爬每一页
            yield scrapy.Request(url=self.list_url, callback=self.parse_httpbin, method="POST", headers=self.headers,  body=json.dumps(body), errback=self.errback_httpbin)

        # self.logger.info(
        #     'Got successful response from {}'.format(response.url))
        # do something useful here...

    def errback_httpbin(self, failure):
        print(11123)
        self.logger.info(repr(failure))
