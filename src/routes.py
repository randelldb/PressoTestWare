import json

from flask import render_template, request
from jinja2.runtime import to_string

from src import db
from src.models import CalibrationModel, MainCounter
from random import random, uniform, randint

from src import app
from src.handlers import modbusHandler
from src.handlers import printerHandler
from src.handlers.calibrationModelHandler import CalibrationModelHandler

# CalibrationModelHandler instance
cm = CalibrationModelHandler()
global current_model


@app.route('/complete_calibration')
def complete_calibration():
    # update counter
    try:
        db.session.add(MainCounter())
        db.session.commit()
        print('Count update success!')
    except:
        print('Count update  failed...')

    return 'Completed'


@app.route('/set_certificate', methods=['GET', 'POST'])
def set_certificate():
    global current_model
    model = CalibrationModel.query.filter_by(id=current_model).first()
    print('yheaaaaah im in py')
    r_a_hi = request.form['r_a_hi']
    r_a_lo = request.form['r_a_lo']
    temp_a = request.form['temp_a']
    rv_a = request.form['rv_a']
    r_b_hi = request.form['r_b_hi']
    r_b_lo = request.form['r_b_lo']
    temp_b = request.form['temp_b']
    rv_b = request.form['rv_b']
    print(r_a_hi)

    return current_model


@app.route('/certificate_template')
def certificate_template():
    return render_template('certificate_template.html')


@app.route('/modbusData')
def modbusData():
    import json
    x = 0
    toJson = json.dumps(x)
    # open_conn = modbusHandler.open_modbus_conn('COM7')
    # read_data = modbusHandler.read_data(open_conn)
    # toJson = json.dumps(read_data)
    return toJson


@app.route('/get_calibration_model')
def get_calibration_model():
    items = CalibrationModel.query.all()
    return render_template('get_calibration_model.html', items=items)


@app.route('/set_graph_bounds/<id>')
def set_graph_bounds(id):
    test = 5
    items = CalibrationModel.query.filter_by(id=id).first()
    data = {
        'hvPlus': items.a_hvPlus
    }
    toJson = json.dumps(test)
    return data


@app.route('/get_model_preset/<id>')
def get_model_preset(id):
    global current_model
    current_model = id
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


@app.route('/get_printers')
def get_printers():
    printers = printerHandler.get_printers()
    return render_template('get_printers.html', printers=printers)


@app.route('/get_ports')
def get_ports():
    ports = modbusHandler.serial_ports()
    return render_template('get_ports.html', ports=ports)


@app.route('/set_ports/<id>')
def set_ports(id):
    # modbusHandler.open_modbus_conn('COM7')
    connected = id
    return connected


@app.route('/get_count')
def get_count():
    get_certificate_id = MainCounter.query.order_by(MainCounter.id.desc()).first()
    count = to_string(get_certificate_id.id + 1)
    return count


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
