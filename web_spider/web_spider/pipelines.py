# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class PoetrySpiderPipeline(object):
    def process_item(self, item, spider):
        path = '/Volumes/iserv-data/data/'
        title = item['poetry_title']
        name = ''
        if(isinstance(title, list) and len(title) > 0):
            name = title[0].strip()
        elif(type(title) == type('')):
            name = title.strip()
        else:
            name = str(time.time())
        type = item['poetry_type']
        f = open(path + type + '/' + name, 'w+')
        line = json.dumps(dict(item))
        f.write(line.decode("unicode_escape"))
        f.flush()
        f.close()
        return item
