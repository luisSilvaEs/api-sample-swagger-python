from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, db_name, host='mongodb://localhost', port=27017):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]

    def get_notes_db(self, collection_name):
        return self.db[collection_name]#returns a collection (array)