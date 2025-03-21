from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import os


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "tutDB.sqlite3")

db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

