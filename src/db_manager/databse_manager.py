import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import ObjectId

load_dotenv()

class DatabaseManager:
    def __init__(self):
        uri = os.environ.get("MONGO_URI")
        self.collection = MongoClient(uri)['arthuloo']['child_insights']

    def get_data(self):
        # data = self.collection.find_one({"child_id": child_id})
        self.collection.insert_one({"child_id": '123', "name": "John Doe", "age": 10})
        data = self.collection.find_one({"child_id": '1234'})
        # print(list(self.collection.find()))
        return data