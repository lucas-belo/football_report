import json

from pydash import get

from logs.logs_setup import successfully_process_log
from path import project_folder
from src.data_processing.data_processing import data_processing
from src.data_processing.json_unifier import json_formatter
from src.database.query import get_document
from src.web_scraper.real_time_data_scraper.spider_run import run_spider_and_get_result, delete_file


def run_report_generator(country: str, league: str, team: str) -> dict[str, str | int | list[str] | list[int]]:
    """
    This main function orchestrates all the system steps:
     - Query the database
     - Delete the old scrapped data
     - Runs the web scraper
     - Unify database and scraper json
     - Process the json data
     - Render the report html

    :param country: the name of the country
    :param league: the name of the league
    :param team: the name of the team
    :return: the completed json
    """

    scraper_json_path = f'{project_folder}/src/web_scraper/real_time_data_scraper/team_data.json'
    scraper_exception_json_path = f'{project_folder}/src/web_scraper/real_time_data_scraper/scraper_exception.json'

    # Query database
    document = get_document(country, league, team)

    # Run Scraper
    delete_file(scraper_json_path)
    run_spider_and_get_result(team)

    # Get scraper json
    with open(scraper_json_path, 'r') as file:
        data = json.load(file)

    with open(scraper_exception_json_path, 'r') as file:
        exception_data = json.load(file)

    scraper_exception_json = get(exception_data, "0", {"Scraper exception data not found..."})
    scraper_json = get(data, "0", scraper_exception_json)

    # Format jsons
    formatted_json = json_formatter(document, scraper_json)

    data_processing(formatted_json, 'src/view_pages/report/template.html')

    successfully_process_log()

    return formatted_json


if __name__ == "__main__":
    teams = ["Sport Club Corinthians Paulista", "São Paulo Futebol Clube"]

    for team in teams:
        run_report_generator("brazil_teams", "serie_a", team)
