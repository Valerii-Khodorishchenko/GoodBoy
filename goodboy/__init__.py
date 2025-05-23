from flask import Flask
# from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import Config


app = Flask(__name__, static_folder='static')
app.config.from_object(Config)
db = SQLAlchemy(app)
# migrate = Migrate(app, db)
from goodboy import models
with app.app_context():
    db.create_all()

from . import views