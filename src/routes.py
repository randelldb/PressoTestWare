from flask import render_template, request
from src import db
from src.models import CalibrationModel
from random import random


from src import app
from src.handlers import modbusHandler
from src.handlers.calibrationModelHandler import CalibrationModelHandler

# CalibrationModelHandler instance
cm = CalibrationModelHandler()


@app.route('/modbusData')
def modbusData():
    text = request.args.get('jsdata')

    # open_conn = modbusHandler.open_modbus_conn('COM6')
    # read_data = modbusHandler.read_data(open_conn)
    x = random()

    #return render_template('modbusData.html', suggestion=read_data)
    return render_template('modbusData.html', suggestion=x)

@app.route('/get_calibration_model')
def get_calibration_model():
    items = CalibrationModel.query.all()
    return render_template('get_calibration_model.html', items=items)

@app.route('/get_model_preset/<id>')
def get_model_preset(id):
    items = CalibrationModel.query.filter_by(id=id).first()
    return render_template('get_model_preset.html', items=items)


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


