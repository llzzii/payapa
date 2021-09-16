
from scrapy.exporters import JsonItemExporter


class JsonExporterPipleline(object):

    # 调用scrapy提供的json export导出json文件
    def __init__(self):
        self.file = open('juejin.json', 'wb')
        self.exporter = JsonItemExporter(
            self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
