import scrapy

from ..items import LjxspiderItem


class LjxSpider(scrapy.Spider):
    name = "ljx"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        top250_list = response.xpath("//div[@class='item']")

        for it in top250_list:
            item = LjxspiderItem()

            #
            item['moviesImg'] = it.xpath('div[@class="pic"]/a/img/@src').extract()
            #
            temp = it.xpath('div[@class="info"]/div[@class="hd"]/a/span[@class="title"]/text()'
                            ).extract()  # .replace(u'\xa0', '')
            item['moviesName'] = [i.replace(u'\xa0', '').replace('\\', '').replace('/', '') for i in temp]
            #
            item['moviesOtherName'] = it.xpath('div[@class="info"]/div[@class="hd"]/a/span[@class="other"]/text()'
                                               ).extract_first().replace('/', '').replace(u'\xa0', '')

            yield item

        next_page = response.xpath("//span[@class='next']/a/@href").extract_first()
        # if next_page:
        #     yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)
        #     yield response.follow(next_page, self.parse)
        pass
