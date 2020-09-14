# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 此类是模型层,主要是对有价值数据的封装(类似java实体),然后再写入数据库
class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # 即为类添加字段
    # name = scrapy.Field()
    title = rating = scrapy.Field()
