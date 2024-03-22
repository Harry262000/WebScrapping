import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/CL%3DF/history?period1=1534377600&period2=1692144000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')
events = soup.find('div', {'class':'Pb(10px) Ovx(a) W(100%)'}).findAll('td',{"class":"Py(10px) Ta(start) Pend(10px)"})
for data in events:
    print("=====")
    print(data)

