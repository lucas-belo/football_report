from src.database.query import get_document
from src.web_scraper.real_time_data_scraper.spider_run import *
from src.data_processing.json_unifier import json_formatter

import json

team_name = "Corinthians"

# Query database

document = get_document("brazil_teams", "serie_a", team_name)


# Run Scraper

RunSpider.run_spider_and_get_result(team_name)


# Get scraper json

scraper_json_path = 'src/web_scraper/real_time_data_scraper/team_data.json'

with open(scraper_json_path, 'r') as file:
    data = json.load(file)

scraper_json = data[0]


# Format jsons

json_formatter(document, scraper_json)

