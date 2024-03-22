# web_scraping_project/

│
├── src/                   # Source code folder
│   ├── __init__.py        # Package initialization file
│   ├── scrapers/          # Folder for scraper modules
│   │   ├── __init__.py    # Package initialization file
│   │   └── scraper1.py    # Scraper module 1
│   │   └── scraper2.py    # Scraper module 2
│   │   └── ...            # Other scraper modules
│   │
│   ├── utils/             # Folder for utility functions
│   │   ├── __init__.py    # Package initialization file
│   │   └── helpers.py     # Helper functions
│   │
│   └── main.py            # Main script to run the scraping process
│
├── data/                  # Folder to store scraped data
│   └── output/            # Folder to store final output files
│       └── output.csv     # Final output CSV file
│       └── output.json    # Final output JSON file
│       └── ...            # Other output files
│
├── notebooks/             # Folder for Jupyter notebooks (optional)
│
├── requirements.txt       # File listing all Python dependencies
└── README.md              # Project documentation

# 🕸️ Web Scraping Repository

Welcome to the Web Scraping Repository! Explore a variety of web scraping projects covering diverse topics like crude oil, cryptocurrencies, Glassdoor job data, real estate, and SpaceX. Each project is equipped with its own set of web scraping tools, and we've provided links to the code so you can dive right in.

## Projects

### 🛢️ Crude Oil

- __Directory__: [Crude_oil](./Crude_oil/Crude_oil/spiders/Oil_data.py)
- __Last Update__: [Last Commit](./Crude_Oil)
- __Description__: Web scraping project related to crude oil data.
- __Tools Used__: BeautifulSoup, Requests

### 📚 Ebook

- __Directory__: [Ebook](./Ebook)
- __Last Update__: [Last Commit](./Ebook)
- __Description__: Web scraping project related to ebooks.
- __Tools Used__: Scrapy, Selenium

### 💰 Crypto

- __Directory__: [Crypto](./crypto/crypto/spiders)
- __Last Update__: [Last Commit](./crypto)
- __Description__: Web scraping project related to cryptocurrency data.
- __Tools Used__: BeautifulSoup, Requests

### 🏢 Glassdoor

- __Directory__: [Glassdoor](./glassdoor)
- __Last Update__: [Last Commit](./glassdoor)
- __Description__: Web scraping project related to Glassdoor job data.
- __Tools Used__: Scrapy, Selenium

### 🏡 Real Estate

- __Directory__: [Real_estate](./real_estate)
- __Last Update__: [Last Commit](./real_estate)
- __Description__: Web scraping project related to real estate data.
- __Tools Used__: BeautifulSoup, Requests

### 🚀 SpaceX

- __Directory__: [SpaceX](./spacex)
- __Last Update__: [Last Commit](./spacex)
- __Description__: Web scraping project related to SpaceX data.
- __Tools Used__: Scrapy, Selenium

## How to Use

Each subdirectory contains its respective web scraping project. To explore the code and data, click on the directory name, and you'll find detailed instructions and scripts.

## Contribution

Feel free to contribute to any of these projects or create new ones. We welcome your ideas and enhancements to our web scraping efforts.

## License

This repository is open source and available under the [MIT License](./LICENSE).

Happy scraping! 🌐🔍
