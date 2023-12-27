# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LjxspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    moviesImg = scrapy.Field()  # 电影封面
    moviesName = scrapy.Field()  # 电影名称
    moviesOtherName = scrapy.Field()  # 其他名称
    moviesLeadRole = scrapy.Field()  # 主演
    moviesDirector = scrapy.Field()  # 导演
    moviesTime = scrapy.Field()  # 上映时间
    moviesCountry = scrapy.Field()  # 上映国家
    moviesType = scrapy.Field()  # 电影类型
    moviesScore = scrapy.Field()  # 评分
    moviesEvaNumber = scrapy.Field()  # 评价人数
    moviesSign = scrapy.Field()  # 短评
    pass
