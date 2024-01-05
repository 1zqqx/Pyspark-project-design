# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QdfictionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # book_link = scrapy.Field()  # 书连接
    # book_cover = scrapy.Field()  # 封面连接
    book_name = scrapy.Field()  # 书名
    book_author = scrapy.Field()  # 作者
    book_first_partition = scrapy.Field()  # 一级分区
    book_second_partition = scrapy.Field()  # 二级分区
    book_status = scrapy.Field()  # 连载/完结
    book_intro = scrapy.Field()  # 书介绍
    # book_wordage = scrapy.Field()  # 书字数
    date_list = scrapy.Field()  # 上榜年月份
    pass
