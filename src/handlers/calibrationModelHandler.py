from flask import jsonify

from src import models, db


class CalibrationModelHandler:

    @staticmethod
    def select_model():

        select_model = models.CalibrationModel.query.get(1)

    @staticmethod
    def create_model(name, model, customer, type_a, a_highValue, a_hvPlus, a_hvMin, a_lowValue, a_lvPlus, a_lvMin,
                     type_b, b_highValue, b_hvPlus, b_hvMin, b_lowValue, b_lvPlus, b_lvMin):

        new_model = models.CalibrationModel(name=name, model=model, customer=customer,
                                            type_a=type_a, a_highValue=a_highValue, a_hvPlus=a_hvPlus,
                                            a_hvMin=a_hvMin, a_lowValue=a_lowValue,
                                            a_lvPlus=a_lvPlus, a_lvMin=a_lvMin,
                                            type_b=type_b, b_highValue=b_highValue, b_hvPlus=b_hvPlus,
                                            b_hvMin=b_hvMin, b_lowValue=b_lowValue,
                                            b_lvPlus=b_lvPlus, b_lvMin=b_lvMin)

        try:
            db.session.add(new_model)
            db.session.commit()
            print('Creating model success!')
        except:
            print('Creating model failed...')

    @staticmethod
    def delete_model(model_id):
        get_model_id = models.CalibrationModel.query.filter_by(id=model_id).first()

        try:
            db.session.delete(get_model_id)
            db.session.commit()
            print('Deleting model success!')
        except:
            print('Deleting model failed...')


    @staticmethod
    def update_model(model_id):

        select_model = models.CalibrationModel.query.get(model_id)
        select_model.name = 'test'

        try:
            db.session.commit()
            print('Update model success!')
        except:
            print('Update model failed...')

