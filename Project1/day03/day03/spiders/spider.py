import scrapy

from day03.items import Day03Item


class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/subject/35208463/reviews"]

    def parse(self, response):
        review_list = response.xpath("//div[@class='main review-item']")

        items = []
        for im in review_list:
            item = Day03Item()
            item['userAvator'] = im.xpath(
                "header/a[@class='avator']/img/@src")
            items.append(item)

        print(len(items))
        print(items)
        return items
        pass
