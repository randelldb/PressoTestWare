import json

from flask import render_template, request, redirect
from jinja2.runtime import to_string

from src import db
from src.models import CalibrationModel, MainCounter, CertificateTemplate
from random import random, uniform, randint

from src import app
from src.handlers import modbusHandler, printerHandler
from src.handlers.calibrationModelHandler import CalibrationModelHandler
from src.handlers.templateHandler import TemplateHandler

# CalibrationModelHandler instance
cm = CalibrationModelHandler()
th = TemplateHandler()
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


@app.route('/validate_hv')
def validate_hv():
    print('valitdate')
    return ''


@app.route('/update_certificate_template', methods=['GET', 'POST'])
def update_certificate_template():
    cert_data_1 = request.form['cert_data_1']
    cert_data_2 = request.form['cert_data_2']
    cert_data_3 = request.form['cert_data_3']
    cert_data_4 = request.form['cert_data_4']
    cert_data_5 = request.form['cert_data_5']
    cert_data_6 = request.form['cert_data_6']
    cert_data_7 = request.form['cert_data_7']
    cert_data_8 = request.form['cert_data_8']
    cert_data_9 = request.form['cert_data_9']
    cert_data_10 = request.form['cert_data_10']
    cert_data_11 = request.form['cert_data_11']
    cert_data_12 = request.form['cert_data_12']
    cert_data_13 = request.form['cert_data_13']
    cert_data_14 = request.form['cert_data_14']
    cert_data_15 = request.form['cert_data_15']
    cert_data_16 = request.form['cert_data_16']
    cert_data_17 = request.form['cert_data_17']
    cert_data_18 = request.form['cert_data_18']
    cert_data_19 = request.form['cert_data_19']
    cert_data_20 = request.form['cert_data_20']
    cert_data_21 = request.form['cert_data_21']
    cert_data_22 = request.form['cert_data_22']
    cert_data_23 = request.form['cert_data_23']
    cert_data_24 = request.form['cert_data_24']
    cert_data_25 = request.form['cert_data_25']
    cert_data_26 = request.form['cert_data_26']

    th.update_template(cert_data_1, cert_data_2, cert_data_3, cert_data_4, cert_data_5, cert_data_6, cert_data_7,
                        cert_data_8, cert_data_9, cert_data_10, cert_data_11, cert_data_12, cert_data_13, cert_data_14,
                        cert_data_15, cert_data_16, cert_data_17, cert_data_18, cert_data_19, cert_data_20,
                        cert_data_21, cert_data_22, cert_data_23, cert_data_24, cert_data_25, cert_data_26)

    return redirect('/certificate_template_edit')


@app.route('/certificate_template_edit')
def certificate_template_edit():
    items = CertificateTemplate.query.filter_by(id=1).first()

    return render_template('certificate_template_edit.html', items=items)


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
    return render_template('certificate_template_base.html')


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
    items = CalibrationModel.query.filter_by(id=id).first()
    data = {
        'a_hvPlus': items.a_highValue + items.a_hvPlus,
        'a_hvMin': items.a_lowValue - items.a_hvMin
    }
    toJson = json.dumps(data, indent=4, sort_keys=True)

    return toJson


@app.route('/get_model_data/<id>')
def get_model_data(id):
    global current_model
    current_model = id
    print(current_model)

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

    return render_template('get_model_data.html', items=items, type_a=type_a, type_b=type_b)


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
    return render_template('model_view.html')


@app.route('/model_update/<id>', methods=['GET', 'POST'])
def model_update(id):
    print('if')
    modelName = request.form['modelName']
    brand = request.form['brand']
    model = request.form['model']
    customer = request.form['customer']
    ref = request.form['ref']
    type_a = 1
    a_highValue = request.form['a_highValue']
    a_hvPlus = request.form['a_hvPlus']
    a_hvMin = request.form['a_hvMin']
    a_lowValue = request.form['a_lowValue']
    a_lvPlus = request.form['a_lvPlus']
    a_lvMin = request.form['a_lvMin']
    type_b = 2
    b_highValue = request.form['b_highValue']
    b_hvPlus = request.form['b_hvPlus']
    b_hvMin = request.form['b_hvMin']
    b_lowValue = request.form['b_lowValue']
    b_lvPlus = request.form['b_lvPlus']
    b_lvMin = request.form['b_lvMin']

    cm.update_model(id, modelName, brand, model, customer, ref, type_a, a_highValue, a_hvPlus, a_hvMin, a_lowValue,
                    a_lvPlus, a_lvMin, type_b, b_highValue, b_hvPlus, b_hvMin, b_lowValue, b_lvPlus, b_lvMin)
    return ''


@app.route('/get_model_form_data/<id>')
def get_model_form_data(id):
    global current_model
    current_model = id
    print(current_model)
    items = CalibrationModel.query.filter_by(id=id).first()

    if items.type_a == 0 or items.type_b == 0:
        return render_template('model_form_solo.html', items=items)
    else:
        return render_template('model_form_double.html', items=items)

# ------------------------- Function: Printers and writers
@app.route('/get_printers')
def get_printers():
    printers = printerHandler.get_printers()
    return render_template('get_printers.html', printers=printers)


@app.route('/get_writers')
def get_writers():
    printers = printerHandler.get_printers()
    return render_template('get_writers.html', printers=printers)

# ------------------------- Function: Com
@app.route('/get_ports')
def get_ports():
    ports = modbusHandler.serial_ports()
    return render_template('get_ports.html', ports=ports)


@app.route('/set_ports/<id>')
def set_ports(id):
    connected = modbusHandler.open_modbus_conn(id)
    return ''

# ------------------------- Function: Counter
@app.route('/get_count')
def get_count():
    get_certificate_id = MainCounter.query.order_by(MainCounter.id.desc()).first()
    count = to_string(get_certificate_id.id + 1)
    return count

# ------------------------- Function: Index
@app.route("/")
def index(name=None):
    return render_template('index.html', name=name)
