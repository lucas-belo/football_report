import scrapy

from ..utils import teams_urls


class OgolSpiderSpider(scrapy.Spider):
    name = "ogol_spider"
    allowed_domains = ["www.ogol.com.br"]
    start_urls = [teams_urls.teams_urls["Corinthians"]]

    def parse(self, response):
        season_year = response.xpath('//*[@id="page_rightbar"]/div[1]/div[1]/text()').get()

        # Season summary

        table_rows = response.xpath('//div[@id="entity_season"]/table/tbody/tr')

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

        # Competitions

        official_competitions_div = response.xpath('//div[@class="section" and text()="Competições Oficiais"]')

        competition_data = []

        if official_competitions_div:
            season_divs = official_competitions_div.xpath('//*[@id="page_rightbar"]/div[1]/div[2]/div[2]/div')

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

        # Previous and next games

        table_rows = response.xpath('//div[@id="team_games"]/table/tbody/tr')

        current_matches_data = []

        for index, row in enumerate(table_rows):
            date = row.xpath('.//td[2]/text()').get()
            hour = row.xpath('.//td[3]/text()').get()
            league = row.xpath('.//td[4]/div/div[2]/a/text()').get()
            home_team = row.xpath('.//td[5]/a/text()').get()
            score_vs = row.xpath('.//td[6]/a/text()').get()
            away_team = row.xpath('.//td[7]/a/text()').get()

            stat = {
                "date": date,
                "hour": hour,
                "league": league,
                "home_team": home_team,
                "score_vs": score_vs,
                "away_team": away_team
            }

            current_matches_data.append(stat)

        yield {
            "season_year": season_year,
            "season_matches_data": matches_data,
            "competition_data": competition_data,
            "current_matches_data": current_matches_data
        }
