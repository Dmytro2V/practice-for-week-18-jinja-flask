Introduction To Flask
CAREFUL : some updates:
1. need last flask
2. instead of FLASK_ENV=development variable use flask run --debug.


Introduction to Flask
You are about to begin creating web applications with Python using the power of the Flask framework.

When you finish this lesson, you should be able to:

Setup a new Flask project
Run a simple Flask web application on your computer
Utilize basic configuration on a Flask project
What is Flask
Flask is a package for Python which provides a framework for building web applications. Many additional packages have been created by the Python community to work with Flask to provide rich functionality including html templates, web forms, session management and much more.

Flask handles web server calls using routes to determine the appropriate response.

Benefits of Flask
Here are some of the reasons that development teams chose Flask for their web application.

No rules - Flask allows teams to design their own project structure
Easy to use - Takes only a few lines of code to get started (as you will see)
Can start small then grow huge - There's no limit on how large or complex a Flask application can become
Flask makes no assumptions about database layer (or anything else) - again each development team can choose the database and interfaces that work best for their solution
Get started quickly
A basic Flask application takes only a few lines of code to set up. That means it only takes a few minutes to get started.

Setup
If you want to follow along with the code in this lesson, prepare your system by creating a new folder for your project and cd to that folder in your terminal.

Now begin by installing the Flask package.

pipenv install Flask~=1.1
You can verify that the install worked by checking the version.

pipenv run flask --version
Code
Next, create a new file, e.g. simple.py.

Start the file by importing the flask package

from flask import Flask
To use Flask, you need to provide it with an application name. While it is possible to pass in a string, most experienced developers will instead use the dunder __name__ which will automatically pick up the file name. That means you can easily copy this line from project to project.

app = Flask(__name__)
In order to verify Flask is working properly, you will want a url to load. In Flask that is specified using a decorator before a function that returns the desired content.

@app.route('/')
def hello():
    return '<h1>Hello, world!</h1>'
The path for the route is the parameter passed to the app.route decorator. The function can have any name. The return for a web page will be HTML. For other use cases, such as APIs, you may return other content (JSON, perhaps).

You will dig into routes more extensively in a future lesson. Now, it is time to run your minimalist application and test it with a browser.

If you have been following along, your code in the file simple.py should look like this. (Make sure you've saved it.)

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, world!</h1>'
Run
In order to start a Flask application, you need to first specify which file to use. This is done through the environment variable FLASK_APP. To quickly set an environment variable from the command line, use the export command.

export FLASK_APP=simple.py
If you named your file something other than simple.py, then you will need to adjust the export command accordingly.

Finally, start the application using

pipenv run flask run
When it works correctly, you will see output similar to the following.

 * Serving Flask app "simple.py"  
 * Environment: production  
   WARNING: This is a development server. Do not use it in a production deployment.  
   Use a production WSGI server instead.  
 * Debug mode: off  
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)  
Take the url from the last line http://127.0.0.1:5000/ and put it in your browser (Chrome, Firefox, etc.). You should see the content which was returned from the function associated with the / route.

Bonus: Some terminals will even allow you click the link to open it!

Improve run configuration
If you look carefully, you'll see the output is warning you that Flask thinks the Environment is Production and Debug mode is off. When you are working locally it is very useful to change both of these. And this is easy to do with another environment variables.

In your terminal, enter

export FLASK_ENV=development
To stop the application, follow the instructions provided in the output. That is, hold control and type c on your keyboard.

Then restart Flask and you'll see the output

 * Serving Flask app "simple.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 652-054-387
You will also notice that when you change a file and save it, the change is picked up and flask automatically restarts.

 * Detected change in '/Users/crbmac/projects/flask/simple.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 652-054-387
You may need to refresh the page in your browser to see the change.

Specify a port for Flask
On the off chance you need to run more than one Flask application at a time, you can easily specify a port. The default, as you can see in the url above, is 5000.

If you wanted to use another port, you can add the -p flag to the flask run command.

For example, this will run your application on port 5001

pipenv run flask run -p 5001
You'll see the output change so the last line includes this new port and, of course, that's where your application is running.

 * Running on http://127.0.0.1:5001/ (Press CTRL+C to quit)
Go to http://127.0.0.1:5001/ in your browser to view it.

Configure
Every time you start your virtual environment you need to remember to set the FLASK_APP environment variable. When you change projects, you'll need to switch to the appropriate file name. If you accidentally forget, you'll see an error message like this.

Error: Could not locate a Flask application. You did not provide the "FLASK_APP"
environment variable, and a "wsgi.py" or "app.py" module was not found in the
current directory.
One solution is create your application in app/_init.py_. Another is to use configuration. The benefit of a configuration file is that you can set many other environment variables as well, such as FLASK_ENV.

.flaskenv
In order for Flask to access the .flaskenv file, you'll need to install the python-dotenv package.

From your command line terminal,

pipenv install python-dotenv~=0.13
Now create a file named .flaskenv. (Think of the .env file you created to hold environment variables in your Express applications.)

In this file specify the environment variables you want. For now you only need one so it will look like

FLASK_APP=simple.py
FLASK_ENV=development
Notice that export is not include in the file.

If you'd like to test .flaskenv, you need to remove the environment variables. One option is to reboot your computer. Another is to use a command in your terminal called unset. You can think of it like the opposite of export.

Run one or both of these commands.

unset FLASK_APP
unset FLASK_ENV
If you have created the .flaskenv file as above, then pipenv run flask run will work as before. If not, you'll see error and/or warning messages.

app.config
Another approach to configuration is to use a dictionary that comes with the Flask framework. In fact, you will often use both (as you will see momentarily).

This dictionary is called config and it's found in the instantiated Flask object which is named app both in the above example and nearly every Flask application on the planet!

Good - set values directly
As you've seen, it is possible to directly add a property to a dictionary.

For example on the line after app = Flask(__name__), you could set a value as follows

app.config["greeting"] = 'Hello, world!'
If you then decided to use that variable, you might end up with a simple program that looks something like this.

from flask import Flask

app = Flask(__name__)
# Set configuration variable
app.config["greeting"] = 'Hey there, humans!'


@app.route('/')
def hello():
    # Use configuration variable
    return f'<h1>{app.config["greeting"]}</h1>'
In this example, you'll see the return value was switched to a formatted string so the configured variable could be easily integrated.

Better - config class
Not only are you likely to want many configured values, but best practices state that separating concerns into distinct files and classes is a superior approach. Therefore, Flask easily supports loading a module class for your configuration. You can give it a try.

Create a new file in your project folder named config.py. Make it a class with a property for each configuration variable.

class Config(object):
    GREETING = 'Salutations, superior students!'
Modify your program to import your new class right after the flask import

from config import Config
And replace the direct dictionary change (app.config["greeting"] = 'Hey there, humans!') with

app.config.from_object(Config)
That result in a program in simple.py that looks like this:

from flask import Flask
# Load configuration class
from config import Config

app = Flask(__name__)
# Apply configuration from class
app.config.from_object(Config)


@app.route('/')
def hello():
    # Use configuration variable
    return f'<h1>{app.config["GREETING"]}</h1>'
Best - environment overrides config
Sometimes you have a value which changes from environment to environment.

Common examples include debug level and API keys for third party services. As an experiment you can make up any variable you want, of course.

Begin in the Config class. Since you know the value could come from the environment, import the build-in os package and create a class variable which first tries to get the environment value, and if not found, uses a hard-coded value. This would make your config.py look like the following.

import os


class Config(object):
    GREETING = 'Salutations, superior students!'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-key-for-devs'
os.environ.get('SECRET_KEY') is what looks in the environment for SECRET_KEY. If not found, then or causes the string 'default-key-for-devs' to be used instead.

In order to see what's happening, you can print out the value from the program file simple.py (after applying the configuration, of course).

from flask import Flask
# Load configuration class
from config import Config

app = Flask(__name__)
# Apply configuration from class
app.config.from_object(Config)
# Test value of variable that may or may not come from the environment
print("SECRET KEY IS: ", app.config["SECRET_KEY"])


@app.route('/')
def hello():
    # Use configuration variable
    return f'<h1>{app.config["GREETING"]}</h1>'
If you run the application now (using pipenv run flask run), the hard-coded value will show up somewhere in the output

SECRET KEY IS:  default-key-for-devs
Now you edit .flaskenv to add the new variable.

FLASK_APP=simple.py
FLASK_ENV=development
SECRET_KEY=super-secret-stuff
And rerun (control+c followed by pipenv run flask run) to see

SECRET KEY IS:  super-secret-stuff
What you've learned
Setup a new Flask project
Run a simple Flask web application on your computer
Utilize basic configuration on a Flask project