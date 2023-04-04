import scrapy
import json
from ..items import LaptopscraperItem

class RelianceSpider(scrapy.Spider):
    name = 'reliance'
    page = 1
    start_urls = [f'https://www.reliancedigital.in/rildigitalws/v2/rrldigital/cms/pagedata?pageType=categoryPage&categoryCode=S101210&page=1&size=24']

    def parse(self, response):
        item = LaptopscraperItem()
        data = json.dumps(response.body)
        products = data['productListData']['results']
        for product in products:
            item['title'] = product['name']
            item['price'] = product['price']['value']
            item['rating'] = product['averageRating']
            item['reviews'] = product['numberOfReviews']
            item['url'] = product['url']
            item['is_refurbished'] = False
            item['website'] = 'reliance'

            yield item

        self.page += 1
        if self.page <= 3:
            yield scrapy.Request(url=f'https://www.reliancedigital.in/rildigitalws/v2/rrldigital/cms/pagedata?pageType=categoryPage&categoryCode=S101210&page={self.page}&size=24', callback=self.parse)