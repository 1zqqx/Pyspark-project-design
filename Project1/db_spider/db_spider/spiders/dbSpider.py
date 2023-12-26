import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'dbSpider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/36178641/reviews']

    def parse(self, response):
        review_list = response.xpath('//html/body/div[@class="wrapper"]/div[@id="content"]/div[1]/div[1]/div['
                                     '@class="review-list  "]')

        res_list = []
        for item in res_list:
            print(item)
        pass
