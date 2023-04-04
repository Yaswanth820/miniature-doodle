import scrapy
from ..items import LaptopscraperItem

class ShopCluesSpider(scrapy.Spider):
    name = 'shopclues'
    page = 1
    start_urls = [f'https://www.shopclues.com/ajaxCall/searchProducts?q=laptop&z=0&page={page}']


    def parse(self, response):
        for url in response.css('.row a::attr(href)'):
            url = url.get()[2:]
            url = 'https://' + url
            yield scrapy.Request(url=url, callback=self.parse_product)
        
        self.page += 1
        if self.page <= 3:
            yield scrapy.Request(url=f'https://www.shopclues.com/ajaxCall/searchProducts?q=laptop&z=0&page={self.page}', callback=self.parse)
    

    def parse_product(self, response):
        item = LaptopscraperItem()
        title = response.css('h1::text').get()
        is_refurbished = 'Refurbished' in title
        # clean title
        title = title.strip()
        title = title.replace('\n', '').replace('\"', '').replace('(Refurbished)', '')
        price = response.css('.f_price::text').get().replace('₹', '')
        rating = response.css('#main_data .prd_ratings > span:nth-child(1)::text').get()
        reviews = response.css('.rr a span::text').get()
        if reviews == 'Be the first to write a review':
            reviews = 0

        item['title'] = title
        item['price'] = price
        item['rating'] = rating
        item['reviews'] = reviews
        item['url'] = response.url
        item['is_refurbished'] = is_refurbished
        item['website'] = 'shopclues'

        yield item