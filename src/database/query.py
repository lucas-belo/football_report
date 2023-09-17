import logging

from .connection import MongoDbManager

from logs.logs_setup import setup_logging

setup_logging()


def get_document(database_name, collection_name, nome):
    try:
        client = MongoDbManager.mongodb_connection()
        if client:
            db = client[database_name]
            collection = db[collection_name]
            logging.info("Connected to the database")
            print("Connected to the database")

            query_criteria = {
                "name": nome
            } if nome else {}

            document = collection.find_one(query_criteria)

            if document:
                return document
            else:
                print("Document not found.")
                logging.warning("Document not found.")
                return None
        else:
            print("Failed to connect to the database in the query module.")
            logging.error("Failed to connect to the database in the query module.")
            return None

    except Exception as e:
        print(f"Error to get document: {e}")
        logging.error(f"Error to get document: {e}")
        return None
