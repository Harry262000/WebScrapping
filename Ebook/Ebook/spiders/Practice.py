import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/events/python-events/'
req = requests.get(url)

soup = BeautifulSoup(req.text, 'lxml')
events = soup.find('ul', {'class': 'list-recent-events'}).findAll('li')
for event in events:
    event_details = dict()
    event_details['name'] = event_details['name'] = event.find('h3').find('a').text
    event_details['location'] = event.find('span', {'class', 'event-location'}).text
    event_details['time'] = event.find('time').text
    print(event_details)
