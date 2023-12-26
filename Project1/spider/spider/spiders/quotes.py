import scrapy


# 创建scrapy 项目  scrapy startproject <project name>
# 创建  scrapy genspider quotes "quotes.toscrape.com"


# scrapy crawl <name>
# scrapy crawl <name> -o <name>.json

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        res = response.xpath('//div[@class="quote"]')
        # for quote in res:
        #     yield {
        #         # "text": quote.xpath("span[1]")
        #         "text": quote.xpath(".//span[@class='text']/text()").extract_first(),
        #         "author": quote.xpath(".//small[@class='author']/text()").extract_first(),
        #         "tags": quote.xpath(".//div[@class='tags']/a[@class='tag']/text()").extract(),
        #     }
        re = []
        for quote in res:
            # "text": quote.xpath("span[1]")
            te = {}
            text = quote.xpath(".//span[@class='text']/text()").extract_first()
            author = quote.xpath(".//small[@class='author']/text()").extract_first()
            tags = quote.xpath(".//div[@class='tags']/a[@class='tag']/text()").extract()
            te["text"] = text
            te["author"] = author
            te["tags"] = tags
            re.append(te)
        print(re)
        return re
