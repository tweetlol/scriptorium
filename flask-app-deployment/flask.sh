#!/bin/bash

# CREATE AND ACTIVATE PYTHON VENV
python3 -m venv venv
source venv/bin/activate

# PREPARE NESCESSITIES
pip install flask
mkdir app

echo "
from flask import Flask
app = Flask(__name__)
from app import routes
" > app/__init__.py
echo "
from app import app
" > application-name.py

# MAKE APP/ROUTES.PY FILE
echo "
from flask import render_template
from app import app

# HOME PAGE ROUTE
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Flask webapp at access point /index')
" > app/routes.py

# MAKE APP/TEMPLATES/INDEX.HTML FILE
mkdir -p app/templates

echo '
<!doctype html>
<html>
    <head>
        <title>application-name.py</title>
    </head>
    <body>
        <h1>Hello, world!</h1>
        <p>{{title}}</p>
    </body>
</html>
' > app/templates/index.html

flask run --debug
