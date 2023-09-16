from src.database.connection import MongoDbManager


def test_database_connection():
    manager = MongoDbManager()

    client = manager.mongodb_connection()
    assert client is not None

    manager.mongodb_disconnect()


def test_database_disconnection():
    manager = MongoDbManager()

    client = manager.mongodb_connection()
    manager.mongodb_disconnect()

    assert manager.client is None

