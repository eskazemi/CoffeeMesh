from flask import Flask
from flask_smorest import Api
from config import BaseConfig
from api.api import blueprint

# We create an instance of the Flask application object.
app = Flask(__name__)

app.config.from_object(BaseConfig)

# We create an instance of flask-smorest’s Api object.
kitchen_api = Api(app)

kitchen_api.register_blueprint(blueprint)
