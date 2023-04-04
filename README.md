# Miniature-doodle 

This is an API that compares product prices accross different websites. Currently this fetches laptop data. It supports Flipkart, Shopclues, Croma, Vijay Sales, Reliance.

There are two main components to this project:

1. The API
2. The Web Scraper

## The API

The API is a RESTful API that allows you to search for a product and get the price of the product from different websites as well. It offers robust filtering of products. The API is built using the Django REST Framework and uses Django's ORM to query the database (SQLite). The results are paginated and the API supports searching, filtering and ordering. We can filter based on price range, search term, second hand or not, total review count, ratings, website. To speed up the query time I have used database indexes and caching. I have indexed the most frequently used filters which are price, total_review_count, website. I have also used the Django cache framework to cache the API results. The cache is invalidated after 15 minutes.

## The Web Scraper

The web scraper is a Python script that scrapes the data from the websites and stores it in the database. It uses the Scrapy framework to scrape the data. Currently it scrapes 3 pages of every site. However, this number can be cranked up by changing the page limit. To avoid rate limiting I have used the User-Agent rotation and random delays along with a proxy pool.


## How to run the project

1. Clone the repository
2. Create a virtual environment
3. Install the requirements using `pip install -r requirements.txt`
4. Run the migrations using `python manage.py make migrations` and `python manage.py migrate`
5. Run the web scraper using `scrapy crawl <spider-name>` (croma, flipkart, shopclues, reliance, vijaysales).
6. Run the server using `python manage.py runserver <port>`
7. Go to `http://localhost:<port>/api/v1/laptops/` to see the API

