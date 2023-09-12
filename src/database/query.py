from connection import mongodb_connection


def get_collection(database_name, collection_name):
    try:
        client = mongodb_connection()
        if client:
            db = client[database_name]
            collection = db[collection_name]
            print("Connected to the database")
            return collection
        else:
            print("Failed to connect to the database.")
            return None
    except Exception as e:
        print(e)
        return None
