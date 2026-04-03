import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

def GetDBCollection(collection_name):
    uri = os.environ.get("MONGO_URI")
    client = MongoClient(uri)
    db = client['arthuloo']
    collection = db[collection_name]
    return collection

