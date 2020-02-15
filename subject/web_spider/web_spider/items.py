# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PoetrySpiderItem(scrapy.Item):
    poetry_title = scrapy.Field()
    poetry_type = scrapy.Field()
    poetry_author = scrapy.Field()
    poetry_time = scrapy.Field()
    poetry_content = scrapy.Field()
