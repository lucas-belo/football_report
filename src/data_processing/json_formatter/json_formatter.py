import json


def format_json(input_json):
    try:
        data = json.loads(input_json)

        formatted_json = json.dumps(data, indent=4, ensure_ascii=False)

        with open('data.json', 'w', encoding='utf-8') as output_file:
            output_file.write(formatted_json)

        print("JSON saved on 'data.json'")
    except json.JSONDecodeError as e:
        print("Error to analise the json:", e)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    input_json = '''
{"season_year": "2023/24", "season_matches_data": [{"competition": "Supercopa Europeia", "matches_played": "1", "wins": "0", "draws": "1", "losses": "0", "goals": "1-1"}, {"competition": "Liga dos Campe\u00f5es", "matches_played": "2", "wins": "2", "draws": "0", "losses": "0", "goals": "6-2"}, {"competition": "Liga Inglesa", "matches_played": "8", "wins": "6", "draws": "0", "losses": "2", "goals": "17-6"}, {"competition": "SuperCopa Inglaterra", "matches_played": "1", "wins": "0", "draws": "1", "losses": "0", "goals": "1-1"}, {"competition": "Copa da Liga", "matches_played": "1", "wins": "0", "draws": "0", "losses": "1", "goals": "0-1"}, {"competition": "Total", "matches_played": "13", "wins": "8", "draws": "2", "losses": "3", "goals": "25-11"}], "competition_data": [{"competition": "Liga Inglesa 2023/24", "Position": "3\u00ba"}, {"competition": "Supercopa - Inglaterra 2023", "Position": "2.\u00aa"}, {"competition": "Copa da Liga 2023/24", "Position": "3R"}, {"competition": "Supercopa Europeia 2023", "Position": "1.\u00ba"}, {"competition": "Liga dos Campe\u00f5es 2023/24", "Position": "FG"}], "current_matches_data": [{"date": "29/10", "hour": "12:30", "league": "PL", "home_team": "Manchester United", "score_vs": "vs", "away_team": "Manchester City"}, {"date": "25/10", "hour": "16:00", "league": "LC", "home_team": "Young Boys", "score_vs": "vs", "away_team": "Manchester City"}, {"date": "21/10", "hour": "11:00", "league": "PL", "home_team": "Manchester City", "score_vs": "vs", "away_team": "Brighton & Hove Albion"}, {"date": "08/10", "hour": "12:30", "league": "PL", "home_team": "Arsenal", "score_vs": "1-0", "away_team": "Manchester City"}, {"date": "04/10", "hour": "16:00", "league": "LC", "home_team": "RB Leipzig", "score_vs": "1-3", "away_team": "Manchester City"}, {"date": "30/09", "hour": "11:00", "league": "PL", "home_team": "Wolverhampton", "score_vs": "2-1", "away_team": "Manchester City"}]}
    '''

    format_json(input_json)
