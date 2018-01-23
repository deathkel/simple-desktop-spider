# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SimpledesktopspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Image(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()
    thumbnail = scrapy.Field()
    original = scrapy.Field()
    pass
