
import logging
from scrapy.exporters import JsonItemExporter

logger = logging.getLogger(__name__)


class JsonExporterPipleline(object):

    # 调用scrapy提供的json export导出json文件
    def __init__(self, obj):
        self.file = open(obj['name']+'.json', 'wb')
        self.exporter = JsonItemExporter(
            self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            obj=crawler.spider.obj
        )

    def close_spider(self, spider):
        logger.debug("爬虫结束")
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
