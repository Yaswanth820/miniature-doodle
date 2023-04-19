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
6. Run the server using `python manage.py runserver <port>` (default port is 8000)
7. Go to `http://localhost:8000/api/v1/laptops/` to see the API

Open the above url in your browser to see the API. You can also use Postman to test the API.
MAKE SURE TO RUN ATLEAST ONE WEB SCRAPER BEFORE YOU RUN THE API.


## How to run specific web scraper

1. Go to the `laptops` directory - `cd laptops`
2. Run the web scraper using `scrapy crawl <spider-name>` (shopclues, flipkart, croma, reliance, vijaysales). Ex: `scrapy crawl shopclues`
3. The data will be stored in the database.
4. You can run the API now. Go to `http://localhost:8000/api/v1/laptops/` to see the API data


## API Endpoints

1. Filter (highest price/lowest price/highest review & rating) - GET `http://localhost:8000/api/v1/laptops/?ordering=<ordering>` (ordering can be - `price`, `-price`, `rating`, `-rating`) `-` refers to descending order

2. Search - GET `http://localhost:8000/api/v1/laptops/?search=<search_term>`

3. Filter by is_refurbished - GET `http://localhost:8000/api/v1/laptops/?is_refurbished=<true/false>`

4. Top n - This is default ordering - GET `http://localhost:8000/api/v1/laptops/`

5. Filter by price range - GET `http://localhost:8000/api/v1/laptops/?website=<website>` (website can be flipkart, shopclues, croma, reliance, vijaysales)

The response is paginated. The default page size is 10. You can change the page size by adding `page_size=<page_size>` to the query string. You can also change the page number by adding `page=<page_number>` to the query string.

```json
{
    "count": 36,
    "next": "http://localhost:8000/api/v1/laptops/?page=2&website=shopclues",
    "previous": null,
    "results": [
        {
            "title": "(Refurbished)DELL Latitude E7440 14.1-Inch Laptop ( intel Core I5-4rth), 8GB DDR3, 120GB SSD, Windows 10 , MS Office 19",
            "price": 29999.0,
            "rating": null,
            "total_review_count": 0,
            "website": "shopclues",
            "is_refurbished": true,
            "url": "https://www.shopclues.com/refurbished-dell-latitude-e7440-14.1-inch-laptop-intel-core-i5-4rth-8gb-ddr3-120gb-ssd-windows-10-ms-office-19-153062654.html"
        },
        {
            "title": "(Refurbished)DELL Latitude E7440 14.1-Inch Laptop ( intel Core I5-4rth), 4GB DDR3, 512GB SSD, Windows 10 , MS Office 19",
            "price": 30999.0,
            "rating": null,
            "total_review_count": 0,
            "website": "shopclues",
            "is_refurbished": true,
            "url": "https://www.shopclues.com/refurbished-dell-latitude-e7440-14.1-inch-laptop-intel-core-i5-4rth-4gb-ddr3-512gb-ssd-windows-10-ms-office-19-153062653.html"
        },
        {
            "title": "(Refurbished)DELL Latitude E7440 14.1-Inch Laptop ( intel Core I5-4rth), 8GB DDR3, 256GB SSD, Windows 10 , MS Office 19",
            "price": 31999.0,
            "rating": null,
            "total_review_count": 0,
            "website": "shopclues",
            "is_refurbished": true,
            "url": "https://www.shopclues.com/refurbished-dell-latitude-e7440-14.1-inch-laptop-intel-core-i5-4rth-8gb-ddr3-256gb-ssd-windows-10-ms-office-19-153062656.html"
        },
        {
            "title": "ASUS Vivobook 15 15.6 (39.62 cm) FHD AMD Dual Core Ryzen 3 3200U Thin and Light Laptop (8GB/256GB SSD/Integrated Graphics/Windows 11/Office 2021/Grey/1.68 Kg) X512DA-BQ302WS",
            "price": 36809.0,
            "rating": null,
            "total_review_count": 0,
            "website": "shopclues",
            "is_refurbished": false,
            "url": "https://www.shopclues.com/asus-vivobook-15-15.6-and-34-39.62-cm-fhd-amd-dual-core-ryzen-3-3200u-thin-and-light-laptop-8gb-256gb-ssd-integrated-graphics-windows-11-office-2021-grey-1.68-kg-x512da-bq302ws-153161156.html"
        },
        {
            "title": "Lenovo V14 Intel Core i3 10th Gen 14-inch HD Thin and Light Laptop (4GB RAM/ 1TB HDD/ Windows 10 Professional/ Grey/ 1.6 kg), 82C4016TIH",
            "price": 38899.0,
            "rating": null,
            "total_review_count": 0,
            "website": "shopclues",
            "is_refurbished": false,
            "url": "https://www.shopclues.com/lenovo-v14-intel-core-i3-10th-gen-14-inch-hd-thin-and-light-laptop-4gb-ram-1tb-hdd-windows-10-professional-grey-1.6-kg-82c4016tih-151425716.html"
        },
        {
            "title": "Lenovo Ideapad S145 Intel Core i5 10th Gen 15.6 inch FHD Thin and Light Laptop (8GB/1TB/Windows 10/Grey/1.85Kg) 81W800FLIN",
            "price": 42990.0,
            "rating": null,
            "total_review_count": 0,
            "website": "shopclues",
            "is_refurbished": false,
            "url": "https://www.shopclues.com/lenovo-ideapad-s145-intel-core-i5-10th-gen-15.6-inch-fhd-thin-and-light-laptop-8gb-1tb-windows-10-grey-1.85kg-81w800flin-152862661.html"
        },
        {
            "title": "Dell Inspiron 3593 15.6 inch FHD Laptop (10th Gen i3-1005G1/ 4GB/ 1TB/ Integrated Graphics/ Win 10 + MS Office/ Silver) D560299WIN9SE",
            "price": 43059.0,
            "rating": null,
            "total_review_count": 0,
            "website": "shopclues",
            "is_refurbished": false,
            "url": "https://www.shopclues.com/dell-inspiron-3593-15.6-inch-fhd-laptop-10th-gen-i3-1005g1-4gb-1tb-integrated-graphics-win-10--ms-office-silver-d560299win9se-151425718.html"
        },
        {
            "title": "Dell Inspiron 3501 15.6-inch FHD Laptop (10th Gen Core i3-1005G1/4GB/1TB HDD/Windows 10 Home + MS Office/Intel HD Graphics), Accent Black",
            "price": 44381.0,
            "rating": null,
            "total_review_count": 0,
            "website": "shopclues",
            "is_refurbished": false,
            "url": "https://www.shopclues.com/dell-inspiron-3501-15.6-inch-fhd-laptop-10th-gen-core-i3-1005g1-4gb-1tb-hdd-windows-10-home--ms-office-intel-hd-graphics-accent-black-151425717.html"
        },
        {
            "title": "Asus VivoBook 15 X515JA-BQ511WS Laptop (10th Gen-Intel Core i5-1035G1/8GB/256GB SSD/Intel UHD Graphics/Windows 11/MSO/FHD) 39.62 cm (15.6 inch",
            "price": 45299.0,
            "rating": null,
            "total_review_count": 0,
            "website": "shopclues",
            "is_refurbished": false,
            "url": "https://www.shopclues.com/asus-vivobook-15-x515ja-bq511ws-laptop-10th-gen-intel-core-i5-1035g1-8gb-256gb-ssd-intel-uhd-graphics-windows-11-mso-fhd-39.62-cm-15.6-inch-153161169.html"
        },
        {
            "title": "Dell Inspiron Core i5 11th Gen 4 GB RAM/ 1 TB HDD + 256 GB SSD/ 15.6 Inch Laptop (Black, D560398WIN9B)",
            "price": 46099.0,
            "rating": null,
            "total_review_count": 0,
            "website": "shopclues",
            "is_refurbished": false,
            "url": "https://www.shopclues.com/dell-inspiron-core-i5-11th-gen-4-gb-ram-1-tb-hdd--256-gb-ssd-15.6-inch-laptop-black-d560398win9b-152433223.html"
        }
    ]
}

```
