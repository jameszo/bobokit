# -*- coding: utf-8 -*-
import scrapy
from web_spider.items import PoetrySpiderItem

import re
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class PoetrySpider(CrawlSpider):
    name = 'PoetrySpider'
    allowed_domains = ['gushiwen.org']
    start_urls = ['http://so.gushiwen.org/guwen', 'http://so.gushiwen.org']

    def parse(self, response):
        if(response.url.find('view_') >= 0):
            idx_num = re.findall(r"_(.+?).aspx", response.url)
            if(idx_num != None and len(idx_num) > 0):
                item = PoetrySpiderItem()
                item['poetry_title'] = response.xpath('//h1/text()').extract()
                item['poetry_type'] = 'gushici'
                person = response.xpath('//p[@class="source"]/a/text()').extract()
                if(person != None and len(person) > 1):
                    item['poetry_author'] = person[1]
                    item['poetry_time'] = person[0]
                elif(person != None and len(person) == 1):
                    item['poetry_author'] = person[0]
                    item['poetry_time'] = ''
                else:
                    item['poetry_author'] = ''
                    item['poetry_time'] = ''
                item['poetry_content'] = response.xpath('//div[@id="contson%s"]' % idx_num[0] + '/*/text()').extract()
                if (item['poetry_content'] == [] or item['poetry_content'] == '' or item['poetry_content'] == None):
                    item['poetry_content'] = response.xpath('//div[@id="contson%s"]' % idx_num[0] + '/text()').extract()
                if(item['poetry_content'] != None and item['poetry_content'] != [] and item['poetry_content'] != ''):
                    yield item
        elif(response.url.find('bookv_') >= 0):
            item = PoetrySpiderItem()
            item['poetry_title'] = response.xpath('//h1/text()').extract()
            item['poetry_type'] = 'guwen'
            person = response.xpath('//p[@class="source"]/a/text()').extract()
            if(person != None and len(person) > 1):
                item['poetry_author'] = person[1]
                item['poetry_time'] = person[0]
            elif(person != None and len(person) == 1):
                item['poetry_author'] = person[0]
                item['poetry_time'] = ''
            else:
                item['poetry_author'] = ''
                item['poetry_time'] = ''
            item['poetry_content'] = response.xpath('//div[@class="contson"]/*/text()').extract()
            if(item['poetry_content'] != None and item['poetry_content'] != [] and item['poetry_content'] != ''):
                yield item

        for url in response.xpath('//a/@href').extract():
            if url.startswith('http'):
                yield scrapy.Request(url, callback=self.parse, dont_filter=False)
            else:
                url = 'http://so.gushiwen.org'+url
                yield scrapy.Request(url, callback=self.parse, dont_filter=False)

