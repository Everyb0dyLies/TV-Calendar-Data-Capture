# -*- coding: utf-8 -*-

import scrapy
import re
from TV_Calendar_Data_Capture.items import TvCalendarDataCaptureItem

class DetailSpider(scrapy.spiders.Spider):
    name = "detail"
    allowed_domains = ["zimuzu.tv"]
    zmz_id = ""

    def __init__(self, zmz_id = None, *args, **kwargs):
        super(DetailSpider, self).__init__(*args, **kwargs)
        if zmz_id == None:
            pass
        else :
            self.zmz_id = zmz_id
            self.start_urls = ['http://www.zimuzu.tv/subtitle/%s' % zmz_id]

    def parse(self, response):
        subtitle = response.xpath('//div[@class="box subtitle-con"]')[0]
        title = subtitle.xpath('h2[@class="subtitle-tit"]/text()').extract()[0].encode('utf-8')
        ch_name = subtitle.xpath('ul[@class="subtitle-info"]/li[1]/text()').extract()[0].encode('utf-8')[12:]
        en_name = subtitle.xpath('ul[@class="subtitle-info"]/li[2]/text()').extract()[0].encode('utf-8')[12:]
        lang = subtitle.xpath('ul[@class="subtitle-info"]/li[3]/text()').extract()[0].encode('utf-8')[12:]
        version = subtitle.xpath('ul[@class="subtitle-info"]/li[4]/text()').extract()[0].encode('utf-8')[12:]
        format = subtitle.xpath('ul[@class="subtitle-info"]/li[5]/text()').extract()[0].encode('utf-8')[12:]
        source = subtitle.xpath('ul[@class="subtitle-info"]/li[6]/text()').extract()[0].encode('utf-8')[12:]
        release_time = subtitle.xpath('ul[@class="subtitle-info"]/li[7]/text()').extract()[0].encode('utf-8')
        if re.search(r'最后编辑：', release_time):
            release_time = re.split(r'最后编辑：', release_time)[1][0:16]
        else:
            release_time = release_time[12:28]
        file_name = subtitle.xpath('div[@class="subtitle-links tc"]/h3/a/text()').extract()[0].encode('utf-8')
        file_link = subtitle.xpath('div[@class="subtitle-links tc"]/h3/a/attribute::href').extract()[0].encode('utf-8')
        
        item = TvCalendarDataCaptureItem()
        item['zmz_id'] = self.zmz_id
        item['title'] = title
        item['ch_name'] = ch_name
        item['en_name'] = en_name
        item['lang'] = lang
        item['version'] = version
        item['format'] = format
        item['source'] = source
        item['release_time'] = release_time
        item['file_name'] = file_name
        item['file_link'] = file_link
        yield item

