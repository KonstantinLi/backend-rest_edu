from flask import Flask
from flask_marshmallow import Marshmallow

from . import random_data

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'SecretKey'
ma = Marshmallow(app)
data = random_data.Creator.create_data()

from . import views


