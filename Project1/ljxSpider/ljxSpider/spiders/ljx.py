import scrapy

from ..items import LjxspiderItem
import re


class LjxSpider(scrapy.Spider):
    name = "ljx"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        top250_list = response.xpath("//div[@class='item']")

        for it in top250_list:
            item = LjxspiderItem()

            # 电影海报 ---------------------------------------------------------------------------------------
            item['moviesImg'] = it.xpath('div[@class="pic"]/a/img/@src').extract_first()
            # 电影名称----------------------------------------------------------------------------------------
            temp = it.xpath('div[@class="info"]/div[@class="hd"]/a/span[@class="title"]/text()'
                            ).extract()  # .replace(u'\xa0', '')
            temp = [i.replace(u'\xa0', '').replace('\\', '').replace('/', '') for i in temp]
            # temp = [re.sub("[^a-zA-Z\u4e00-\u9fa5]", '', i) for i in temp]  # 正则匹配不太好 会把所有非中文字符和字母替换掉
            item['moviesName'] = temp[0]
            item['moviesNameEn'] = temp[1] if len(temp) >= 2 else 'NULL'
            # 其他名称 ---------------------------------------------------------------------------------------
            item['moviesOtherName'] = it.xpath('div[@class="info"]/div[@class="hd"]/a/span[@class="other"]/text()'
                                               ).extract_first().replace('/', '').replace(u'\xa0', '')
            # 导演/主演 --------------------------------------------------------------------------------------
            # 上映年份 ---------------------------------------------------------------------------------------
            # 上映地区 ---------------------------------------------------------------------------------------
            temp = it.xpath('div[@class="info"]/div[@class="bd"]/p[1]/text()').extract()
            temp = [i.replace(u'\xa0', '').replace('\n', '').replace('\r', '').strip() for i in temp]
            item['moviesDirector'] = temp[0].split("主演")[0]
            item['moviesLeadRole'] = "主演" + temp[0].split("主演")[1] if len(temp[0].split("主演")) > 1 else 'NULL'
            temp_1 = temp[1].split('/')
            item['moviesTime'] = temp_1[0]
            item['moviesSector'] = temp_1[1].split(' ')
            if len(temp_1) == 3:
                item['moviesType'] = temp_1[2].split(' ')
            # 评分 -------------------------------------------------------------------------------------------
            item['moviesScore'] = it.xpath(
                'div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()'
            ).extract_first()
            # 评价人数 ----------------------------------------------------------------------------------------
            temp = it.xpath(
                './div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[4]/text()').extract_first()
            item['moviesEvaNumber'] = get_digit(temp)
            # 短评 -------------------------------------------------------------------------------------------
            item['moviesSign'] = it.xpath(
                './div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract_first()

            yield item

        next_page = response.xpath("//span[@class='next']/a/@href").extract_first()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)
        #     yield response.follow(next_page, self.parse)
        pass


def get_digit(stg):
    # 匹配数字
    temp = re.findall("\d+\.?\d*", stg)
    return temp[0] if len(temp) > 0 else "NULL"
    # re.findall('[\u4e00-\u9fa5]',str1) 匹配中文
    pass