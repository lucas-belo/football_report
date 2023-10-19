import logging

from scrapy.http import Response

from logs.logs_setup import setup_logging

setup_logging()


def season_summary(response: Response) -> dict:
    """
    This function receives the response from the main spider class request and get the current season matches data
    (the matches, wins, draws, loses, and goals in each championship)

    :param response: the response from the ogol website
    :return: the season matches summary data in a dict format
    """
    try:
        table_rows = response.xpath(
            '//div[@id="entity_season"]/table/tbody/tr'
        )

        matches_data = []

        for index, row in enumerate(table_rows):
            competition = row.xpath('.//td[1]//a/text()').get()
            matches_played = row.xpath('.//td[2]/text()').get()
            wins = row.xpath('.//td[3]/text()').get()
            draws = row.xpath('.//td[4]/text()').get()
            losses = row.xpath('.//td[5]/text()').get()
            goals = row.xpath('.//td[6]/text()').get()

            if index == len(table_rows) - 1:
                competition = "Total"

            stat = {
                "competition": competition,
                "matches_played": matches_played,
                "wins": wins,
                "draws": draws,
                "losses": losses,
                "goals": goals
            }
            matches_data.append(stat)

        if not matches_data:
            matches_data = {
                "competition": "Sorry, data not available",
                "matches_played": "Sorry, data not available",
                "wins": "Sorry, data not available",
                "draws": "Sorry, data not available",
                "losses": "Sorry, data not available",
                "goals": "Sorry, data not available"
            }

        print("Season Matches Data was successfully scraped")
        logging.info("Season Matches Data was successfully scraped")
        return matches_data

    except Exception as e:
        matches_data = {
            "competition": "Sorry, data not available",
            "matches_played": "Sorry, data not available",
            "wins": "Sorry, data not available",
            "draws": "Sorry, data not available",
            "losses": "Sorry, data not available",
            "goals": "Sorry, data not available"
        }
        print(f"Error to get season matches data: {e}")
        logging.error(f"Error to get season matches data: {e}")
        return matches_data
