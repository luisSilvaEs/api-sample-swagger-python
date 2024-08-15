from flask import Flask, request

app = Flask(__name__) #name is a "dunder" variable and is a Python speciall variable reserved for interal use

class Notes():
    @app.route("/")
    def get():
        return "Hello world"


# Indicates the name of the module. If the module is run as the main program, it is set to "__main__"
if __name__ == "__main__":
    app.run(debug=True)