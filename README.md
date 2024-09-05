# Todo List API

A RESTful API for managing a to-do list.

## Description

This Python application provides a RESTful API for managing a to-do list. It allows users to create, read, update, and delete (CRUD) tasks.

## Getting Started

### Dependencies

- Python 3.x
- Flask
- Flask Migrate
- Flask SQLAlchemy
- Flask-SMOREST
- Marshmallow
- Pydantic
- Alembic
- Swagger
- PostgreSQL

### Installing

- Clone the repository:

```
git clone https://github.com/ryanitj/todolist-api
```

- Create a virtual environment:

```
.venv\Scripts\activate # On MAC: source venv/bin/activate
```

- Install dependencies:

```
pip install -r requirements.txt
```

- Configuration:
  Create a .env file in the project root directory and add your environment variables, follow an example below:

```
DB_PORT=5432
DB_URL=postgresql://postgres:postgres@localhost
DB_NAME=postgres

API_KEY=<YOUR_API_KEY>
```

### Executing program

- Create the database:

```
flask db init
flask db migrate
flask db upgrade
```

- Run the application:

```
flask run
```

## Authors

Contributors names and contact info

Ryan Coelho  
[Linkedin](https://www.linkedin.com/in/ryan-coelho-217b11200/)
