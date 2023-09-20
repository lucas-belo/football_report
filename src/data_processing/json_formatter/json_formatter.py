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
{"season_year": "2023", "season_matches_data": [{"competition": "Copa Sul-Americana", "matches_played": "6", "wins": "4", "draws": "1", "losses": "1", "goals": "6-3"}, {"competition": "Libertadores", "matches_played": "6", "wins": "2", "draws": "1", "losses": "3", "goals": "7-6"}, {"competition": "Brasileir\u00e3o", "matches_played": "23", "wins": "6", "draws": "9", "losses": "8", "goals": "27-29"}, {"competition": "Copa do Brasil", "matches_played": "8", "wins": "4", "draws": "0", "losses": "4", "goals": "9-10"}, {"competition": "Campeonato Paulista ", "matches_played": "13", "wins": "6", "draws": "5", "losses": "2", "goals": "20-11"}, {"competition": "Total", "matches_played": "56", "wins": "22", "draws": "16", "losses": "18", "goals": "69-59"}], "competition_data": [{"competition": "Campeonato Paulista 2023", "Position": "QF"}, {"competition": "Campeonato Brasileiro 2023", "Position": "14\u00ba"}, {"competition": "Copa do Brasil 2023", "Position": "SF"}, {"competition": "Copa Sul-Americana 2023", "Position": "SF"}, {"competition": "Copa Libertadores 2023", "Position": "FG"}], "current_matches_data": [{"date": "30/09", "hour": "18:30", "league": "D1", "home_team": "S\u00e3o Paulo", "score_vs": "vs", "away_team": "Corinthians"}, {"date": "26/09", "hour": "21:30", "league": "CS", "home_team": null, "score_vs": "vs", "away_team": "Fortaleza"}, {"date": "22/09", "hour": "20:00", "league": "D1", "home_team": "Corinthians", "score_vs": "vs", "away_team": "Botafogo"}, {"date": "18/09", "hour": "21:00", "league": "D1", "home_team": "Corinthians", "score_vs": "4-4", "away_team": "Gr\u00eamio"}, {"date": "14/09", "hour": "19:00", "league": "D1", "home_team": "Fortaleza", "score_vs": "2-1", "away_team": "Corinthians"}, {"date": "03/09", "hour": "16:00", "league": "D1", "home_team": "Corinthians", "score_vs": "0-0", "away_team": "Palmeiras"}]}
    '''

    format_json(input_json)
