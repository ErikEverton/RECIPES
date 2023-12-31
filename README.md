# RECIPES
#### Video Demo:  <URL HERE>
#### Description:
## Intruduction

This project is a website where the users can share their recipes with the world. On this website you can upload your own recipes,
you can read other people recipes, you can update your recipes if you want to improve them, you can delete them if you want to and 
you can comment in your own recipes or comment in others recipes.

### /recipes/__init__.py

This directory is responsible for creating the app and register the blueprints for authentication and recipes.

### /recipes/auth.py

Here is where all the logic for register and login a user is made.

### /recipes/db.py

Here we connect the application with the database and initialize the database.

### /recipes/recipes.py

Here we do all the logic of the application. We create new recipes, we read the recipes, we update old recipes
and we delete some of them. Here is the logic for the comments too.

### /recipes/templates

All the html files are here.

### /recipes/schema.sql

Here we create all the tables we're going to use.

### /tests

This is directory where the tests are made.

### Prerequisites

Before you run this project you need to install some dependecies.
You can install python on this site: <https://www.python.org/downloads/>
When you install the python, pip will be instaled with it.

#### Instalation guide

-Steps to run the project

Activate the virtual enviroment:
```bash
. .venv/bin/activate
```

Install Flask:
```bash
pip install Flask
```

Run the Flask Application:
```bash
flask --app recipes run
```

Disable the Virtual Environment:
```bash
deactivate
```

### Running tests
You just need to run the next command:
```bash
python -m pytest tests/
```

### Technologies used
* [Flask](https://flask.palletsprojects.com/en/3.0.x/)

### Authors/contributors

**Erik** - did everything - [Erik](https://github.com/ErikEverton)

### License
This project is under **MIT** license - Acess the details - [MIT](https://github.com/MIT)
