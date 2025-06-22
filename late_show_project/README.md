Late Show API Challenge
A Flask REST API for managing a Late Night TV show system, built with MVC architecture, PostgreSQL, JWT authentication, and tested with Postman.
Setup Instructions
Prerequisites

Python 3.8+
PostgreSQL
Git
Postman
Pipenv

Installation

Clone the repository:

git clone https://github.com/<username>/late-show-api-challenge.git
cd late-show-api-challenge


Install dependencies:

pipenv install
pipenv shell


Set up PostgreSQL:

CREATE DATABASE late_show_db;


Configure environment variables in .env:

DATABASE_URL=postgresql://<user>:<password>@localhost:5432/late_show_db
JWT_SECRET_KEY=your-secret-key


Initialize the database:

export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade


Seed the database:

python server/seed.py

Running the Application
export FLASK_APP=server/app.py
flask run

Authentication Flow

Register a user:
POST /register with { "username": "your_username", "password": "your_password" }


Login to get JWT:
POST /login with { "username": "your_username", "password": "your_password" }


Use the returned access_token in protected routes:
Add header: Authorization: Bearer <token>



API Routes



Route
Method
Auth Required
Description



/register
POST
No
Register a new user


/login
POST
No
Login and get JWT token


/episodes
GET
No
List all episodes


/episodes/<id>
GET
No
Get episode details with appearances


/episodes/<id>
DELETE
Yes
Delete episode and its appearances


/guests
GET
No
List all guests


/appearances
POST
Yes
Create a new appearance


Sample Request/Response
POST /register
Request:
{
    "username": "testuser",
    "password": "testpass"
}

Response:
{
    "message": "User registered successfully"
}

POST /appearances
Request:
{
    "rating": 4,
    "guest_id": 1,
    "episode_id": 1
}

Headers:
Authorization: Bearer <token>

Response:
{
    "id": 1,
    "rating": 4,
    "guest_id": 1,
    "episode_id": 1
}

Postman Testing

Import challenge-4-lateshow.postman_collection.json into Postman.
Test the following:
Register a user
Login to get token
Use token in protected routes (POST /appearances, DELETE /episodes/<id>)


Ensure all routes return expected status codes and data.

GitHub Repository
https://github.com//late-show-api-challenge
Project Structure
.
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
│   │   └── user.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
│   │   └── auth_controller.py
├── migrations/
├── challenge-4-lateshow.postman_collection.json
└── README.md
