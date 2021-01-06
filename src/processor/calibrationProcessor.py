from src import cache

class CalibrationValidator:

    def __init__(self, selector, temp, rv, pressureReading, pressureSet, tollPlus, tollMin):

        self.selector = selector
        self.temp = temp
        self.rv = rv

        self.pressureReading = pressureReading
        self.pressureSet = pressureSet
        self.tollPlus = tollPlus
        self.tollMin = tollMin

        self.checks = []

    def add(self):
        pass

    def validate(self):
        pass

    def validator(self):
        if 19 <= self.temp <= 21 and 30 <= self.rv <= 60:
            # print('Temp is ' + str(self.temp) + ': Temp is in range')
            # print('Rv is ' + str(self.rv) + ': Rv is in range')
            if self.pressureSet - self.tollMin <= self.pressureReading <= self.pressureSet + self.tollPlus:
                print('pass')

                cache.set(str(self.selector) + '_temp', self.temp)
                cache.set(str(self.selector) + '_rv', self.rv)
                cache.set(str(self.pressureReading) + '_pressureReading', self.pressureReading)
                return 1
            else:
                print('fail')
                return 0
        else:
            print('Check temp and Rv!!!')
            return 0
