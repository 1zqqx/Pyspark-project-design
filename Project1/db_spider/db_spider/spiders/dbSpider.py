from typing import Dict, Any

import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'dbSpider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/36178641/reviews']

    def parse(self, response):
        review_list = response.xpath('//div[@class="main review-item"]')
        # movies_cid = review_list.xpath('.//@data-cid').extract()

        movies_review = []

        for i in review_list:
            movies_map = {}

            movies_name = i.xpath(
                "a/img[@rel='v:image']/@title")
            # 用户名
            user_name = i.xpath(
                "header/a[@class='name']/text()").extract_first()
            # 评价时间
            reviews_time = i.xpath(
                "header/span[@class='main-meta']/text()").extract_first()
            # 一句总结
            reviews_title = i.xpath(
                "div/h2/a/text()").extract_first()
            #  影评内容 短版
            reviews_short_content = i.xpath(
                "div/div[@class='review-short']/div/text()").extract_first()
            str.replace(reviews_short_content, ' ', '')
            str.replace(reviews_short_content, '\n', '')
            str.replace(reviews_short_content, u'\xa0', '')
            str.replace(reviews_short_content, u'\u3000', '')
            # 赞同
            reviews_approve = i.xpath(
                "div/div[@class='action']/a[@class='action-btn up']/span/text()").extract_first()
            # 不赞同
            reviews_against = i.xpath(
                "div/div[@class='action']/a[@class='action-btn down']/span/text()").extract_first()
            # 回复数
            reviews_reply = i.xpath(
                "div/div[@class='action']/a[@class='reply ']/text()").extract_first()

            movies_map['movies_name'] = movies_name
            movies_map['user_name'] = user_name
            movies_map['reviews_time'] = reviews_time
            movies_map['reviews_title'] = reviews_title
            movies_map['reviews_short_content'] = reviews_short_content
            movies_map['reviews_approve'] = reviews_approve
            movies_map['reviews_against'] = reviews_against
            movies_map['reviews_reply'] = reviews_reply
            movies_review.append(movies_map)
            pass

            # movies_map['user'] = review_list.xpath(
            #     './header[@class="main-hd"]/a[@class="name"]/text()').extract_first()
            # movies_map['review_time'] = review_list.xpath(
            #     './/div[@id=' + i + ']/header[@class="main-hd"]/span[@class="main-meta"]/text()').extract_first()

            # user_name = review_list.xpath('.//div[1]/header[@class="main-hd"]/a[@class="name"]/text()')
            # print(movies_cid)

        for i in movies_review:
            print(i)
        pass
