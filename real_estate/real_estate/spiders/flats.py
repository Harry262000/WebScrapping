import scrapy
from scrapy.loader import ItemLoader
from ..items import Flatitem


class Flatspider(scrapy.Spider):
    name = 'flat'
    start_urls = ['https://www.magicbricks.com/property-for-rent/residential-real-estate?bedroom=&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment,Residential-House,Villa&cityName=Bangalore']

    def parse(self, response):
        print("[Response]")
        flats = response.css("div.mb-srp__list")

        for flat in flats:
            loader = ItemLoader(item=Flatitem(), selector=flat)
            loader.add_css('title', 'h2::text')
            loader.add_css('price', 'div.mb-srp__card__price div::text')
            yield loader.load_item()

        scroll_script = "window.scrollTo(0, document.body.scrollHeight);"
        yield scrapy.Request(url=response.url, callback=self.parse_scroll, meta={'scroll_script': scroll_script})

    def parse_scroll(self, response):
        print("[Scrolled Response]")
        flats = response.css("div.mb-srp__list")

        for flat in flats:
            loader = ItemLoader(item=Flatitem(), selector=flat)
            loader.add_css('title', 'h2::text')
            loader.add_css('price', 'div.mb-srp__card__price div::text')
            yield loader.load_item()

        next_page = response.css('a.pagination__next::attr(href)').get()
        if next_page:
            scroll_script = "window.scrollTo(0, document.body.scrollHeight);"
            yield scrapy.Request(url=next_page, callback=self.parse_scroll, meta={'scroll_script': scroll_script})
