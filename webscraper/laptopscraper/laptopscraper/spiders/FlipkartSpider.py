import scrapy
from ..items import LaptopscraperItem


class FlipkartSpider(scrapy.Spider):
    name = 'flipkart'
    page = 1
    start_urls = [f'https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page}']


    def parse(self, response):
        for url in response.css('a._1fQZEK::attr(href)').getall():
            url = 'https://www.flipkart.com' + url
            yield scrapy.Request(url=url, callback=self.parse_product)
        
        self.page += 1
        if self.page <= 3:
            yield scrapy.Request(url=f'https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={self.page}', callback=self.parse)


    def parse_product(self, response):
        item = LaptopscraperItem()
        title = response.css('.B_NuCI::text').get()
        price = response.css('._16Jk6d::text').get()
        rating = response.css('._16VRIQ ._3LWZlK::text').get()
        reviews = response.css('._13vcmD+ span::text').get()

        # clean price
        try:
            price = price[1:].replace(',', '')
        except:
            price = None

        # clean reviews
        try:
            reviews = reviews[1:].replace(' Reviews', '')
        except:
            reviews = 0

        item['title'] = title
        item['price'] = price
        item['rating'] = rating
        item['reviews'] = reviews
        item['url'] = response.url
        item['is_refurbished'] = False
        item['website'] = 'flipkart'

        yield item