# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class ExpressCompanyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # ex_comp_name = scrapy.Field()
    # ex_comp_url_suffix = scrapy.Field()
    # ex_pro_name = scrapy.Field()
    # ex_pro_url_suffix = scrapy.Field()
    # ex_city_name = scrapy.Field()
    # ex_city_url_suffix = scrapy.Field()

class ExpressPointItem(scrapy.Item):
    ex_comp_name = scrapy.Field()
    ex_comp_url_suffix = scrapy.Field()
    ex_pro_name = scrapy.Field()
    ex_pro_url_suffix = scrapy.Field()
    ex_city_name = scrapy.Field()
    ex_city_url_suffix = scrapy.Field()
    ex_county_name = scrapy.Field()
    ex_county_url = scrapy.Field()


