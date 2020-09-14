# -*- coding: utf-8 -*-
import scrapy
from lxml import etree


class TianmaoSpiderSpider(scrapy.Spider):
    """
        爬取天猫物品数据
    """

    name = 'tianmao_spider'
    allowed_domains = ['list.tmall.com']
    start_urls = [
        'https://list.tmall.com/search_product.htm?q=%CA%D6%BB%FA&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton']

    def parse(self, response):
        html = etree.HTML(response.text)
        product_list = html.xpath("//div[@class='product  ']/div[@class='product-iWrap']")
        for product in product_list:
            div = product.xpath(".//div")
            price = product.xpath(".//p[@class='productPrice']/em/text()")
            title = product.xpath(".//div[@class='productTitle productTitle-spu']/a/text()")
            if len(title) < 1:
                title = product.xpath(".//div[@class='productTitle ']/a/text()")
            if len(price) > 0:
                print("".join(price))
            print("".join(title))
            print()
