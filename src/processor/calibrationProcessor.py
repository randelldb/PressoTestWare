class CalibrationValidator:

    def __init__(self, temp, rv, pressureReading, pressureSet, tollPlus, tollMin):

        self.temp = temp
        self.rv = rv

        self.pressureReading = pressureReading
        self.pressureSet = pressureSet
        self.tollPlus = tollPlus
        self.tollMin = tollMin

    def validator(self):
        if 19 <= self.temp <= 21 and 30 <= self.rv <= 60:
            print('Temp is ' + str(self.temp) + ': Temp is in range')
            print('Rv is ' + str(self.rv) + ': Rv is in range')
            if self.pressureSet - self.tollMin <= self.pressureReading <= self.pressureSet + self.tollPlus:
                print('pass')
                return 1
            else:
                print('fail')
                return 0
        else:
            print('Check temp and Rv!!!')
            return 0
