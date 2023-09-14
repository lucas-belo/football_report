def previous_and_next_games(response):
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

            score_vs = row.xpath('.//td[6]/a/text()').get()
            away_team = row.xpath('.//td[7]/a/text()').get()

            if away_team is None:
                away_team = row.xpath('.//td[7]/a/b/text()').get()
                if away_team is None:
                    away_team = row.xpath('.//td[7]/div/div[2]/a/text()').get()

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
            current_matches_data = "Os dados dos jogos anteriores e próximos desse time não foram encontrados..."

        return current_matches_data
    except Exception as e:
        current_matches_data = "Os dados das partidas anteriores e próximas desse time não foram encontrados..."
        print(f"Error to get the current_matches_data data: {e}")
        return current_matches_data
