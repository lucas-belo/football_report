import logging

from jinja2 import Template

from logs.logs_setup import setup_logging
from src.data_processing.utils.teams_crest_url import teams_crest_url

setup_logging()


def data_processing(json: any, template_html_file: str) -> None:
    """
    Process JSON data and render an HTML report.

    :param json: the completed json (database and scrapped data)
    :param template_html_file: the report html template
    :return: None. Just render the html and store it in the file report.html
    """
    try:
        with open(template_html_file, "r", encoding="utf-8") as file:
            template_html = file.read()
        template = Template(template_html)

        crowd_quantity = json["crowd"]["quantity"]
        stadium_capacity = json["stadium"]["capacity"]

        def format_number(json_field):
            formatted_number = "{:,}".format(json_field)
            formatted_number = formatted_number.replace(",", ".")
            return formatted_number

        formatted_crowd_quantity = format_number(crowd_quantity)
        formatted_stadium_capacity = format_number(stadium_capacity)

        html_report = template.render(
            team=json["name"],
            state=json["state"],
            stadium_name=json["stadium_name"],
            founding_year=json["founding_year"],
            titles=json["titles"],
            relegation=json["relegation"],
            crowd=json["crowd"],
            formatted_crowd_quantity=formatted_crowd_quantity,
            stadium=json["stadium"],
            formatted_stadium_capacity=formatted_stadium_capacity,
            season_year=json["season_year"],
            season_matches_data=json["season_matches_data"],
            competition_data=json["competition_data"],
            current_matches_data=json["current_matches_data"],
            url="{{ url_for('static', path='/style.css') }}",
            team_crest_url=teams_crest_url[json["name"]]
        )

        with open("src/view_pages/report/report.html", "w", encoding="utf-8") as output_file:
            output_file.write(html_report)

        print("Json data successfully processed and HTML rendered")
        logging.info("Json data successfully processed and HTML rendered")

    except Exception as e:
        with open("src/view_pages/report/report.html", "w", encoding="utf-8") as output_file:
            output_file.write("Error to process the report, please, reload the page...")

        print(f"Error to process the json data and render the HTML: {e}")
        logging.error(f"Error to process the json data and render the HTML: {e}")
