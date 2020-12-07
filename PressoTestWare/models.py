from sqlalchemy import Column, Integer, String
from PressoTestWare import Base


class CalibrationModel(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<CalibrationModel(title='%s')>" % self.name
