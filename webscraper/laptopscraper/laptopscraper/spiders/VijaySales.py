import scrapy
import json
from ..items import LaptopscraperItem

class VijaySpider(scrapy.Spider):
    name = 'vijay_sales'
    page = 1
    start_urls = [f'https://search.unbxd.io/f9d11deb7fc16223c3d695a0cfeb479c/ss-unbxd-prod-vijaysales33881654062505/search?version=V2&q=laptop&rows=12&page={page}&f.cityId_1_price_unx_f.facet.range.start=0&f.cityId_1_price_unx_f.facet.range.end=3000000&f.cityId_1_price_unx_f.facet.range.gap=1000&fields=uniqueId,sku,title,imageUrl,productUrl,cityId_1_*']


    def parse(self, response):
        data = json.loads(response.body)
        for product in data['response']['products']:
            url = product['productUrl']
            yield scrapy.Request(url=url, callback=self.parse_product)

        # scrape 3 pages
        if self.page <= 3:
            self.page += 1
            yield scrapy.Request(url=f'https://search.unbxd.io/f9d11deb7fc16223c3d695a0cfeb479c/ss-unbxd-prod-vijaysales33881654062505/search?version=V2&q=laptop&rows=12&page={self.page}&f.cityId_1_price_unx_f.facet.range.start=0&f.cityId_1_price_unx_f.facet.range.end=3000000&f.cityId_1_price_unx_f.facet.range.gap=1000&fields=uniqueId,sku,title,imageUrl,productUrl,cityId_1_*', callback=self.parse)


    def parse_product(self, response):
        item = LaptopscraperItem()
        title = response.css('#ContentPlaceHolder1_h1ProductTitle::text').get()
        title = title.encode('ascii', 'xmlcharrefreplace')
        title = title.decode('utf-8')
        reviews = response.css('.clsRatingCounts::text').get()
        if reviews is None:
            reviews = 0
        
        item['title'] = title
        item['price'] = response.css('br+ span span::text').get()
        item['rating'] = response.css('.starcolor::text').get()
        item['reviews'] = reviews
        item['url'] = response.url
        item['is_refurbished'] = False
        item['website'] = 'vijay_sales'

        yield item