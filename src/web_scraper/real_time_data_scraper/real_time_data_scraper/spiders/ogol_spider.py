import scrapy


class OgolSpiderSpider(scrapy.Spider):
    name = "ogol_spider"
    allowed_domains = ["www.ogol.com.br"]
    start_urls = ["https://www.ogol.com.br"]

    def parse(self, response):
        pass
