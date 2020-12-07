import os
import traceback
from typing import Tuple, Union, Any, Dict

from tkinter import *

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# instantiate database
engine = create_engine('sqlite:///../data/db.db', echo=True)
session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

# Creates a new session to the database by using the engine we described.
Session = sessionmaker(bind=engine)
session = Session()

from PressoTestWare.models import CalibrationModel

@staticmethod
def create():
    testCommit = CalibrationModel('Testing 2')

    session.add(testCommit)
    session.commit()

    return testCommit



