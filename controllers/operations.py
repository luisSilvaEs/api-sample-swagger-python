from controllers.db import MongoDBConnection

database_name='todoappdb'
db = MongoDBConnection(database_name)

class MongoDBController:
    #it is important to send "self" as parameter event when the function does not recieve real args. This is a Flask requisite
    def get_notes(self):
        collection_name='todoappcollection'
        collection = db.get_notes_db(collection_name) #function returns a collection/array
        all_notes_from_db = list(collection.find({}, {"_id": 0})) # Retrieve all notes, exclude the `_id` field
        #The find() method retrieves documents from the collection, and {"_id": 0} in the projection specifies that the _id field should be excluded from the results.
        return all_notes_from_db