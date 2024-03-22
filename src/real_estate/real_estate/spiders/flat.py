import requests
from bs4 import BeautifulSoup

url = ''
req = requests.get(url)

soup = BeautifulSoup(req.text, 'html.parser')
events = soup.find('div', {'class': 'mb-srp__card'}).findAll('div')
for event in events:
    event_details = dict()
    event_details['name'] = event_details['name'] = event.find('div', {'class', 'mb-srp__card__price--amount'}).find('h2').text
    event_details['location'] = event.find('div', {'class', 'mb-srp__card__price--amount'}).text
    print(event_details)


#from bs4 import BeautifulSoup
# import requests
#
#
# HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
# res = requests.get("https://www.zomato.com/bangalore", headers=HEADERS)
# html = res.status_code
# print(html)


