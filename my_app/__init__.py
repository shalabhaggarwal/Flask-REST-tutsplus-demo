from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db=db)

from my_app.catalog.views import catalog
app.register_blueprint(catalog)

db.create_all()
