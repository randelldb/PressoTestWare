from src import app
from flask import render_template
from src.handlers.calibrationModelHandler import CalibrationModelHandler

@app.route('/')
def hello(name=None):
    # CalibrationModelHandler.create_model('SLT Pass.', 'Emmerson B100', 'NedTrain',
    #              1, 8, 0.5, 0.5, 6, 0.2, 0.2,
    #              2, 2, 0.1, 0.1, 1, 0.1, 0.1)

    return render_template('index.html', name=name)