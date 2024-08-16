from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from views.routes import main as main_blueprint
import os

app = Flask(__name__) #name is a "dunder" variable and is a Python speciall variable reserved for interal use

# Register my Blueprint routes
app.register_blueprint(main_blueprint)

# Swagger configuration
SWAGGER_URL = '/swagger'  # URL for accessing Swagger UI
API_URL = '/swagger.yaml'  # Path to the Swagger YAML file

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI endpoint
    API_URL,  
    config={  # Swagger UI config overrides
        'app_name': "ToDo App API"
    }
)

# Register the Swagger UI blueprint
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Serve the swagger.yaml file
@app.route('/swagger.yaml')
def swagger_yaml_file():
    return send_from_directory(os.path.abspath(os.path.dirname(__file__)), 'swagger.yaml')

# Indicates the name of the module. If the module is run as the main program, it is set to "__main__"
if __name__ == "__main__":
    app.run(debug=True)