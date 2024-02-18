# PYTHON FLASK WEB APPLICATION

deploys a skeleton web app framework in Flask

either follow steps manually, or run [flask.sh](https://github.com/tweetlol/scriptorium/blob/main/flask-app-deployment/flask.sh)

## creating the files and python virtual enviroment

- create a python virtual enviroment:

```sh
python3 -m venv venv
```

- activate the created virtual enviroment:

```sh
source venv/bin/activate
```

- you should see your virtual enviroment's name to the left of prompt
- you can deactivate the virtual enviroment with `deactivate`
- install flask in your virtual enviroment:

```sh
pip install flask
```

- the application will exist in a package:
- a subdirectory that includes a \_\_init\_\_.py file is considered a package, and can be imported
- create a directory for a package and the \_\_init\_\_.py file:

```sh
mkdir app
echo "
from flask import Flask

app = Flask(__name__)

from app import routes
" > app/__init__.py
```

- handlers for the application routes are written as Python functions, called view functions
- view functions are mapped to one or more route URLs so that Flask knows what logic to execute when a client requests a given URL
- create module app/routes.py and add a first view function (home page route):

```sh
echo "
from flask import render_template
from app import app

# HOME PAGE ROUTE
@app.route('/')
def landing():
    return 'Hello world string!'

@app.route('/index')
def index():
    return render_template('index.html', title='Home at /index')

" > app/routes.py
```

- there are two decorators, which associate the URLs / and /index to this function
- to complete the application, you need to have a Python script at the top-level that defines the Flask application instance
- create application-name.py, and define it as a single line that imports the application instance:

```sh
echo "
from app import app
" > application-name.py
```

- statement imports the app variable that is a member of the app package
- run the app:

```sh
flask run --debug
```

- choosing the `--debug` option makes changes to files update while Flask is running
- the app can be accessed at [localhost:5000](http://127.0.0.1:5000) by default

## html templates

- prepare a folder for template HTML files
- prepare HTML files to deliver as outputs of view functions
- use jinja for logic in html documents

```sh
mkdir -p app/templates;
echo '
<!doctype html>
<html>
    <head>
        <title>application-name.py</title>
    </head>
    <body>
        <h1>Hello, world!</h1>
        <p>This is {{title}}</p>
    </body>
</html>
' > app/templates/index.html
```

- with argument placeholder {{title}} to be replaced at render
- HTML template will be returned when you call the corresponding view function from `app/routes.py`:

```py
@app.route('/index')
def index():
    return render_template('index.html', title='Home at /index')
```
