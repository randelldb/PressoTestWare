from src import db

class MainCounter(db.Model):
    __tablename__ = 'MainCounter'

    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer())

class DefaultSettings(db.Model):
    __tablename__ = 'DefaultSettings'

    id = db.Column(db.Integer, primary_key=True)
    com = db.Column(db.String(255))
    main_printer = db.Column(db.String(255))
    label_writer = db.Column(db.String(255))

class CertificateTemplate(db.Model):
    __tablename__ = 'CertificateTemplate'

    id = db.Column(db.Integer, primary_key=True)
    cert_data_1 = db.Column(db.String(255))
    cert_data_2 = db.Column(db.String(255))
    cert_data_3 = db.Column(db.String(255))
    cert_data_4 = db.Column(db.String(255))
    cert_data_5 = db.Column(db.String(255))
    cert_data_6 = db.Column(db.String(255))
    cert_data_7 = db.Column(db.String(255))
    cert_data_8 = db.Column(db.String(255))
    cert_data_9 = db.Column(db.String(255))
    cert_data_10 = db.Column(db.String(255))
    cert_data_11 = db.Column(db.String(255))
    cert_data_12 = db.Column(db.String(255))
    cert_data_13 = db.Column(db.String(255))
    cert_data_14 = db.Column(db.String(255))
    cert_data_15 = db.Column(db.String(255))
    cert_data_16 = db.Column(db.String(255))
    cert_data_17 = db.Column(db.String(255))
    cert_data_18 = db.Column(db.String(255))
    cert_data_19 = db.Column(db.String(255))
    cert_data_20 = db.Column(db.String(255))
    cert_data_21 = db.Column(db.String(255))
    cert_data_22 = db.Column(db.String(255))
    cert_data_23 = db.Column(db.String(255))
    cert_data_24 = db.Column(db.String(255))
    cert_data_25 = db.Column(db.String(255))
    cert_data_26 = db.Column(db.String(255))

class CalibrationModel(db.Model):
    __tablename__ = 'CalibrationModel'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    brand = db.Column(db.String(255))
    model = db.Column(db.String(255))
    customer = db.Column(db.String(255))
    ref = db.Column(db.String(255))

    type_a = db.Column(db.Integer())
    a_highValue = db.Column(db.Float())
    a_hvPlus = db.Column(db.Float())
    a_hvMin = db.Column(db.Float())
    a_lowValue = db.Column(db.Float())
    a_lvPlus = db.Column(db.Float())
    a_lvMin = db.Column(db.Float())

    type_b = db.Column(db.Integer())
    b_highValue = db.Column(db.Float())
    b_hvPlus = db.Column(db.Float())
    b_hvMin = db.Column(db.Float())
    b_lowValue = db.Column(db.Float())
    b_lvPlus = db.Column(db.Float())
    b_lvMin = db.Column(db.Float())
