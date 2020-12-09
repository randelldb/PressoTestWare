from src import app
from flask import render_template
from src.handlers.calibrationModelHandler import CalibrationModelHandler

# CalibrationModelHandler instance
cm = CalibrationModelHandler()


@app.route('/')
def hello(name=None):
    # Adding model test
    # cm.create_model('SLT Pass.', 'Emmerson B100', 'NedTrain',
    #              1, 8, 0.5, 0.5, 6, 0.2, 0.2,
    #              2, 2, 0.1, 0.1, 1, 0.1, 0.1)

    # Deleting model test
    # cm.delete_model(1)

    # Updating model test
    # !!move to other file!!
    cm.update_model(1)


    return render_template('index.html', name=name)
