import logging

from scrapy.http import Response

from logs.logs_setup import setup_logging

setup_logging()


def competitions(response: Response) -> dict:
    """
    This function receives the response from the main spider class request and get the competitions
    (the position in each championship that team is competing)

    :param response: the response from the ogol website
    :return: return the competition data in a dict format
    """

    try:
        official_competitions_div = response.xpath('//div[@class="section" and text()="Competições Oficiais"]')

        competition_data = []

        if official_competitions_div:
            season_divs = official_competitions_div.xpath('//*[@id="page_rightbar"]/div[1]/div/div[2]/div')

            for season_div in season_divs:
                competition_text = season_div.xpath(
                    './/div[@class="competition"]//div[@class="text"]/a/text()'
                ).get()

                number_class = season_div.xpath(
                    './/div[contains(@class, "number")]/text()'
                ).get()

                stat = {
                    "competition": competition_text,
                    "Position": number_class
                }

                competition_data.append(stat)

            if not competition_data:
                competition_data = {
                    "competition": "Sorry, data not available",
                    "Position": "Sorry, data not available"
                }

        else:
            competition_data = {
                "competition": "Sorry, data not available",
                "Position": "Sorry, data not available"
            }
            return competition_data

        print("Competition data was successfully scraped")
        logging.info("Competition data was successfully scraped")
        return competition_data

    except Exception as e:
        competition_data = {
            "competition": "Sorry, data not available",
            "Position": "Sorry, data not available"
        }
        print(f"Error to get the competition data: {e}")
        logging.info(f"Error to get the competition data: {e}")
        return competition_data
