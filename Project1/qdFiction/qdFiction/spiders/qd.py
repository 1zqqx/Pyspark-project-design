import re
import string

import scrapy

from ..items import QdfictionItem
from time import sleep


class QdSpider(scrapy.Spider):
    name = "qd"
    allowed_domains = ["www.qidian.com"]
    start_urls = []

    def start_requests(self):
        with open("urls.txt") as fs:
            self.start_urls = fs.readlines()

        for url in self.start_urls:
            print(f"[=] {url}")
            sleep(2)
            yield scrapy.Request(url=url, callback=self.parse)
        pass

    def parse(self, response):
        b_list = response.xpath('//div[@class="book-mid-info"]')
        date_li_y = response.xpath('//div[@class="btn-box cf"]/div[@id="year"]/a/span[1]/text()').get()
        date_li_m = response.xpath('//div[@class="btn-box cf"]/div[@id="month"]/a/span[1]/text()').get()
        print(f"[-] {date_li_y} - {date_li_m}")
        date_ = get_num(date_li_y) + "-" + get_num(date_li_m)
        for xp in b_list:
            item = QdfictionItem()
            item['book_name'] = xp.xpath('h2/a/text()').get().strip()
            item['book_author'] = xp.xpath('p[@class="author"]/a[@class="name"]/text()').get().strip()
            item['book_first_partition'] = xp.xpath('p[@class="author"]/a[2]/text()').get().strip()
            item['book_second_partition'] = xp.xpath('p[@class="author"]/a[3]/text()').get().strip()
            item['book_status'] = xp.xpath('p[@class="author"]/span/text()').get().strip()
            item['book_intro'] = xp.xpath('p[@class="intro"]/text()').get().strip()
            # item['book_wordage'] = item.xpath('p[@class="update"]/span/span/text()').get().strip() + "万字"
            item['date_list'] = date_
            yield item

        next_url = response.xpath('//div[@class="lbf-pagination"]/ul/li[1]/a/@href').get()
        if next_url != 'javascript:;' and next_url is not None:
            next_url = 'https:' + next_url
            sleep(2)
            print(f"[+] {next_url}")
            yield scrapy.Request(url=next_url, callback=self.parse)
        pass


def get_num(s: string) -> string:
    # 正则表达式提取所有数字
    return ''.join(re.findall(r'\d+', s))
    pass
