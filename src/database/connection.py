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
    def mongodb_connection():
        password = os.getenv('MONGODB_PWD')
        uri = f"mongodb+srv://lhbelo:{password}@cluster0.rismkis.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(uri, server_api=ServerApi('1'))
        try:
            client.admin.command('ping')
            logging.info("Pinged your deployment. You successfully connected to MongoDB!")
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return client
        except Exception as e:
            logging.error(e)
            print(e)

    def mongodb_disconnect(self):
        if self.client:
            self.client.close()
            print("Disconnected from the database")
            logging.info("Disconnected from the database")
            self.client = None

