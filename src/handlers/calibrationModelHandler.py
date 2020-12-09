from src import models, db


class CalibrationModelHandler:

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
        db.session.add(new_model)
        db.session.commit()
        print('Commit!!')


#  name, model, customer,
# type_a, a_highValue, a_hvPlus, a_hvMin, a_lowValue, a_lvPlus, a_lvMin,
# type_b, b_highValue, b_hvPlus, b_hvMin, b_lowValue, b_lvPlus, b_lvMin


