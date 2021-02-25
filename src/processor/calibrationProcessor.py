from src import cache


class CalibrationValidator:

    def __init__(self, selector, subSelector, temp, rv, pressureReading, pressureSet, tollPlus, tollMin):

        self.selector = selector
        self.subSelector = subSelector
        self.temp = temp
        self.rv = rv

        self.pressureReading = pressureReading
        self.pressureSet = pressureSet
        self.tollPlus = tollPlus
        self.tollMin = tollMin
        self.checks = []

    def validator(self):
        if 19 <= self.temp <= 21 and 30 <= self.rv <= 60:
            print('env vars passed cur values: ')
            print(self.temp + '--' + self.rv)
            if self.pressureSet - self.tollMin <= self.pressureReading <= self.pressureSet + self.tollPlus:
                print('Press passed cur value: ')
                print(self.pressureReading + 'set point is' + self.pressureSet)
                cache.set(str(self.selector) + '_' + str(self.subSelector) + '_temp', self.temp)
                cache.set(str(self.selector) + '_' + str(self.subSelector) + '_rv', self.rv)
                cache.set(str(self.selector) + '_' + str(self.subSelector) + '_pressureReading', self.pressureReading)
                return 1
            else:
                return 0
        else:
            print('Check temp and Rv!!!')
            return 0
