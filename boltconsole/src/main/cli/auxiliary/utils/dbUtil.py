from bson import ObjectId
from pymongo import MongoClient


class DBUtil:
    def __init__(self):
        self.connection = None
        self.database = None
        self.connect()
        self.init_database()

    def connect(self):
        self.connection = MongoClient("mongodb://localhost:27017/")
        # self.connection = MongoClient(
        #     "mongodb+srv://katsuro:Zi9a44RDSx83jV59@bolt.fnyu7t8.mongodb.net/?retryWrites=true&w=majority")

    def init_database(self):
        self.database = self.connection["bolt"]

    def get_one(self, collection, gfilter):
        collection = self.database[collection]
        return collection.find_one(gfilter)

    def get_all(self, collection):
        data = []
        for item in collection.find():
            data.append(item)
        return data

    def insert(self, collection_name, data):
        collection = self.database[collection_name]
        x = collection.insert_one(data)
        return self.get_one(collection_name, {"_id": x.inserted_id})

    def updates(self, collection, data_id, key, value):
        collection = self.database[collection]
        x = collection.update_one({"_id": ObjectId(data_id)}, {"$set": {key: value}})
        return x
