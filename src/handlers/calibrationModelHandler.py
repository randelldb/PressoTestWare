from flask import jsonify
from src import models, db


class CalibrationModelHandler:
    @staticmethod
    def select_model(id):
        select_model = models.CalibrationModel.query.filter_by(id=id).first()

        return select_model

    @staticmethod
    def create_model(name, brand, model, customer, ref, type_a, a_highValue, a_hvPlus, a_hvMin, a_lowValue, a_lvPlus,
                     a_lvMin,
                     type_b, b_highValue, b_hvPlus, b_hvMin, b_lowValue, b_lvPlus, b_lvMin):

        new_model = models.CalibrationModel(name=name, brand=brand, model=model, customer=customer, ref=ref,
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
    def update_model(model_id, name, brand, model, customer, ref, type_a, a_highValue, a_hvPlus, a_hvMin, a_lowValue,
                     a_lvPlus, a_lvMin, type_b, b_highValue, b_hvPlus, b_hvMin, b_lowValue, b_lvPlus, b_lvMin):

        select_model = models.CalibrationModel.query.get(model_id)
        select_model.name = name
        select_model.brand = brand
        select_model.model = model
        select_model.customer = customer
        select_model.ref = ref
        select_model.type_a = type_a
        select_model.a_highValue = a_highValue
        select_model.a_hvPlus = a_hvPlus
        select_model.a_hvMin = a_hvMin
        select_model.a_lowValue = a_lowValue
        select_model.a_lvPlus = a_lvPlus
        select_model.a_lvMin = a_lvMin
        select_model.type_b = type_b
        select_model.b_highValue = b_highValue
        select_model.b_hvPlus = b_hvPlus
        select_model.b_hvMin = b_hvMin
        select_model.b_lowValue = b_lowValue
        select_model.b_lvPlus = b_lvPlus
        select_model.b_lvMin = b_lvMin

        try:
            db.session.commit()
            print('Update model success!')
        except:
            print('Update model failed...')
