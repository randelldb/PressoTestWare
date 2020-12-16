from flask import render_template, request
from src import db
from src.models import CalibrationModel
from random import random, uniform, randint

from src import app
from src.handlers import modbusHandler
from src.handlers.calibrationModelHandler import CalibrationModelHandler


# CalibrationModelHandler instance
cm = CalibrationModelHandler()


@app.route('/modbusData')
def modbusData():
    import json
    text = request.args.get('jsdata')
    x = 4

    a = {'name': 'bar', 'data': x}
    toJson = json.dumps(a)

    # read_data = modbusHandler.read_data(open_conn)
    # return render_template('modbusData.html', suggestion=read_data)
    return toJson


@app.route('/get_calibration_model')
def get_calibration_model():
    items = CalibrationModel.query.all()
    return render_template('get_calibration_model.html', items=items)

    
@app.route('/get_model_preset/<id>')
def get_model_preset(id):
    items = CalibrationModel.query.filter_by(id=id).first()
    type_a = items.type_a
    type_b = items.type_b

    if type_a == 1:
        type_a = "High Pressure"
    elif type_a == 2:
        type_a = "Low Pressure"
    elif type_a == 3:
        type_a = "Condenser Pressure"

    if type_b == 1:
        type_b = "High Pressure"
    elif type_b == 2:
        type_b = "Low Pressure"
    elif type_b == 3:
        type_b = "Condenser Pressure"
    return render_template('get_model_preset.html', items=items, type_a=type_a, type_b=type_b)


@app.route('/get_ports')
def get_ports():
    ports = modbusHandler.serial_ports()
    return render_template('get_ports.html', ports=ports)


@app.route('/set_ports/<id>')
def set_ports(id):
    modbusHandler.open_modbus_conn(id)
    print(id)
    return render_template('set_ports.html')


@app.route("/")
def index(name=None):
    # Adding model test
    # cm.create_model('SLT Pass.', 'Emmerson B100', 'NedTrain',
    #              1, 8, 0.5, 0.5, 6, 0.2, 0.2,
    #              2, 2, 0.1, 0.1, 1, 0.1, 0.1)

    # Deleting model test
    # cm.delete_model(1)

    # Updating model test
    # !!move to other file!!
    # cm.update_model(1)

    return render_template('index.html', name=name)
