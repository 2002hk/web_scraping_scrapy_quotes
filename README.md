# web_scraping_scrapy_quotes
## To scrape quotes.toscrape.com website using scrapy
## Libraries used
- scrapy
- ipyhton
- virtualenv
## Project Structure
```bash
quotescraper/
│── venv/
│── quotescraper/               # Project module
│   ├── spiders/                # Spider definitions
│   │   ├── __init__.py
│   │   ├── quotespider.py        # Custom spider
│   ├── __init__.py
│   ├── items.py                # Define scraped data structure
│   ├── middlewares.py          # Custom middlewares
│   ├── pipelines.py            # Data processing pipelines
│   ├── settings.py             # Scrapy settings
│── scrapy.cfg                  # Scrapy configuration file
│── requirements.txt            # Dependencies
│── README.md                   # Project documentation
```
## Commands used
```bash
## to create virtual env
python -m venv venv
python venv\Scripts\activate
## to create project
scrapy startproject quotescraper
## go the spider folder
scrapy genspider quotespider quotes.toscrape.com
## to activate scrapy shell
scrapy shell
```
- Successfully able to scrape 1000 quotes from the website with effective pagination
