# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AngellistItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    location = scrapy.Field()