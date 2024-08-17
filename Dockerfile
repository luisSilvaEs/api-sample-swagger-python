# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5005 available to the world outside this container
EXPOSE 5005

# Define environment variable to tell Flask to run in development mode
ENV FLASK_APP=main.py
ENV FLASK_ENV=development

# Docker handles networking and the fact that the Flask application inside the container is bound to 127.0.0.1 (localhost) instead of 0.0.0.0.
# To change that it is necessary to change the host to 0.0.0.0
CMD ["flask", "run", "--host=0.0.0.0"]