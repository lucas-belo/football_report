import os

from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()


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
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return client
        except Exception as e:
            print(e)

    def mongodb_disconnect(self):
        if self.client:
            self.client.close()
            print("Disconnected from the database")
            self.client = None
