# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompactItem(scrapy.Item):
    city=scrapy.Field()
    kms=scrapy.Field()
    fuel=scrapy.Field()
    model=scrapy.Field()
    transm=scrapy.Field()
    price=scrapy.Field()
    yom=scrapy.Field()
    url=scrapy.Field()
    owner=scrapy.Field()
    color=scrapy.Field()
