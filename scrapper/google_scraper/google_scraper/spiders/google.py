import scrapy


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['api.scraperapi.com']
    start_urls = ['http://api.scraperapi.com/']

    def parse(self, response):
        pass
