import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import ObjectId
from src.db_manager.config_db import GetDBCollection

load_dotenv()

class DatabaseManager:
    def __init__(self, collection_name = "child_insights"):
        self.collection = GetDBCollection(collection_name)

    def get_data(self, id):
        _id = ObjectId(id)
        # print(type(_id))
        data = self.collection.find_one({"child_id": _id})
        # print(list(self.collection.find()))
        if data != None:
            return data
        raise ValueError(f"No data found for child_id {id}")
        