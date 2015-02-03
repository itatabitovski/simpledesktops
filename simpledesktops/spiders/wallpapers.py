# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from simpledesktops.items import SimpledesktopsItem


class WallpapersSpider(CrawlSpider):
    name = 'wallpapers'
    allowed_domains = ['simpledesktops.com']
    start_urls = ['http://simpledesktops.com/browse/']

    rules = (
        Rule(LinkExtractor(allow=r'browse/desktops/20[0-9]{2}/(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)/[0-9]{2}'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'browse/\d\/$'), follow=True),
    )

    def parse_item(self, response):
        i = SimpledesktopsItem()
        i['image_urls'] = ['http://{0}/{1}'.format(self.allowed_domains[0], response.xpath('//div[@class="desktop"]/a/@href').extract()[0])]
        return i
