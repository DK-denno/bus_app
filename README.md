# [BUS-APP](https://buupasss.herokuapp.com/)
#### By **[Dennis Kamau]**

## Description
This is a simple backend app providing ais for a bus booking service.

## Set Up and Installations

### Prerequisites
1. Ubuntu Software
2. Python3.6 o higher
3. [Postgres](https://www.postgresql.org/download/)
4. [python virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)
5. PIP

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/DK-denno/bus_app.git && cd bus-book`

### Activate virtual environment
Activate virtual environment using python3.6 as default handler
```bash
virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`

### Create the Database
```bash
psql
CREATE DATABASE bus_app;
```
### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'insta'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

[N/B] -> Edit your 'ALLOWED_HOSTS' to add your locahost]

```
### Run initial Migration
```bash
python manage.py makemigrations bus_app
python manage.py migrate
```

### Run the app
```bash
python manage.py runserver
```
Open terminal on `localhost:8000`

## Known bugs
Like and Follow functionality do not work

## Technologies used
    - Python 3.6
    - Django Rest Framework
    - JWT Tokens
    - Heroku
    - Postgresql

## Support and contact details
Contact me on dennisveer27@gmail.com or kamadennis05@gmail.com for any comments, reviews or advice.

### License
Copyright (c) **Dennis Kamau**
