# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    pass

def serialize_price(value):
    return f'£ {str(value)}'

class BookItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    title = scrapy.Field()
    product_type = scrapy.Field()
    price_exl_tax = scrapy.Field(serializer = serialize_price)
    price_inc_tax = scrapy.Field(serializer = serialize_price)
    tax = scrapy.Field(serializer = serialize_price)
    availability = scrapy.Field()
    number_reviews = scrapy.Field()
    stars = scrapy.Field()
    category = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()


