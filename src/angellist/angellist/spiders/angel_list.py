import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://wellfound.com/startups/location/bangalore-urban"

# Define user-agent header
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

# Send GET request with headers
response = requests.get(url, headers=headers)

# Check the status code of the response
if response.status_code == 200:
    print("Status code:", response.status_code)
    
    # Parse HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Now you can extract data from the parsed HTML using BeautifulSoup
    # For example, find all tables and convert them to Pandas DataFrames
    tables = pd.read_html(url)
    for table in tables:
        print(table)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

# Introduce a delay before making the next request
time.sleep(2)  # Delay of 2 seconds
