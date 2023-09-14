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
    {"season_year": "2023", "season_matches_data": [{"competition": "Libertadores", "matches_played": "10", "wins": "7", "draws": "2", "losses": "1", "goals": "21-6"}, {"competition": "Brasileirão", "matches_played": "22", "wins": "11", "draws": "8", "losses": "3", "goals": "37-17"}, {"competition": "Supercopa Brasil", "matches_played": "1", "wins": "1", "draws": "0", "losses": "0", "goals": "4-3"}, {"competition": "Copa do Brasil", "matches_played": "6", "wins": "2", "draws": "1", "losses": "3", "goals": "9-7"}, {"competition": "Campeonato Paulista ", "matches_played": "16", "wins": "11", "draws": "4", "losses": "1", "goals": "25-7"}, {"competition": "Total", "matches_played": "55", "wins": "32", "draws": "15", "losses": "8", "goals": "96-40"}], "competition_data": [{"competition": "Campeonato Paulista 2023", "Position": "1.º"}, {"competition": "Campeonato Brasileiro 2023", "Position": "2º"}, {"competition": "Supercopa do Brasil 2023", "Position": "1.º"}, {"competition": "Copa do Brasil 2023", "Position": "QF"}, {"competition": "Copa Libertadores 2023", "Position": "SF"}], "current_matches_data": [{"date": "20/09", "hour": "19:00", "league": "D1", "home_team": "Grêmio", "score_vs": "vs", "away_team": "Palmeiras"}, {"date": "19/09", "hour": "19:00", "league": "D1", "home_team": "Red Bull Bragantino", "score_vs": "vs", "away_team": "Palmeiras"}, {"date": "15/09", "hour": "21:30", "league": "D1", "home_team": "Palmeiras", "score_vs": "vs", "away_team": "Goiás"}, {"date": "03/09", "hour": "16:00", "league": "D1", "home_team": "Corinthians", "score_vs": "0-0", "away_team": "Palmeiras"}, {"date": "30/08", "hour": "21:30", "league": "CL", "home_team": null, "score_vs": "0-0", "away_team": "Deportivo Pereira"}, {"date": "27/08", "hour": "18:30", "league": "D1", "home_team": "Palmeiras", "score_vs": "1-0", "away_team": "Vasco"}]}
    '''

    format_json(input_json)