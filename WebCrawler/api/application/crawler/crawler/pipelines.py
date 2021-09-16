# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
from itemadapter import ItemAdapter
from application.models import MongoDB

logger = logging.getLogger(__name__)


class CrawlerPipeline:
    collection_name = 'scrapy_items'

    def __init__(self, obj):
        self.obj = obj

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            obj=crawler.spider.obj
        )

    def process_item(self, item, spider):
        # self.exporter.export_item(item)
        logger.debug("DB添加数据")
        MongoDB[spider.obj['name']+"_data"].insert(dict(item))
        return item
