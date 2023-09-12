from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from io import StringIO
import json

from src.web_scraper.real_time_data_scraper.real_time_data_scraper.spiders.ogol_spider import OgolSpiderSpider

process = CrawlerProcess(get_project_settings())

process.crawl(OgolSpiderSpider)
process.start()






