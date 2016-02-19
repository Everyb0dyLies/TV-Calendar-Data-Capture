# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TvCalendarDataCaptureItem(scrapy.Item):
    zmz_id = scrapy.Field() 
    title = scrapy.Field()
    ch_name = scrapy.Field()
    en_name = scrapy.Field()
    lang = scrapy.Field()
    version = scrapy.Field()
    format = scrapy.Field()
    source = scrapy.Field()
    release_time = scrapy.Field()
    file_name = scrapy.Field()
    file_link = scrapy.Field()
