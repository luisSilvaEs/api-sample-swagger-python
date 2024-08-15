from flask import Flask
from views.routes import main as main_blueprint

app = Flask(__name__) #name is a "dunder" variable and is a Python speciall variable reserved for interal use

app.register_blueprint(main_blueprint)

# Indicates the name of the module. If the module is run as the main program, it is set to "__main__"
if __name__ == "__main__":
    app.run(debug=True)