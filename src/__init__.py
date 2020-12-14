debug = True
import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# Flask instance
dir_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__,
            template_folder=dir_path + '/templates',
            static_folder=dir_path + '/templates/static')

# SQL Alchemy instance
db = SQLAlchemy()
# DB Migration instance
migrate = Migrate()
# Marshmallow Instance
ma = Marshmallow()



def create_app(test_config=None):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dir_path + '/data/db.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    return app
