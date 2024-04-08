import logging

from scrapy.http import Response

from logs.logs_setup import setup_logging

setup_logging()


def previous_and_next_games(response: Response) -> list[dict]:
    """
    This function receives the response from the main spider class request and get the previous and next matches data
    (the 3 previous and 3 next matches of the team)

    :param response: the response from the ogol website
    :return: the previous and next games data in a dict format
    """
    try:

        table_rows = response.xpath('//div[@id="team_games"]/table/tbody/tr')

        current_matches_data = []

        for index, row in enumerate(table_rows):
            date = row.xpath('.//td[2]/text()').get()
            hour = row.xpath('.//td[3]/text()').get()
            league = row.xpath('.//td[4]/div/div[2]/a/text()').get()
            home_team = row.xpath('.//td[5]/a/text()').get()

            if home_team is None:
                home_team = row.xpath('.//td[5]/a/b/text()').get()
                if home_team is None:
                    home_team = row.xpath('.//td[5]/div/div[1]/a/b/text()').get()
                    if home_team is None:
                        home_team = row.xpath('.//td[5]/div/div[1]/a/text()').get()

            score_vs = row.xpath('.//td[7]/a/text()').get()
            if score_vs is None:
                score_vs = f"{row.xpath('.//td[7]/a/div[12]/text()').get()} - Em andamento"

            away_team = row.xpath('.//td[9]/a/text()').get()

            if away_team is None:
                away_team = row.xpath('.//td[9]/a/b/text()').get()
                if away_team is None:
                    away_team = row.xpath('.//td[9]/div/div[2]/a/text()').get()
                    if away_team is None:
                        away_team = row.xpath('//*[@id="9574525"]/td[9]/div/div[2]/a/b/text()').get()

            stat = {
                "date": date,
                "hour": hour,
                "league": league,
                "home_team": home_team,
                "score_vs": score_vs,
                "away_team": away_team
            }

            current_matches_data.append(stat)

        if not current_matches_data:
            current_matches_data = [{
                "date": "Sorry, data not available",
                "hour": "Sorry, data not available",
                "league": "Sorry, data not available",
                "home_team": "Sorry, data not available",
                "score_vs": "Sorry, data not available",
                "away_team": "Sorry, data not available"
            }]

        print("Current Matches Data was successfully scraped!")
        logging.info("Current Matches Data was successfully scraped!")
        return current_matches_data
    except Exception as e:
        current_matches_data = [{
            "date": "Sorry, data not available",
            "hour": "Sorry, data not available",
            "league": "Sorry, data not available",
            "home_team": "Sorry, data not available",
            "score_vs": "Sorry, data not available",
            "away_team": "Sorry, data not available"
        }]
        print(f"Error to get the Current Matches Data: {e}")
        logging.error(f"Error to get the Current Matches Data: {e}")
        return current_matches_data
