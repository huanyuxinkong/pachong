# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PafengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    tithref = scrapy.Field()


    liti = scrapy.Field()
    conliti = scrapy.Field()
    author = scrapy.Field()  # 作者
    con = scrapy.Field()  # 文章内容
    day = scrapy.Field()


