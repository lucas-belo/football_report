# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RealTimeDataScraperItem(scrapy.Item):
    season_year = scrapy.Field()
    season_matches_data = scrapy.Field()
    competition_data = scrapy.Field()
    current_matches_data = scrapy.Field()
