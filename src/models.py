from src import db


class CalibrationModel(db.Model):
    __tablename__ = 'CalibrationModel'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    model = db.Column(db.String(255))
    customer = db.Column(db.String(255))
    highValue = db.Column(db.Float())
    hvPlus = db.Column(db.Float())
    hvMin = db.Column(db.Float())
    lowValue = db.Column(db.Float())
    lvPlus = db.Column(db.Float())
    lvMin = db.Column(db.Float())

    # def __init__(self, name, model, customer, highValue, hvPlus, hvMin, lowValue, lvPlus, lvMin):
    #     self.name = name
    #     self.model = model
    #     self.customer = customer
    #     self.highValue = highValue
    #     self.hvPlus = hvPlus
    #     self.hvMin = hvMin
    #     self.lowValue = lowValue
    #     self.lvPlus = lvPlus
    #     self.lvMin = lvMin

    # def __repr__(self, name):
    #      return "<CalibrationModel(title='%s')>" % self.name
