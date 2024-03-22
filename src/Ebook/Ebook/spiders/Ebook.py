import scrapy
from scrapy.loader import ItemLoader
from ..items import EbookItem

class EbookSpider(scrapy.Spider):

    name = "ebook"
    start_urls = ["https://books.toscrape.com/catalogue/category/books/travel_2/"]
#
# def __init__(self):
#     super().__init__()
#     self.page_count = 0

def parse(self, response):
    ebooks = response.css("article.product_pod")

    for ebook in ebooks:
        loader = ItemLoader(item=EbookItem(), Selector=ebook)

        loader.add_css('title', "h3 a::attr(title)")
        loader.add_css('price', "p.price_color::text")

        yield loader.load_item()

    # next_btn = response.css("li.next a")
    #
    # if next_btn:
    #     next_page =  f"{self.start_urls[0]/next_btn.attrib['href']}"
    #     yield scrapy.Request(url=next_page)