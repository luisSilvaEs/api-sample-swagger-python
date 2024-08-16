from controllers.db import MongoDBConnection
from pymongo import errors
from flask import request, jsonify

database_name='todoappdb'
db = MongoDBConnection(database_name)
collection_name='todoappcollection'

class MongoDBController:
    #it is important to send "self" as parameter event when the function does not recieve real args. This is a Flask requisite
    def get_notes(self):
        collection = db.get_notes_db(collection_name) #function returns a collection/array
        all_notes_from_db = list(collection.find({}, {"_id": 0})) # Retrieve all notes, exclude the `_id` field
        #The find() method retrieves documents from the collection, and {"_id": 0} in the projection specifies that the _id field should be excluded from the results.
        return all_notes_from_db

    def add_notes(self):
        
        new_note_description = request.json['newNotes']
        
        try:
            # Perform the insert operation
            inserted_note_id = db.add_notes_db(collection_name, new_note_description)

            if inserted_note_id:
                return jsonify("Added Successfully"), 201
            else:
                return jsonify("Failed to add the note"), 500

        except errors.PyMongoError as e:
            # Catch any PyMongo-specific errors
            return jsonify(f"An error occurred: {str(e)}"), 500

        except Exception as e:
            # Catch any other exceptions
            return jsonify(f"An unexpected error occurred: {str(e)}"), 500

    
    def delete_notes(self):
        try:
            note_id = request.args.get('id')
            
            # Perform the delete operation
            deleted_count = db.delete_note_by_id(collection_name, note_id)

            if deleted_count == 1:
                return jsonify("Deleted Successfully"), 200
            else:
                return jsonify("No note found with the specified ID"), 404 

        except errors.PyMongoError as e:
            # Catch any PyMongo-specific errors
            return jsonify(f"An error occurred: {str(e)}"), 500

        except Exception as e:
            # Catch any other exceptions
            return jsonify(f"An unexpected error occurred: {str(e)}"), 500