#We use Blueprint to create a collection of routes that can be registered later in the main application. This allows for modularizing the application.
from flask import Blueprint, jsonify
from controllers.operations import MongoDBController

# Initialize Blueprint
main = Blueprint('main', __name__)

# Initialize MongoDBController
mongo_controller = MongoDBController()

@main.route('/')
def home():
        return "Hello world"

@main.route('/getNotes', methods=['GET'])
def get_notes_route():
        notes = mongo_controller.get_notes()
        return jsonify(notes) # Return the notes as a JSON response
