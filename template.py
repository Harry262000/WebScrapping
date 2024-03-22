import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Sections based on data source types
data_sources = ["wiki", "website", "api"]
list_of_files = [
    ".github/workflows/python-app.yml",
    "flask_app/__init__.py",
    "flask_app/app.py",
    "flask_app/views.py",
    "flask_app/models.py",
    "flask_app/static/css/main.css",
    "flask_app/static/js/main.js",
    "flask_app/static/images/.gitkeep",
    "flask_app/templates/index.html",
    "requirements.txt",
    "README.md",
    "LICENSE",
    "Dockerfile",
    "config/config.yaml",
    "params.yaml",
    "data/.gitkeep",
]

# Adding files dynamically for each data source section
for source in data_sources:
    source_capitalized = source.capitalize()  # Capitalizing for better naming
    list_of_files += [
        f"scrapers/{source}/__init__.py",
        f"scrapers/{source}/{source}_scraper.py",
        f"scrapers/{source}/requirements_{source}.txt",
        f"flask_app/templates/{source}.html",
    ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # Just creating an empty file for now
        logging.info(f"Created empty file: {filepath}")

    else:
        logging.info(f"File already exists: {filepath}")