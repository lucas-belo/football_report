import logging
import os

from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from logs.logs_setup import setup_logging

load_dotenv()

setup_logging()


class MongoDbManager:
    def __init__(self):
        self.client = None

    @staticmethod
    def mongodb_connection() -> MongoClient:
        """
        Establish a connection to MongoDB.

        :return: A connection to the MongoDB server
        """
        password = os.getenv('MONGODB_PWD')
        uri = f"mongodb+srv://lhbelo:{password}@cluster0.ya4gv31.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        client = MongoClient(uri, server_api=ServerApi('1'))
        try:
            client.admin.command('ping')
            logging.info("Pinged your deployment. You successfully connected to MongoDB!")
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return client
        except Exception as e:
            logging.error(e)
            print(e)

    def mongodb_disconnect(self) -> None:
        """
        Disconnect from the MongoDB server and closes the MongoDB Client.

        :return: None
        """
        if self.client:
            self.client.close()
            print("Disconnected from the database")
            logging.info("Disconnected from the database")
            self.client = None

