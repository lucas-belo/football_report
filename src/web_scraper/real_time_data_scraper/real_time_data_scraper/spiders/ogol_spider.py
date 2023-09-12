import scrapy

from ..utils import teams_urls


class OgolSpiderSpider(scrapy.Spider):
    name = "ogol_spider"
    allowed_domains = ["www.ogol.com.br"]
    start_urls = [teams_urls.teams_urls["Corinthians"]]

    def parse(self, response):
        season_year = response.xpath('//*[@id="page_rightbar"]/div[1]/div[1]/text()').get()
        season_summary = response.xpath('//*[@id="page_main"]/div[1]/h2/text()').get()
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

        yield {
            "season_year": season_year,
            "season_summary": season_summary,
            "season_matches_data": matches_data
        }
