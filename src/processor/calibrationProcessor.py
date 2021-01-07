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
            if self.pressureSet - self.tollMin <= self.pressureReading <= self.pressureSet + self.tollPlus:
                cache.set(str(self.selector) + '_temp', self.temp)
                cache.set(str(self.selector) + '_rv', self.rv)
                cache.set(str(self.selector) + '_pressureReading', self.pressureReading)
                return 1
            else:
                return 0
        else:
            print('Check temp and Rv!!!')
            return 0
