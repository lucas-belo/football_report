def competitions(response):
    try:
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

            if not competition_data:
                competition_data = "Os dados das competições desse time não foram encontrados..."

            return competition_data
        else:
            competition_data = "Os dados das competições desse time não foram encontrados..."
            return competition_data

    except Exception as e:
        competition_data = "Os dados das competições desse time não foram encontrados..."
        print(f"Error to get the competition data: {e}")
        return competition_data