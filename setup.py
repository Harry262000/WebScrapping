import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.1"

setuptools.setup(
    name="web_scrapping_projects",
    version = __version__,
    author = "Harshal Honde",
    author_email= "Harshalhonde50@gmail.com", 
    description ="A Python package for web scraping ", 
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/HarshalHonde50/WebScrapping",
    project_urls = {
        "Bug Tracker": "https://github.com/HarshalHonde50/WebScrapping/issues"},
    packages = setuptools.find_packages(),  # <-- Corrected parameter name
    classifiers= [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
    python_requires = ">=3.6"
)
