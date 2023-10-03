from scrapy import signals
from twisted.internet import reactor
import subprocess
from multiprocessing import Process, Queue
import scrapy.crawler as crawler
from scrapy.crawler import CrawlerRunner

import logging
from scrapy.crawler import CrawlerProcess
from src.web_scraper.real_time_data_scraper.real_time_data_scraper.spiders.ogol_spider import OgolSpiderSpider

from logs.logs_setup import setup_logging

setup_logging()


def delete_file(file_name):
    try:
        with open(file_name, "w"):
            pass
        print(f"The file '{file_name}' has been successfully deleted.")
        logging.info(f"The file '{file_name}' has been successfully deleted.")
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
        logging.info(f"The file '{file_name}' has been successfully deleted.")
    except Exception as e:
        print(f"An error occurred while deleting the file '{file_name}': {str(e)}")
        logging.error(f"An error occurred while deleting the file '{file_name}': {str(e)}")


def run_spider_and_get_result(team_name):
    try:
        print("Starting the ogol_spider runner")
        logging.info("Starting the ogol_spider runner")
        process = CrawlerProcess(
            settings={
                'FEED_URI': 'src/web_scraper/real_time_data_scraper/team_data.json',
                'FEED_FORMAT': 'json'
            }
        )
        process.crawl(OgolSpiderSpider, team_name=team_name)
        process.start()

        import sys
        del sys.modules['twisted.internet.reactor']
        from twisted.internet import reactor
        from twisted.internet import default
        default.install()


    except Exception as e:
        print(f"An error occurred trying to run the ogol_spider: {e}")
        logging.error(f"An error occurred trying to run the ogol_spider: {e}")

# def run_spider_and_get_result(team_name):
#     try:
#         print("Starting the ogol_spider runner")
#         logging.info("Starting the ogol_spider runner")
#
#         runner = CrawlerProcess(
#             settings={
#                 'FEED_URI': 'src/web_scraper/real_time_data_scraper/team_data.json',
#                 'FEED_FORMAT': 'json'
#             },
#         )
#
#         d = runner.crawl(OgolSpiderSpider, team_name=team_name)
#         d.addBoth(lambda _: reactor.stop())
#         reactor.run()
#
#         import sys
#         del sys.modules['twisted.internet.reactor']
#         from twisted.internet import reactor
#         from twisted.internet import default
#         default.install()
#
#     except Exception as e:
#             print(f"An error occurred trying to run the ogol_spider: {e}")
#             logging.error(f"An error occurred trying to run the ogol_spider: {e}")


# def run_spider_and_get_result(team_name):
#     try:
#         print("Starting the ogol_spider runner")
#         logging.info("Starting the ogol_spider runner")
#         crawled_items = []
#
#         def add_item(item):
#             crawled_items.append(item)
#
#         runner = CrawlerRunner()
#         crawler = Crawler(OgolSpiderSpider, settings={
#                      'FEED_URI': 'src/web_scraper/real_time_data_scraper/team_data.json',
#                      'FEED_FORMAT': 'json'
#                       }
#                           )
#
#         crawler.signals.connect(add_item, signal=signals.item_scraped)
#
#         d = runner.crawl(crawler, team_name=team_name)
#         d.addBoth(lambda _: reactor.stop())
#         reactor.run()
#
#     except Exception as e:
#         print(f"An error occurred trying to run the ogol_spider: {e}")
#         logging.error(f"An error occurred trying to run the ogol_spider: {e}")
#
