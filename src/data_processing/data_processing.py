import logging

from jinja2 import Template

from logs.logs_setup import setup_logging

setup_logging()


def data_processing(json, template_html_file):
    try:
        with open(template_html_file, "r", encoding="utf-8") as file:
            template_html = file.read()
        template = Template(template_html)

        html_report = template.render(
            team=json["name"],
            state=json["state"],
            stadium_name=json["stadium_name"],
            founding_year=json["founding_year"],
            titles=json["titles"],
            relegation=json["relegation"],
            crowd=json["crowd"],
            stadium=json["stadium"],
            season_year=json["season_year"],
            season_matches_data=json["season_matches_data"],
            competition_data=json["competition_data"],
            current_matches_data=json["current_matches_data"]
        )

        with open("src/view_pages/report/report.html", "w", encoding="utf-8") as output_file:
            output_file.write(html_report)

        print("Json data successfully processed and HTML rendered")
        logging.info("Json data successfully processed and HTML rendered")

    except Exception as e:
        print(f"Error to process the json data and render the HTML: {e}")
        logging.error(f"Error to process the json data and render the HTML: {e}")

