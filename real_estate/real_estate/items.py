
from scrapy import Item, Field

class Flatitem(Item):
    title = Field()
    price = Field()
