# -*- coding:utf-8 -*-
import scrapy


class JuejinItem(scrapy.Item):
    categoryName = scrapy.Field()
    title = scrapy.Field()
    tags = scrapy.Field()
    userName = scrapy.Field()
    briefContent = scrapy.Field()
