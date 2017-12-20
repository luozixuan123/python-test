# -*- coding: utf-8 -*-


import scrapy
from scrapy.spider import Spider


class ScrapyTest(Spider):
    name = "test"

    def __init__(self, name=None, **kwargs):
        Spider.__init__(self, name, **kwargs)

    def start_requests(self):
        a = 'http://www.cdht.gov.cn:80/zwgkjddt/121734.jhtml'

        yield scrapy.Request(a)

    def parse(self, response):
        b = response.body
        t1 = "".join(response.xpath("//h1//text()").extract()).strip()

