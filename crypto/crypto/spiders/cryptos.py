import requests
import pandas as pd
from bs4 import BeautifulSoup

# Set up headers
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

# Initialize an empty list to store data
all_cryptos = []

# Initialize variables for pagination and page limit
page = 1
page_limit = 300
has_more_data = True

while has_more_data and page <= page_limit:
    # Make a request to the website
    url = f"https://crypto.com/price?page={page}"
    res = requests.get(url, headers=HEADERS)
    html = res.text
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", class_='chakra-table css-1qpk7f7')

    # Check if there is data in the table
    if table:
        for rows in table.find_all("tr", class_="css-1cxc880"):
            serial = rows.find("td", class_="css-w6jew4").text.strip()
            names = rows.find("p", class_="chakra-text css-rkws3").text.strip()
            short_names = rows.find("span", class_="chakra-text css-1jj7b1a").text.strip()
            price = rows.find("div", class_="css-b1ilzc").text.strip()
            hrs = rows.find("td", class_="css-vtw5vj").text.strip()
            vols = rows.find("td", class_="css-15lyn3l").text.strip()

            # Append data to the list
            all_cryptos.append([serial, names, short_names, price, hrs, vols])

        # Move to the next page
        page += 1
    else:
        has_more_data = False

# Create a DataFrame from the collected data
df = pd.DataFrame(all_cryptos, columns=["Serial", "Names", "Short Names", "Price", "24h Change", "Volume"])

# Save DataFrame to a CSV file
df.to_csv("crypto_data.csv", index=False)
