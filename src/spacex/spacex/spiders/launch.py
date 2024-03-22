import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches_(2010%E2%80%932019)#Launches"

req = requests.get(url)

soup = BeautifulSoup(req.text, 'html.parser')
table = soup.find("tbody")
table_data = {}
for row in table.find("tr"):
    row_name = row.findall('td').text.strip()
    row_value = row.find_all('td')[1].text.strip()

    # Assign the row_name as the key and row_value as the value in the dictionary
    table_data[row_name] = row_value
    print(table_data)






























# import scrapy
#
# class spacexSpider(scrapy.Spider):
#     name = 'spacex'
#     start_urls = ["https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches_(2010%E2%80%932019)#Launches"]
#
#     def parse(self, response, **kwargs):
#         print("=========")
#         table = response.css("tbody")
#
#         launch_details = {}
#         for row in table.css("tr"):
#             heading = row.css("th::text").get()
#             data = row.css("td::text").get()
#
#         yield launch_details
