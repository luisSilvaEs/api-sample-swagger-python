# README

API documented using Swagger. This is a simple API running in its own Docker container. The app is built on Pyhton, utilizing:

- **Flask** as framework,
- **request** utility to handle endpoints and
- MongoDB as the database to persist the store the data

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

## Install Swagger

1. Install flask-swagger-ui: `pip install flask flask-swagger-ui`
2. Update requirements.txt file: `pip freeze > requirements.txt`
3. Create a swagger.yaml file that describes your API.
4. Integrate Swagger UI into your Flask app using flask_swagger_ui.
5. Access the Swagger UI at /swagger on your local server.

## Dockerize app

### Create image and initial settings

1. Create _Dockerfile_ and _.dockerignore_ files
2. Dockerfile will have the image to run python, the instruction to move our app in a directory inside the image, expose a port and the command to run the app.
3. dockerignore should contain the venv folder, compiled Python files, cache directories, and environment files when building the Docker image.
4. Build manually the image: `docker build -t api-python-image .`
5. After a few seconds we should get in the screen something as follow in case the building had beeen successfull

```bash
sha256:e15f106a9d34d18363b3ab11c7da6a7d2a77caf4dded0940da9546599cb6dc7e                                          0.0s
 => => naming to docker.io/library/api-python-image                                                                                                0.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/tfybdh9wrkhsm3pkc1dh6midu

What's Next?
  1. Sign in to your Docker account → docker login
  2. View a summary of image vulnerabilities and recommendations → docker scout quickview
```

6. Validate the image had been created: `docker images`

```bash
REPOSITORY                              TAG       IMAGE ID       CREATED              SIZE
api-python-image                       latest    e15f106a9d34   About a minute ago   175MB
```

### Run container from created image

1. Run in your terminal following command: `docker run -ti -p 5005:5000 api-python-image`
2. You should be able to access to the app through the ULR [http://localhost:5005](http://localhost:5005) if working you should
   see in the browser:

```
Hello world
```

also in the terminal you should see the following output

```bash
Serving Flask app 'main.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
```

### Create a docker compose file

1. Create a file named _docker-compose.yaml_
2. The file should have 2 services: one for the app (_flask-app_) and a second for the data base (_mongodb_)

### Create a volume to store the data

1. In the **docker-compose.yaml** file, just add the following volume to the mongodb service

```yaml
volumes: - mongo-data:/data/db: #Creates a Docker volume named mongo-data that is mapped to MongoDB's data directory (/data/db). This ensures that data persists even if the container is stopped or removed.
```

2. Declare a name a volume to persist MongoDB data at the bottom of the file

```yaml
volumes:
  mongo-data:
```

3. Finally build the container using docker compose `docker compose up`

## How to use the start up the app locally(dev)

1. Download the app through this [repository](https://github.com/luisSilvaEs/api-sample-swagger-python)
2. Create a virtual environment to isolate the app's dependencies `python3 -m venv venv`
3. Activate the virtual environment `source venv/bin/activate`
4. Install dependencies `pip install -r requirements.txt`
5. Finally run the app using `python3 main.py` or `flask run`

_WARNING_ since the you might not have MongoDB not the collection locally, only the server might start but nor the app,
therfore the endponints won't work.

## How to start up the app using docker compose (prod)

1. Download the app through this [repository](https://github.com/luisSilvaEs/api-sample-swagger-python)
2. Build the image and start the container `docker compose up`

## Endpoints

- To see Swagger documentation: [http://localhost:5005/swagger](http://localhost:5005/swagger)
- To get all the notes: [http://localhost:5005/getNotes](http://localhost:5005/getNotes)
- To add a new note: [http://localhost:5005/addNotes](http://localhost:5005/addNotes)
- To delete a note: [http://localhost:5005/deleteNotes?id={idNote}](http://localhost:5005/deleteNotes?id={idNote})

_Note_ In local the Base URL change **http://localhost:5005/** for **127.0.0.1:5000/**

### Sample of data

```json
[
  {
    "description": "buy clothes",
    "id": "1"
  },
  {
    "description": "make food",
    "id": "2"
  },
  {
    "description": "feed the dog",
    "id": "4"
  },
  {
    "description": "drink coffee",
    "id": "3"
  }
]
```

## References

- [django-rest-api](https://github.com/techwithtim/django-rest-api/tree/main)
- [Linode-Flask-MongoDB-API](https://github.com/techwithtim/Linode-Flask-MongoDB-API/tree/main)
- [Python API Tutorial: Getting Started with APIs](https://www.dataquest.io/blog/python-api-tutorial/)
- [Python Programs 4: Dockerizing Your Flask API for Seamless Deployments](https://medium.com/@prateekbansalind/python-programs-4-dockerizing-your-flask-api-for-seamless-deployments-28c1842a92cb)
- [Video Create A Python API in 12 Minutes](https://www.youtube.com/watch?v=zsYIw6RXjfM)
- [Video Python REST API Tutorial - Building a Flask REST API](https://www.youtube.com/watch?v=GMppyAPbLYk)
