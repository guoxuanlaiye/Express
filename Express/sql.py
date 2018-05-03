import pymysql
from pymysql import DatabaseError

conn = pymysql.connect("localhost", "root", "", "test", use_unicode=True, charset="utf8")
cursor = conn.cursor()

class Sql(object):

    @classmethod
    def insert_expressPoint(cls, ex_comp_name, ex_comp_url_suffix, ex_pro_name, ex_pro_url_suffix, ex_city_name, ex_city_url_suffix, ex_county_name, ex_county_url):
        sql = "insert into express_points(company_name, company_url, province, province_url, city, city_url, county_name, county_url) values ('%s','%s','%s','%s','%s','%s','%s','%s')" % (ex_comp_name, ex_comp_url_suffix, ex_pro_name, ex_pro_url_suffix, ex_city_name, ex_city_url_suffix, ex_county_name, ex_county_url)
        try:
            cursor.execute(sql)
            conn.commit()
        except DatabaseError as dbError:
            print("---- insert_expressPoint %s" % dbError)
            conn.rollback()

