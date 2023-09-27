from src.database.query import get_document


def test_get_document():
    database_name = "brazil_teams"
    collection_name = "serie_a"
    name = "Sport Club Corinthians Paulista"

    result = get_document(database_name, collection_name, name)

    assert result is not None
