# README

API documented using Swangger. This is a simple API running in its own Docker container. The app is built on Pyhton, utilizing:

- **Flask** as framework,
- **request** utility to handle endpoints and
- MongoDB as the database to persist the store the data.

MongoDB runs in its dedicated container and utilizes a volume to persist the data.

The main idea behind this project is only to get familiar with the use of Python as a backend for an API so nothing too fancy si expected. This API is similar to the one built in [NodeJS](https://github.com/luisSilvaEs/api-sample-swagger-documented).

## Documenting creation process

1. Create a new folder for your project, move inside the folder and start a virtual environment for your project running: `python3 -m venv venv`
2. Activate virtual environment: `source venv/bin/activate`
3. Install flask: `pip install requests flask`
4. Copy all the current dependencies of the environment in a new file named requirements.txt That file is used when later reproduce the environment to a different machine. It is the equivalent to the package.json file in NodeJS: `pip freeze > requirements.txt`
5. Create a file named: _main.py_ or _app.py_
6. Backup in Git:
   - `git init`
   - create a gitignore file and add inside the folder _venv/_
