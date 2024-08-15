#We use Blueprint to create a collection of routes that can be registered later in the main application. This allows for modularizing the application.
from flask import Blueprint, jsonify, request
from controllers.operations import get_notes

# Initialize Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
        return "Hello world"

@main.route('/getNotes', methods=['GET'])
def get_notes_route():
        notes = get_notes()
        return notes
