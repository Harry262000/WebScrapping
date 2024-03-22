import setuptools
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Read the contents of README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

# Log a message indicating the start of the setup process
logging.info('Setup process started...')

# Create a 'logging' directory
logging_folder = "logging"
if not os.path.exists(logging_folder):
    os.makedirs(logging_folder)
    logging.info(f"Created directory: {logging_folder}")

# Create a log file inside the 'logging' directory
log_file = os.path.join(logging_folder, "setup.log")
with open(log_file, "w") as log:
    log.write("Setup process started...\n")

# Call setuptools.setup() with your package details
setuptools.setup(
    name="web_scrapping_projects",
    version=__version__,
    author="Harshal Honde",
    author_email="Harshalhonde50@gmail.com",
    description="A Python package for web scraping",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HarshalHonde50/WebScrapping",
    project_urls={
        "Bug Tracker": "https://github.com/HarshalHonde50/WebScrapping/issues"
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
    python_requires=">=3.6"
)

# Log a message indicating the end of the setup process
logging.info('Setup process completed.')
