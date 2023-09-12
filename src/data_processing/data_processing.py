import json

json1 = {
  "name": "Corinthians",
  "state": "São Paulo",
  "stadium_name": "Neo Química Arena",
  "founding_year": 1910,
  "titles": {
    "international": [
      {
        "competition": "Copa Libertadores",
        "quantity": 1,
        "years": [2012]
      },
      {
        "competition": "Mundial de Clubes",
        "quantity": 2,
        "years": [2000, 2012]
      },
      {
        "competition": "Recopa Sul-Americana",
        "quantity": 1,
        "years": [2013]
      }
    ],
    "national": [
      {
        "competition": "Campeonato Brasileiro",
        "quantity": 7,
        "years": [1990, 1998, 1999, 2005, 2011, 2015, 2017]
      },
      {
        "competition": "Copa do Brasil",
        "quantity": 3,
        "years": [1995, 2002, 2009]
      }
    ],
    "regional": [
      {
        "competition": "Campeonato Paulista",
        "quantity": 30,
        "years": [
          1914, 1916, 1922, 1923, 1924, 1928, 1929, 1930, 1937, 1938, 1939, 1941,
          1951, 1952, 1954, 1977, 1979, 1982, 1983, 1988, 1995, 1997, 1999, 2001,
          2003, 2009, 2013, 2017, 2018, 2019
        ]
      }
    ]
  },
  "relegation": [
    {
      "competition": "Campeonato Brasileiro",
      "quantity": 1,
      "years": [2007]
    }
  ],
  "crowd": {
    "quantity": 30000000,
    "main_organized_crowd": "Gaviões da fiel"
  },
  "stadium": {
    "name": "Neo Química Arena",
    "capacity": 49205,
    "location": "São Paulo, SP"
  }
}

json2 = {"season_year": "2023", "season_matches_data": [{"competition": "Copa Sul-Americana", "matches_played": "6", "wins": "4", "draws": "1", "losses": "1", "goals": "6-3"}, {"competition": "Libertadores", "matches_played": "6", "wins": "2", "draws": "1", "losses": "3", "goals": "7-6"}, {"competition": "Brasileirão", "matches_played": "21", "wins": "6", "draws": "8", "losses": "7", "goals": "22-23"}, {"competition": "Copa do Brasil", "matches_played": "8", "wins": "4", "draws": "0", "losses": "4", "goals": "9-10"}, {"competition": "Campeonato Paulista ", "matches_played": "13", "wins": "6", "draws": "5", "losses": "2", "goals": "20-11"}, {"competition": "Total", "matches_played": "54", "wins": "22", "draws": "15", "losses": "17", "goals": "64-53"}], "competition_data": [{"competition": "Campeonato Paulista 2023", "Position": "QF"}, {"competition": "Campeonato Brasileiro 2023", "Position": "13º"}, {"competition": "Copa do Brasil 2023", "Position": "SF"}, {"competition": "Copa Sul-Americana 2023", "Position": "SF"}, {"competition": "Copa Libertadores 2023", "Position": "FG"}], "current_matches_data": [{"date": "23/09", "hour": "18:30", "league": "D1", "home_team": "Corinthians", "score_vs": "vs", "away_team": "Grêmio"}, {"date": "22/09", "hour": "20:00", "league": "D1", "home_team": "Corinthians", "score_vs": "vs", "away_team": "Botafogo"}, {"date": "14/09", "hour": "19:00", "league": "D1", "home_team": "Fortaleza", "score_vs": "vs", "away_team": "Corinthians"}, {"date": "03/09", "hour": "16:00", "league": "D1", "home_team": "Corinthians", "score_vs": "0-0", "away_team": "Palmeiras"}, {"date": "29/08", "hour": "21:30", "league": "CS", "home_team": "Estudiantes", "score_vs": "1-0", "away_team": "Corinthians"}, {"date": "26/08", "hour": "21:00", "league": "D1", "home_team": "Corinthians", "score_vs": "1-1", "away_team": "Goiás"}]}


def json_formatter(json1, json2):
    combined_json = {**json1, **json2}
    combined_json_str = json.dumps(combined_json, indent=2, ensure_ascii=False)
    print(combined_json_str)


json_formatter(json1, json2)
