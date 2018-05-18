# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
import json


# 微博内容
class WeiBoWBSpider(scrapy.Spider):
    name = 'weibo_spider'
    allowed_domains = ['weibo.cn']

    def start_requests(self):
        url = 'https://m.weibo.cn/api/container/getIndex?display=0&retcode=6102&containerid=1076035498972025'
        yield Request(url, callback=self.parse)

    def parse(self, response):
        print('hah')
        content = json.loads(response.body.decode('utf-8'))
        print(content)
        infos = content['data']['cards']
        print(infos)
        for info in infos:
            text = info['mblog']['text']
            print(text)

