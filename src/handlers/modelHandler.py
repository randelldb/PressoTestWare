from src.models import CalibrationModel
from src import db
db()


class ModelHandler:

    def __init__(self, name, model, customer,
                 type_a, a_highValue, a_hvPlus, a_hvMin, a_lowValue, a_lvPlus, a_lvMin,
                 type_b, b_highValue, b_hvPlus, b_hvMin, b_lowValue, b_lvPlus, b_lvMin):
        self.name = name
        self.model = model
        self.customer = customer

        self.type_a = type_a
        self.a_highValue = a_highValue
        self.a_hvPlus = a_hvPlus
        self.a_hvMin = a_hvMin
        self.a_lowValue = a_lowValue
        self.a_lvPlus = a_lvPlus
        self.a_lvMin = a_lvMin

        self.type_b = type_b
        self.b_highValue = b_highValue
        self.b_hvPlus = b_hvPlus
        self.b_hvMin = b_hvMin
        self.b_lowValue = b_lowValue
        self.b_lvPlus = b_lvPlus
        self.b_lvMin = b_lvMin

    # def create_model(self):
    #     new_model = CalibrationModel(name=self.name, model=self.model, customer=self.customer,
    #                                  type_a=self.type_a, a_highValue=self.a_highValue, a_hvPlus=self.a_hvPlus,
    #                                  a_hvMin=self.a_hvMin, a_lowValue=self.a_lowValue,
    #                                  a_lvPlus=self.a_lvPlus, a_lvMin=self.a_lvMin,
    #
    #                                  type_b=self.type_b, b_highValue=self.b_highValue, b_hvPlus=self.b_hvPlus,
    #                                  b_hvMin=self.b_hvMin, b_lowValue=self.b_lowValue,
    #                                  b_lvPlus=self.b_lvPlus, b_lvMin=self.b_lvMin)
    #     db.add()
    #     db.commit()
    #     print('Commit')


#  name, model, customer,
# type_a, a_highValue, a_hvPlus, a_hvMin, a_lowValue, a_lvPlus, a_lvMin,
# type_b, b_highValue, b_hvPlus, b_hvMin, b_lowValue, b_lvPlus, b_lvMin

# makeModel = ModelHandler('SLT Pass.', 'Emmerson B100', 'NedTrain',
#                          1, 8, 0.5, 0.5, 6, 0.2, 0.2,
#                          2, 2, 0.1, 0.1, 1, 0.1, 0.1)
# db.add(makeModel)
# db.commit()
