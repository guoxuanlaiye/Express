import scrapy
from Express.items import ExpressPointItem

class Express_spider(scrapy.Spider):
    name = 'express'
    allowed_domains = ['www.ickd.cn']
    start_urls = ['https://www.ickd.cn/outlets/']

    def parse(self, response):
        ex_companys = response.xpath('//div[@class="attrValue exps"]/ul/li')

        for ex_comp in ex_companys:

            ex_comp_name = ex_comp.xpath("a/text()").extract_first()
            ex_comp_url_suffix = ex_comp.xpath("a/@href").extract_first()

            if not (ex_comp_name == "全部快递"):
                if ex_comp_url_suffix:
                    yield scrapy.Request(url="https://www.ickd.cn/outlets/{}".format(ex_comp_url_suffix), callback=self.getProvince, meta={"ex_comp_name": ex_comp_name, "ex_comp_url_suffix": ex_comp_url_suffix})

    # 省份
    def getProvince(self, response):

        ex_com_provinces = response.xpath('//div[@class="attrs mt10"]/div[@class="attr prov"]/div[@class="attrValue"]/ul/li')
        # print(ex_com_provinces)
        for pro in ex_com_provinces:
            ex_pro_url_suffix = pro.xpath('a/@href').extract_first()
            ex_pro_name = pro.xpath('a/text()').extract_first()
            if not (ex_pro_name == "全部"):
                if ex_pro_url_suffix:
                    meta = {"ex_comp_name": response.meta["ex_comp_name"],
                            "ex_comp_url_suffix": response.meta["ex_comp_url_suffix"],
                            "ex_pro_name": ex_pro_name,
                            "ex_pro_url_suffix": ex_pro_url_suffix}
                    yield scrapy.Request(url="https://www.ickd.cn/outlets/{}".format(ex_pro_url_suffix), callback=self.getCitys, meta=meta)

    # 城市
    def getCitys(self, response):
        ex_com_citys = response.xpath('//div[@class="attrs mt10"]/div[4]/div[@class="attrValue"]/ul/li')
        for city in ex_com_citys:
            ex_city_name = city.xpath('a/text()').extract_first()
            ex_city_url_suffix = city.xpath('a/@href').extract_first()
            if not (ex_city_name == "全部"):
                if ex_city_url_suffix:
                    meta = {"ex_city_name": ex_city_name,
                            "ex_city_url_suffix": ex_city_url_suffix,
                            "ex_comp_name": response.meta["ex_comp_name"],
                            "ex_comp_url_suffix": response.meta["ex_comp_url_suffix"],
                            "ex_pro_name": response.meta["ex_pro_name"],
                            "ex_pro_url_suffix": response.meta["ex_pro_url_suffix"]}

                    yield scrapy.Request(url="https://www.ickd.cn/outlets/{}".format(ex_city_url_suffix), callback=self.getCounty, meta=meta)

    # 区县
    def getCounty(self, response):
        ex_countys = response.xpath('//div[@class="attrs mt10"]/div[5]/div[@class="attrValue"]/ul/li')
        # 如果存在区县，取出区县加入到model中

        item = ExpressPointItem()
        item["ex_city_name"] = response.meta["ex_city_name"]
        item["ex_city_url_suffix"] = response.meta["ex_city_url_suffix"]
        item["ex_comp_name"] = response.meta["ex_comp_name"]
        item["ex_comp_url_suffix"] = response.meta["ex_comp_url_suffix"]
        item["ex_pro_name"] = response.meta["ex_pro_name"]
        item["ex_pro_url_suffix"] = response.meta["ex_pro_url_suffix"]

        if len(ex_countys) > 0:
            for county in ex_countys:
                ex_county_name = county.xpath('a/text()').extract_first()
                ex_county_url = county.xpath('a/@href').extract_first()
                if not (ex_county_name == "全部"):
                    item["ex_county_name"] = ex_county_name
                    item["ex_county_url"] = ex_county_url
                    yield item
        else:
            item["ex_county_name"] = ""
            item["ex_county_url"] = ""
            yield item


    # 快递点
    def getPoint(self, response):
        ex_points = response.xpath('//div[@class="fl"]/div[@class="net-info"]')

        for point in ex_points:
            pass