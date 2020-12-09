class CalibrationModelClass:

    # def __init__(self, name, model, customer,
    #              type_a, a_highValue, a_hvPlus, a_hvMin, a_lowValue, a_lvPlus, a_lvMin,
    #              type_b, b_highValue, b_hvPlus, b_hvMin, b_lowValue, b_lvPlus, b_lvMin):

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