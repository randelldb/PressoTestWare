import sqlite3

conn = sqlite3.connect('data/db.db')
curr = conn.cursor()


class CalibrationModel:
    def __init__(self, name, model, customer, highValue, hvTollPlus, hvTollMin, lowValue, lvTollPlus, lvTollMin):
        self.name = name
        self.model = model
        self.customer = customer
        self.highValue = highValue
        self.hvTollPlus = hvTollPlus
        self.hvTollMin = hvTollMin
        self.lowValue = lowValue
        self.lvTollPlus = lvTollPlus
        self.lvTollMin = lvTollMin
        create_model(name, model, customer, highValue, hvTollPlus, hvTollMin, lowValue, lvTollPlus, lvTollMin)


def create_model(name, model, customer, highValue, hvTollPlus, hvTollMin, lowValue, lvTollPlus, lvTollMin):
    curr.execute(
        "INSERT INTO test Values ('" + name + "', '" + model + "', '" + customer + "', " + highValue + ", " + hvTollPlus + ", " + hvTollMin + ", " + lowValue + ", " + lvTollPlus + ", " + lvTollMin + ")")
    conn.commit()
    conn.close()
    print('done')


CalibrationModel('test insert')

# class CalibrationModel:
#     def __init__(self, name):
#         self.name = name
#         create_model(name)
#
#
#
# def create_model(name):
#     curr.execute("INSERT INTO test Values ('"+ name +"')")
#     conn.commit()
#     conn.close()
#     print('done')
#
#
# CalibrationModel('test insert')
