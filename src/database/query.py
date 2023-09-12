from connection import mongodb_connection


def get_document(database_name, collection_name, nome=None):
    try:
        client = mongodb_connection()
        if client:
            db = client[database_name]
            collection = db[collection_name]
            print("Connected to the database")

            query_criteria = {"nome": nome} if nome else {}

            document = collection.find_one(query_criteria)

            if document:
                print(document)
                return document
            else:
                print("Documento não encontrado.")
                return None
        else:
            print("Failed to connect to the database.")
            return None
    except Exception as e:
        print(e)
        return None


get_document("brazil_teams", "serie_a", "Corinthians")