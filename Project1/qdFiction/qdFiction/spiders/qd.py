import scrapy

from ..items import QdfictionItem
from time import sleep


# 全部作品 100 条 - 收藏

class QdSpider(scrapy.Spider):
    name = "qd"
    allowed_domains = ["www.qidian.com"]
    start_urls = ["https://www.qidian.com/all/orderId11-page5/"]

    def parse(self, response):
        li_list = response.xpath('//div[@class="book-mid-info"]')

        for item in li_list:
            book = QdfictionItem()
            book['book_name'] = item.xpath('h2/a/text()').get().strip()
            book['book_author'] = item.xpath('p/a[@class="name"]/text()').get().strip()
            book['book_first_partition'] = item.xpath('p/a[2]/text()').get().strip()
            book['book_second_partition'] = item.xpath('p/a[3]/text()').get().strip()
            book['book_status'] = item.xpath('p/span/text()').get().strip()
            book['book_intro'] = item.xpath('p[@class="intro"]/text()').get().strip()
            book['book_wordage'] = item.xpath('p[@class="update"]/span/span/text()').get().strip() + "万字"
            yield book

        # 起点网站第四页没有去往第五页的链接 但是可以倒着来 从第五页向前
        next_url = response.xpath(
            '//div[@class="lbf-pagination"]/ul/li[1]/a/@href').get()
        if next_url != 'javascript:;' and next_url is not None:
            next_url = 'https:' + next_url
            print("[=] " + next_url)
            sleep(1)
            yield scrapy.Request(url=next_url, callback=self.parse)
        pass
