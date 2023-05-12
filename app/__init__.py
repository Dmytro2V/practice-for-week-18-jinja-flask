from flask import (Flask, render_template) # type: ignore
# import config class
from app.config import Config # type: ignore



app = Flask(__name__)
# populate Flask config dictionary from config class
app.config.from_object(Config)

# move all routing to routes, and import here
from app import routes


