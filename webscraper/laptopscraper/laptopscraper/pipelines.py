# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class LaptopscraperPipeline:

    def __init__(self):
        self.create_connection()
        # self.create_table()

    def create_connection(self):
        # self.conn = sqlite3.connect('products.db')
        self.conn = sqlite3.connect('../../product_shoppy/db.sqlite3')
        self.curr = self.conn.cursor()

    def create_table(self):
        # self.curr.execute("""DROP TABLE IF EXISTS laptop""")
        self.curr.execute("""create table IF NOT exists laptops(
            id integer PRIMARY KEY AUTOINCREMENT, 
            title text,
            price real,
            rating real,
            reviews integer,
            url text,
            is_refurbished boolean,
            website CHAR(20)
        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item
        
    def store_db(self, item):
        if item['title'] is None or item['price'] is None or item['url'] is None:
            return
        self.curr.execute("""insert into products_api_laptop (title,price,rating,reviews,url,is_refurbished,website) values (?,?,?,?,?,?,?)""", (
            item['title'],
            item['price'],
            item['rating'],
            item['reviews'],
            item['url'],
            item['is_refurbished'],
            item['website']
        ))
        self.conn.commit()
