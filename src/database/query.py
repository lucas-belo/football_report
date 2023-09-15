from .connection import MongoDbManager


def get_document(database_name, collection_name, nome):
    try:
        client = MongoDbManager.mongodb_connection()
        if client:
            db = client[database_name]
            collection = db[collection_name]
            print("Connected to the database")

            query_criteria = {
                "nome": nome
            } if nome else {}

            document = collection.find_one(query_criteria)

            if document:
                print(document)
                return document
            else:
                print("Document not found.")
                return None
        else:
            print("Failed to connect to the database.")
            return None
    except Exception as e:
        print(e)
        return None
