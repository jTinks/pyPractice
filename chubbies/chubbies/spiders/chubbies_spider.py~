from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from chubbies.items import chubbiesItem
class ChubbiesSpider(BaseSpider):
    name = "chubbies" # Name of the spider, to be used when crawling
    allowed_domains = ["chubbiesshorts.com"] # Where the spider is allowed to go
    start_urls = [
        "http://www.chubbiesshorts.com/collections/the-originals/"
    ]
    def parse(self, response):
        hxs = HtmlXPathSelector(response) # The XPath selector
        sites = hxs.select('//li[contains(@class, "product product-title")]/div[@class="product_wrap"]')
        items = []
        for site in sites:
            item = chubbiesItem()
            item['name'] = site.select('div[@class="details"]/a/text()').extract()
            item['link'] = site.select('div[@class="basic_stat product_title"]/a/@href').extract()
            item['price'] = site.select('div[@class="basic_stat product_score brief_metascore"]/div/div/
                                     span[contains(@class, "data metascore score")]/text()').extract()
            item['desk'] = site.select('div[@class="more_stats condensed_stats"]/ul/li/
                                     span[contains(@class, "data textscore textscore")]/text()').extract()
            items.append(item)
        return items



