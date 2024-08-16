from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, db_name, host='mongodb://localhost', port=27017):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]

    def get_notes_db(self, collection_name):
        return self.db[collection_name]#returns a collection (array)

    def add_notes_db(self, collection_name, new_note_description):
        collection = self.get_notes_db(collection_name)
        num_of_docs = collection.count_documents({})
        # Create the new note
        new_note = {
            'id': str(num_of_docs + 1),
            'description': new_note_description
        }

        result = collection.insert_one(new_note)
        return result.inserted_id

    def delete_note_by_id(self, collection_name, note_id):
        collection = self.get_notes_db(collection_name)
        result = collection.delete_one({'id': note_id})
        return result.deleted_count
    