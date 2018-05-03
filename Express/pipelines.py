# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .sql import Sql

class ExpressPipeline(object):
    def process_item(self, item, spider):

        Sql.insert_expressPoint(item["ex_comp_name"], item["ex_comp_url_suffix"], item["ex_pro_name"], item["ex_pro_url_suffix"], item["ex_city_name"], item["ex_city_url_suffix"], item["ex_county_name"], item["ex_county_url"])

        return item
