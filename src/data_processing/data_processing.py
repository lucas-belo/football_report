from jinja2 import Template


def data_processing(json, template_html_file):
    with open(template_html_file, "r", encoding="utf-8") as file:
        template_html = file.read()
    template = Template(template_html)

    html_relatorio = template.render(
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
        output_file.write(html_relatorio)
