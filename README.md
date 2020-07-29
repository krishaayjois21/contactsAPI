# Contacts API

This is my first Rest API using the flask-restful framework. This uses Google Firebase as the database.

Prerequistes
 - Google Account
 - [Python 3](https://www.python.org/)
 - [Docker](https://www.docker.com/) and Docker Compose (Optional , needed to run API in a docker container)

Get Started
 
 - Clone the repo with git: `git clone https://github.com/krishaayjois21/contactsAPI.git`
 - Go into the project root `cd contactsAPI`
 - Install dependencies `pip install -r requirements.txt`
 - Setup a [Google Firebase](https://firebase.google.com) project
 - Create credentials for the service account on the cloud console
 - After downloading the credentials file rename it to `credentials.json`
 - Move the credentials file into the `firebaseInit` folder

Run the API
 - Before you run the API , check if you are OK with the ports the API runs on 
 - To run the API use: `python run.py`
 - To run it a docker container: `docker-compose up`

### Read the [documentation](https://github.com/krishaayjois21/contactsAPI/blob/master/docs/documentation.md)
