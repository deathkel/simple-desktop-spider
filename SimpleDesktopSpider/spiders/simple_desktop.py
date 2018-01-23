# -*- coding: utf-8 -*-
import scrapy
from SimpleDesktopSpider.items import Image
import re
from scrapy.exporters import JsonItemExporter


class SimpleDesktopSpider(scrapy.Spider):
    name = 'simple-desktop'
    host = 'http://simpledesktops.com'
    start_urls = ['http://simpledesktops.com/browse/1/']

    def parse(self, response):
        desktops = response.css('div.desktop')
        for object in desktops:
            image = Image()
            image['name'] = object.css('a').css('img::attr(title)').extract_first()
            thumbnail = object.css('a').css('img::attr(src)').extract_first()
            image['thumbnail'] = thumbnail
            position = re.match("http?://\S+?/\S+?\.(?:jpg|jpeg|gif|png)", thumbnail).span()
            image['original'] = thumbnail[position[0]:  position[1]]
            image['author'] = object.css('span.creator').css('a::text').extract_first()
            yield image

        next_url = response.css('a.back::attr(href)').extract_first()
        if (next_url is not None):
            yield scrapy.Request(self.host + next_url, callback=self.parse)
