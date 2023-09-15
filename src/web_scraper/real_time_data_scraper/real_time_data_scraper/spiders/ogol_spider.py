import scrapy


from ..utils import teams_urls

from .ogol_modules import (
    season_summary,
    competitions,
    previous_and_next_games
                           )


class OgolSpiderSpider(scrapy.Spider):
    name = "ogol_spider"
    allowed_domains = ["www.ogol.com.br"]

    def __init__(self, team_name=None, *args, **kwargs):
        super(OgolSpiderSpider, self).__init__(*args, **kwargs)
        self.team_name = team_name
        if self.team_name:
            self.start_urls = [teams_urls.teams_urls.get(self.team_name)]

    # start_urls = [teams_urls.teams_urls["Ituano"]]

    def parse(self, response):

        # Season year

        season_year = response.xpath('//*[@id="page_rightbar"]/div[1]/div[1]/text()').get()

        if season_year.isnumeric():
            pass
        else:
            season_year = "Temporada atual não encontrada"

        # Season summary

        matches_data = season_summary.season_summary(response)

        # Competitions

        competition_data = competitions.competitions(response)

        # Previous and next games

        current_matches_data = previous_and_next_games.previous_and_next_games(response)

        yield {
            "season_year": season_year,
            "season_matches_data": matches_data,
            "competition_data": competition_data,
            "current_matches_data": current_matches_data
        }

        result = {
            "season_year": season_year,
            "season_matches_data": matches_data,
            "competition_data": competition_data,
            "current_matches_data": current_matches_data
        }

        return result
