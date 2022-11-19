from flask import Flask
from . import model

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'SecretKey'
data = model.Creator.create_data()

from . import views


