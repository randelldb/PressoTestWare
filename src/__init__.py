debug = True
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

dir_path = os.path.dirname(os.path.realpath(__file__))

# Flask app instance
app = Flask(__name__, template_folder=dir_path + '/templates')
# SQL Alchemy instance
db = SQLAlchemy()
# DB Migration instance
migrate = Migrate()
# Marshmallow Instance
ma = Marshmallow()


def create_app(test_config=None):
    from src import models, routes

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dir_path + '/data/db.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    return app

# # Test area #
# from src.models import CalibrationModel
#
# #@staticmethod
# def create():
#     testCommit = CalibrationModel('Real Commit', 'Danfos 1234', 'HTM', 1, 2, 3, 4, 5, 6)
#
#     session.add(testCommit)
#     session.commit()
#     print("im running on my one")
#     #return testCommit
#
# create()
# # Test area #
