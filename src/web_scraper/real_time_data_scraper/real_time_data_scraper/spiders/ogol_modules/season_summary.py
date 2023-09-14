def season_summary(response):
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
            matches_data = "Os dados das partidas desse time não foram encontrados..."

        return matches_data

    except Exception as e:
        matches_data = "Os dados das partidas desse time não foram encontrados..."
        print(f"Error to get matches_data: {e}")
        return matches_data
