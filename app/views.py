from flask import url_for, redirect
from flask_smorest import Api

from app import app
from .resources.category import blp as CategoryBlueprint
from .resources.record import blp as RecordBlueprint
from .resources.user import blp as UserBlueprint

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Flask REST API"
app.config["API_VERSION"] = "v1.0.0"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"

api = Api(app)
api.register_blueprint(UserBlueprint)
api.register_blueprint(CategoryBlueprint)
api.register_blueprint(RecordBlueprint)


@app.route("/")
def index():
    return redirect(url_for("get_users"), code=302)
