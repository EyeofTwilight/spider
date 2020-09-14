# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    # 允许下载的域名
    allowed_domains = ['movie.douban.com']
    # 配置下载的首地址
    start_urls = ['http://movie.douban.com/']

    # 下载完成之后的解析方法
    def parse(self, response):
        # 首先格式化成标准html
        html = etree.HTML(response.text)
        # 获取当前页面豆瓣所有电影
        hot_moves = html.xpath("//div[@class='screening-bd']/ul/li")
        moves = []
        # 提取每一个电影的数据
        for move in hot_moves:
            item = DoubanItem()
            # 为字段赋值
            item['title'] = move.xpath(".//li[@class='title']/a/text()")
            item['rating'] = move.xpath(".//li[@class='rating']/span/text()")
            # 每次只返回一条数据,避免一次返回的数据量太大
            yield item
        try:
            # 获取下一页超链接的值
            next_page = html.xpath("//span[@class='next']/a/@href")[0]
            # 手动发送请求,让爬虫去解析下一页的数据, callback自己递归
            yield scrapy.Request("http://movie.douban.com/top250" + next_page, self.parse)
        except:
            print("下载完毕......")
