Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

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
