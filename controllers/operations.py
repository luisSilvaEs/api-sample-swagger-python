from controllers.db import MongoDBConnection

database_name='todoappdb'
db = MongoDBConnection(database_name)

class MongoDBController:
    #it is important to send "self" as parameter event when the function does not recieve real args. This is a Flask requisite
    def get_notes(self):
        collection_name='todoappcollection'
        all_notes_from_db = db.get_notes_db(collection_name)
        return all_notes_from_db