import json

from flask import render_template, request
from jinja2.runtime import to_string

from src import db
from src.models import CalibrationModel, MainCounter
from random import random, uniform, randint

from src import app
from src.handlers import modbusHandler, printerHandler
from src.processor import calibrationProcessor
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

    return current_model


@app.route('/certificate_template')
def certificate_template():
    return render_template('certificate_template.html')


@app.route('/modbusData')
def modbusData():
    import json
    x = 0
    toJson = json.dumps(x)

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

    return data


@app.route('/get_model_preset/<id>')
def get_model_preset(id):
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

    print(current_model)

    return render_template('get_model_preset.html', items=items, type_a=type_a, type_b=type_b)


@app.route('/model_view')
def model_view():
    return render_template('model_view.html')


@app.route('/create_model', methods=['GET', 'POST'])
def create_model():
    modelName = request.form['modelName']
    brand = request.form['brand']
    model = request.form['model']
    customer = request.form['customer']
    ref = request.form['ref']

    type_a = 1
    a_highValue = request.form['a_highValue']
    b_highValue = request.form['b_highValue']
    a_hvPlus = request.form['a_hvPlus']
    a_hvMin = request.form['a_hvMin']
    b_hvPlus = request.form['b_hvPlus']
    b_hvMin = request.form['b_hvMin']

    type_b = 1
    a_lowValue = request.form['a_lowValue']
    b_lowValue = request.form['b_lowValue']
    a_lvPlus = request.form['a_lvPlus']
    a_lvMin = request.form['a_lvMin']
    b_lvPlus = request.form['b_lvPlus']
    b_lvMin = request.form['b_lvMin']

    cm.create_model(modelName, brand, model, customer, ref,
                    type_a, a_highValue, b_highValue, a_hvPlus, a_hvMin, b_hvPlus, b_hvMin,
                    type_b, a_lowValue, b_lowValue, a_lvPlus, a_lvMin, b_lvPlus, b_lvMin)

    return render_template('model_view.html')

@app.route('/model_delete/<id>')
def model_delete(id):
    cm.delete_model(id)

    print('deleted')

@app.route('/get_model_form_data/<id>')
def get_model_form_data(id):
    items = CalibrationModel.query.filter_by(id=id).first()


    if items.type_a == 0 or items.type_b == 0:
        return render_template('model_form_solo.html', items=items)
    else:
        return render_template('model_form_double.html', items=items)


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
    connected = id
    return connected


@app.route('/get_count')
def get_count():
    get_certificate_id = MainCounter.query.order_by(MainCounter.id.desc()).first()
    count = to_string(get_certificate_id.id + 1)
    return count


@app.route("/")
def index(name=None):
    return render_template('index.html', name=name)
