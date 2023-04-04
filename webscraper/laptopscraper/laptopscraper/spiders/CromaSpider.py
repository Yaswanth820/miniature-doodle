import scrapy
import json
from ..items import LaptopscraperItem

class CromaSpider(scrapy.Spider):
    name = 'croma'
    page = 1
    start_urls = [f'https://api.croma.com/cmstemplate/allchannels/v1/custompage?pageLabelOrId=clp/laptops-for-everyday-use&currentPage={page}&q=:relevance:laptoplifestyle:Everyday+Use:ZAStatusFlag:true']


    def parse(self, response):
        item = LaptopscraperItem()
        data = json.loads(response.body)
        for product in data['products']:
            item['title'] = product['name']
            item['price'] = product['price']['value']
            item['rating'] = product['finalReviewRating']
            item['reviews'] = product['onlyRatingCount']
            item['url'] = 'https://croma.com' + product['url']
            item['is_refurbished'] = False
            item['website'] = 'croma'

            yield item

        # scrape 3 pages
        if self.page <= 3:
            self.page += 1
            yield scrapy.Request(url=f'https://api.croma.com/cmstemplate/allchannels/v1/custompage?pageLabelOrId=clp/laptops-for-everyday-use&currentPage={self.page}&q=:relevance:laptoplifestyle:Everyday+Use:ZAStatusFlag:true', callback=self.parse)