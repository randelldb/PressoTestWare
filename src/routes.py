import json
from threading import Thread
import time
from datetime import date

from flask import render_template, request, redirect, Response
from jinja2.runtime import to_string

import src
from src import app
from src import db
from src import cache
from src.config import confReader

from src.models import CalibrationModel, MainCounter, CertificateTemplate
from src.handlers import printerHandler, certificateWriter, modbusHandler
from src.handlers.calibrationModelHandler import CalibrationModelHandler
from src.handlers.templateHandler import TemplateHandler
from src.processor.calibrationProcessor import CalibrationValidator

cm = CalibrationModelHandler()
th = TemplateHandler()
today = date.today()

### GLOBALS ###
current_id = 1
start = False
readingLoop = {}


# ------------------------- Handling: Calibration

@app.route('/complete_calibration')
def complete_calibration():
    # print label 3 times
    # for i in range(3):
    #     printerHandler.print_label()

    # when completed update counter
    get_certificate_id = MainCounter.query.filter_by(id=1).first()
    get_certificate_id.count = get_certificate_id.count + 1

    db.session.commit()
    print('Count update success!')

    return 'Completed'


def calibration_loop(selector):
    print(selector)
    with app.app_context():
        data = cm.select_model(current_id)

    parse_mb_data = json.loads(modbusData())
    print(parse_mb_data)

    # activate realtime data reading
    # while True:
    #     time.sleep(1)
    # parse_mb_data = readingLoop

    hvPassFlag = 0
    lvPassFlag = 0

    global start_stop
    while start_stop:
        print('Validate Loop started')
        while True:
            if parse_mb_data['switch'] > 5000:
                print('Switch > 5000')
                validateHv = CalibrationValidator(selector,
                                                  'hi',
                                                  parse_mb_data['temp'],
                                                  parse_mb_data['rv'],
                                                  parse_mb_data['press'],
                                                  getattr(data, selector + '_highValue'),
                                                  getattr(data, selector + '_hvPlus'),
                                                  getattr(data, selector + '_hvMin'))

                hvPassFlag = validateHv.validator()

                if hvPassFlag == 1:
                    print(selector + " pass hv, Pass flag raised")
                    print("!!" + hvPassFlag + 'Hi !!')
                else:
                    print(selector + " Fail hv test, Failed flag raised")

            if parse_mb_data['switch'] <= 5000 and hvPassFlag == 1:
                print('Switch <= 5000')
                validateLv = CalibrationValidator(selector,
                                                  'lo',
                                                  parse_mb_data['temp'],
                                                  parse_mb_data['rv'],
                                                  parse_mb_data['press'],
                                                  getattr(data, selector + '_lowValue'),
                                                  getattr(data, selector + '_lvPlus'),
                                                  getattr(data, selector + '_lvMin'))

                lvPassFlag = validateLv.validator()

                if lvPassFlag == 1:
                    print(selector + " pass lv, Pass flag raised")
                    print("!!" + lvPassFlag + 'Lo !!')

                else:
                    print(selector + " Fail lv test, Fail flag raised")

            if hvPassFlag == 1 and lvPassFlag == 1:
                print(selector + " full test passed")
                break


def manual_run(selector):
    t = Thread(target=calibration_loop(selector))
    t.start()
    return "Processing"


@app.route('/run/<selector>', methods=['GET'])
def run(selector):
    global start_stop
    start_stop = True
    print("start")
    return Response(manual_run(selector), mimetype="text/html")


@app.route('/stop/<selector>', methods=['GET'])
def stop(selector):
    global start_stop
    start_stop = False

    # Get general dynamic data
    get_certificate_id = get_count()
    cur_date = today.strftime("%d/%m/%Y")

    # Get dynamic data from cache
    a_hi_temp = cache.get('a_hi_temp')
    a_hi_rv = cache.get('a_hi_rv')
    b_hi_temp = cache.get('b_hi_temp')
    b_hi_rv = cache.get('b_hi_rv')
    a_hi_pressureReading = cache.get('a_hi_pressureReading')
    a_lo_pressureReading = cache.get('a_lo_pressureReading')
    b_hi_pressureReading = cache.get('b_hi_pressureReading')
    b_lo_pressureReading = cache.get('b_lo_pressureReading')

    get_dynamic_cert_data = \
        {"a_hi_temp": a_hi_temp,
         "a_hi_rv": a_hi_rv,
         "b_hi_temp": b_hi_temp,
         "b_hi_rv": b_hi_rv,
         "a_hi_pressureReading": a_hi_pressureReading,
         "a_lo_pressureReading": a_lo_pressureReading,
         "b_hi_pressureReading": b_hi_pressureReading,
         "b_lo_pressureReading": b_lo_pressureReading,
         "get_certificate_id": get_certificate_id,
         "cur_date": cur_date}

    # Get static data for template (data can be changed in the gui template manager)
    get_fixed_cert_data = CertificateTemplate.query.filter_by(id=1).first()
    get_model_cert_data = CalibrationModel.query.filter_by(id=current_id).first()
    certificateWriter.write_data(get_fixed_cert_data, get_dynamic_cert_data, get_model_cert_data)

    return 'stopped'


# ------------------------- Handling: graphs
@app.route('/set_graph_bounds/<id>')
def set_graph_bounds(id):
    ### GLOBALS ###
    global current_id
    current_id = id
    items = CalibrationModel.query.filter_by(id=id).first()
    data = {
        'a_hvPlus': items.a_highValue + items.a_hvPlus,
        'a_hvMin': items.a_highValue - items.a_hvMin,
        'a_lvPlus': items.a_lowValue + items.a_lvPlus,
        'a_lvMin': items.a_lowValue - items.a_lvMin,
        'b_hvPlus': items.b_highValue + items.b_hvPlus,
        'b_hvMin': items.b_highValue - items.b_hvMin,
        'b_lvPlus': items.b_lowValue + items.b_lvPlus,
        'b_lvMin': items.b_lowValue - items.b_lvMin
    }

    toJson = json.dumps(data, indent=4, sort_keys=True)

    return toJson


# ------------------------- Handling: Certificates
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


# ------------------------- Handling: Views
@app.route('/get_calibration_model')
def get_calibration_model():
    items = CalibrationModel.query.all()
    return render_template('get_calibration_model.html', items=items)


@app.route('/get_calibration_model_for_view')
def get_calibration_model_for_view():
    items = CalibrationModel.query.all()
    return render_template('get_calibration_model_for_view.html', items=items)


@app.route('/get_model_data/<id>')
def get_model_data(id):
    items = CalibrationModel.query.filter_by(id=id).first()

    return render_template('get_model_data.html', items=items)


@app.route('/model_view')
def model_view():
    return render_template('model_view.html')


@app.route('/certificate_template')
def certificate_template():
    return render_template('certificate_template_base.html')


# ------------------------- Handling: Calibration models
@app.route('/create_model', methods=['GET', 'POST'])
def create_model():
    modelName = request.form['modelName']
    brand = request.form['brand']
    model = request.form['model']
    customer = request.form['customer']
    ref = request.form['ref']

    type_a = request.form['drop_a']
    a_highValue = request.form['a_highValue']
    a_hvPlus = request.form['a_hvPlus']
    a_hvMin = request.form['a_hvMin']
    a_lowValue = request.form['a_lowValue']
    a_lvPlus = request.form['a_lvPlus']
    a_lvMin = request.form['a_lvMin']

    type_b = request.form['drop_b']
    b_highValue = request.form['b_highValue']
    b_hvPlus = request.form['b_hvPlus']
    b_hvMin = request.form['b_hvMin']
    b_lowValue = request.form['b_lowValue']
    b_lvPlus = request.form['b_lvPlus']
    b_lvMin = request.form['b_lvMin']

    cm.create_model(modelName, brand, model, customer, ref,
                    type_a, a_highValue, a_hvPlus, a_hvMin, a_lowValue, a_lvPlus, a_lvMin,
                    type_b, b_highValue, b_hvPlus, b_hvMin, b_lowValue, b_lvPlus, b_lvMin, )

    return render_template('model_view.html')


# Function to get a calibration model
@app.route('/get_model_form_data/<id>')
def get_model_form_data(id):
    items = CalibrationModel.query.filter_by(id=id).first()

    if items.type_b == "Leeg":
        return render_template('model_form_solo.html', items=items)
    else:
        return render_template('model_form_double.html', items=items)


# Delete function to delete a calibration model from the 'Model configuratie' view
@app.route('/model_delete/<id>')
def model_delete(id):
    cm.delete_model(id)
    print('deleted')
    return render_template('model_view.html')


# Update function to update a calibration model from the 'Model configuratie' view
@app.route('/model_update/<id>', methods=['GET', 'POST'])
def model_update(id):
    modelName = request.form['modelName']
    brand = request.form['brand']
    model = request.form['model']
    customer = request.form['customer']
    ref = request.form['ref']
    type_a = request.form['type_a']
    a_highValue = request.form['a_highValue']
    a_hvPlus = request.form['a_hvPlus']
    a_hvMin = request.form['a_hvMin']
    a_lowValue = request.form['a_lowValue']
    a_lvPlus = request.form['a_lvPlus']
    a_lvMin = request.form['a_lvMin']
    type_b = request.form['type_b']
    b_highValue = request.form['b_highValue']
    b_hvPlus = request.form['b_hvPlus']
    b_hvMin = request.form['b_hvMin']
    b_lowValue = request.form['b_lowValue']
    b_lvPlus = request.form['b_lvPlus']
    b_lvMin = request.form['b_lvMin']

    cm.update_model(id, modelName, brand, model, customer, ref, type_a, a_highValue, a_hvPlus, a_hvMin, a_lowValue,
                    a_lvPlus, a_lvMin, type_b, b_highValue, b_hvPlus, b_hvMin, b_lowValue, b_lvPlus, b_lvMin)
    return ''


# ------------------------- Handling: Printers and writers
# Set the chosen printer from get_printers() as active
@app.route('/set_printer/<selectedPrinter>')
def set_printers(selectedPrinter):
    confReader.writeConfig('default-settings', 'printer', selectedPrinter)
    return ''


# Get list of available printers on the system
@app.route('/get_printers')
def get_printers():
    printers = printerHandler.get_printers()
    return render_template('get_printers.html', printers=printers)


# Set the chosen label writer from get_writers() as active
@app.route('/set_writer/<selectedWriter>')
def set_writer(selectedWriter):
    confReader.writeConfig('default-settings', 'writer', selectedWriter)
    return ''


# Get list of available label writers on the system
@app.route('/get_writers')
def get_writers():
    writers = printerHandler.get_printers()
    return render_template('get_writers.html', writers=writers)


# ------------------------- Handling: Com connection
# Display list of serial ports available on the system
@app.route('/get_ports')
def get_ports():
    # ports = modbusHandler.serial_ports()
    ports = 'leeg'
    return render_template('get_ports.html', ports=ports)


# Set the chosen port from get_ports() as active
@app.route('/set_ports/<id>')
def set_ports(id):
    # set port in config file
    confReader.writeConfig('default-settings', 'com', id)


@app.route('/modbusTransporter/<pressLoop>/<rvLoop>/<tempLoop>/<swtLoop>')
def modbusTransporter(pressLoop, rvLoop, tempLoop, swtLoop):
    global readingLoop
    readingLoop = {
        'press': pressLoop,
        'rv': rvLoop,
        'temp': tempLoop,
        'switch': swtLoop
    }
    return ''


# function to open modbus connection
@app.route('/modbusData')
def modbusData():
    # readConfig = confReader.readConfig()
    # defaultCom = readConfig['default-settings']['com']
    # return json.dumps(modbusHandler.readModbus())
    # return json.dumps(modbusThreadData)
    print(json.dumps(src.modbusTransporter()))
    return json.dumps(src.modbusTransporter())


# ------------------------- Handling: Counter
# Counter used as calibration id number
@app.route('/get_count')
def get_count():
    get_certificate_id = MainCounter.query.filter_by(id=1).first()
    count = to_string(get_certificate_id.count + 1)
    return count


# ------------------------- Handling: Index

@app.route('/get_part_divider/<id>')
def get_part_divider(id):
    items = CalibrationModel.query.filter_by(id=id).first()
    return render_template('part_divider.html', items=items)


@app.route("/")
def index(name=None):
    return render_template('index.html', name=name)
