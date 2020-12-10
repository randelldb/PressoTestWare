from flask import render_template, request
from random import random


from src import app
from src.handlers import modbusHandler
from src.handlers.calibrationModelHandler import CalibrationModelHandler

# CalibrationModelHandler instance
cm = CalibrationModelHandler()


def fixed():
    while True:
        open_conn = modbusHandler.open_modbus_conn('COM6')
        read_data = modbusHandler.read_data(open_conn)
        return read_data

@app.route('/suggestions')
def suggestions():
    text = request.args.get('jsdata')

    open_conn = modbusHandler.open_modbus_conn('COM6')
    read_data = modbusHandler.read_data(open_conn)
    x = random()

    return render_template('suggestions.html', suggestion=x)


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
