class CalibrationValidator:
    hvPassFlag = 0
    lvPassFlag = 0

    def __init__(self, switch, temp, rv, readingHv, highValue, hvPlus, hvMin, readingLv, lowValue, lvPlus, lvMin):
        self.switch = switch

        self.temp = temp
        self.rv = rv

        self.readingHv = readingHv
        self.highValue = highValue
        self.hvPlus = hvPlus
        self.hvMin = hvMin

        self.readingLv = readingLv
        self.lowValue = lowValue
        self.lvPlus = lvPlus
        self.lvMin = lvMin

    def hv_validator(self):
        if self.switch > 5000:

            if 19 <= self.temp <= 21 and 30 <= self.rv <= 60:
                print('Temp is ' + str(self.temp) + ': Temp is in range')
                print('Rv is ' + str(self.rv) + ': Rv is in range')

                if self.highValue - self.hvMin <= self.readingHv <= self.highValue + self.hvPlus:
                    print('pass')
                    # set Pass Flag for High Value
                    self.hvPassFlag = 1
                else:
                    print('fail')
                    self.hvPassFlag = 0
                    self.lvPassFlag = 0

            else:
                print('Check temp and Rv!!!')

    def lv_validator(self):
        if self.hvPassFlag == 1 and self.switch > 5000:

            if 19 <= self.temp <= 21 and 30 <= self.rv <= 60:
                print('Temp is ' + str(self.temp) + ': Temp is in range')
                print('Rv is ' + str(self.rv) + ': Rv is in range')

                if self.lowValue - self.lvMin <= self.readingLv <= self.lowValue + self.lvPlus:
                    print('pass')
                    # set Pass Flag for High Value
                    self.lvPassFlag = 1
                else:
                    print('fail')
                    self.lvPassFlag = 0
                    self.hvPassFlag = 0

            else:
                print('Check temp and Rv!!!')

    def validation_pass(self):
        print(self.lvPassFlag, self.hvPassFlag)
        if self.hvPassFlag and self.lvPassFlag == 1:
            print('Calibration Passed')
        else:
            print('Calibration Failed')


test_a = CalibrationValidator(5001, 20, 40, 8, 8, 0.4, 0.4, 6, 6, 0.1, 0.1)
test_a.hv_validator()
test_a.lv_validator()
test_a.validation_pass()
