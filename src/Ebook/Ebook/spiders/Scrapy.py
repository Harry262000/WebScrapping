# def start_requests(self):
#     for url in self.start_urls:
#         yield SplashRequest(
#             url,
#             callback=self.parse,
#             endpoint='render.html',
#             args={'wait': 5}
#         )


# price = flat.css(".mb-srp__card__price--amount::text").get()


# # follow pagination
# next_page_url = response.css(".SRCard span.page-numbers.next a::attr(href)").get()
# if next_page_url:
#     yield SplashRequest(
#         next_page_url,
#         callback=self.parse,
#         endpoint='render.html',
#         args={'wait': 5}
#     )


# Scroll down the page to load more data
# scroll_script = 'window.scrollTo(0, document.body.scrollHeight); return true;'
# response.data['splash'].execute_js(scroll_script)

# # Extract the data using CSS selectors
# data = []
# items = response.css('div.item')
# for item in items:
#     data.append({
#         'title': item.css('h2::text').get(),
#         'price': item.css('span.price::text').get()
#     })
#
# yield {'data': data}
#
# item = {
#     'title': flat.css('h2::text').get(),
#     'price': flat.css('div.mb-srp__card__price div::text').get()
# }
# yield item
#
#
# import scrapy
# from scrapy.loader import ItemLoader
# from ..items import Flatitem
#
#
# class Flatspider(scrapy.Spider):
#     name = 'flat'
#     start_urls = ['https://www.magicbricks.com/property-for-rent/residential-real-estate?proptype=Multistorey'
#                   '-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment,Residential-House,'
#                   'Villa&cityName=Bangalore']
#
#     def parse(self, response):
#         print("[Response]")
#         flats = response.css("div.mb-srp__list")
#
#         for flat in flats:
#             loader = ItemLoader(item=Flatitem(), selector=flat)
#             loader.add_css('title', 'h2::text')
#             loader.add_css('price', 'div.mb-srp__card__price div::text')
#             yield loader.load_item()
#
#         scroll_script = "window.scrollTo(0, document.body.scrollHeight);"
#         yield scrapy.Request(url=response.url, callback=self.parse_scroll, meta={'scroll_script': scroll_script})
#
#     def parse_scroll(self, response):
#         print("[Scrolled Response]")
#         flats = response.css("div.mb-srp__list")
#
#         for flat in flats:
#             loader = ItemLoader(item=Flatitem(), selector=flat)
#             loader.add_css('title', 'h2::text')
#             loader.add_css('price', 'div.mb-srp__card__price div::text')
#             yield loader.load_item()
#
#         scroll_script = "window.scrollTo(0, document.body.scrollHeight);"
#         yield scrapy.Request(url=response.url, callback=self.parse_scroll, meta={'scroll_script': scroll_script})
#
#     def parse_scroll(self, response):
#         print("[Scrolled Response : 2]")
#         flats = response.css("div.mb-srp__list")
#
#         for flat in flats:
#             loader = ItemLoader(item=Flatitem(), selector=flat)
#             loader.add_css('title', 'h2::text')
#             loader.add_css('price', 'div.mb-srp__card__price div::text')
#             yield loader.load_item()
#
#         scroll_script = "window.scrollTo(0, document.body.scrollHeight);"
#         yield scrapy.Request(url=response.url, callback=self.parse_scroll, meta={'scroll_script': scroll_script})
