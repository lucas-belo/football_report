import os
from scrapy.crawler import CrawlerProcess

from src.web_scraper.real_time_data_scraper.real_time_data_scraper.spiders.ogol_spider import OgolSpiderSpider


class RunSpider:
    def __init__(self, file_name='team_data.json'):
        self.file_name = file_name

    @staticmethod
    def delete_file(file_name):
        try:
            os.remove(file_name)
            print(f"The file '{file_name}' has been successfully deleted.")
        except FileNotFoundError:
            print(f"The file '{file_name}' was not found.")
        except Exception as e:
            print(f"An error occurred while deleting the file '{file_name}': {str(e)}")

    delete_file('src/web_scraper/real_time_data_scraper/team_data.json')

    @staticmethod
    def run_spider_and_get_result(team_name):
        process = CrawlerProcess(
            settings={
                'FEED_URI': 'src/web_scraper/real_time_data_scraper/team_data.json',
                'FEED_FORMAT': 'json'
            }
        )
        process.crawl(OgolSpiderSpider, team_name=team_name)
        process.start()





