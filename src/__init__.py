import atexit
import threading
import serial
from src.config import confReader

debug = True
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_caching import Cache
from src.handlers.modbusHandler import readModbus, opennModbus

# Flask instance
dir_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__,
            template_folder=dir_path + '/templates',
            static_folder=dir_path + '/templates/static')

cache = Cache(config={'CACHE_TYPE': 'simple'})

# SQL Alchemy instance
db = SQLAlchemy()
# DB Migration instance
migrate = Migrate()
# Marshmallow Instance
ma = Marshmallow()

# Seconds
POOL_TIME = 0.2
# variables that are accessible from anywhere
modbusThreadData = {}
# lock to control access to variable
dataLock = threading.Lock()
# thread handler
yourThread = threading.Thread()


def create_app(test_config=None):
    opennModbus()

    def interrupt():
        global yourThread
        yourThread.cancel()

    def doStuff():
        global modbusThreadData
        global yourThread
        with dataLock:
            modbusThreadData = readModbus()
            modbusCollector(modbusThreadData)

            # Set the next thread to happen
            yourThread = threading.Timer(POOL_TIME, doStuff, ())
            yourThread.start()

    def doStuffStart():
        # Do initialisation stuff here
        global yourThread
        # Create your thread
        yourThread = threading.Timer(POOL_TIME, doStuff, ())
        yourThread.start()

    # Initiate
    doStuffStart()
    # When you kill Flask (SIGTERM), clear the trigger for the next thread
    atexit.register(interrupt)

    def modbusCollector(data):
        modbusGlobal(data)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dir_path + '/data/db.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cache.init_app(app)

    return app


def modbusGlobal(data):
    global modbusThreadData
    modbusThreadData = data


def modbusTransporter():
    global modbusThreadData
    if modbusThreadData is None:
        return {}
    else:
        return modbusThreadData
