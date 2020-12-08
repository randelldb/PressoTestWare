hvPassFlag = 0
lvPassFlag = 0


def hv_validator(temp, rv, reading, highValue, hvPlus, hvMin):
    temp = temp
    rv = rv
    reading = reading

    highValue = highValue
    hvPlus = hvPlus
    hvMin = hvMin

    if 19 <= temp <= 21 and 30 <= rv <= 60:
        print('Temp is ' + str(temp) + ': Temp is in range')
        print('Rv is ' + str(rv) + ': Rv is in range')

        if highValue - hvMin <= reading <= highValue + hvPlus:
            print('pass')
            # set Pass Flag for High Value
            hvPassFlag = 1
        else:
            print('fail')
            hvPassFlag, lvPassFlag = 0

    else:
        print('Check temp and Rv!!!')

    print(hvPassFlag)


def lv_validator(temp, rv, reading, lowValue, lvPlus, lvMin):
    temp = temp
    rv = rv
    reading = reading

    lowValue = lowValue
    lvPlus = lvPlus
    lvMin = lvMin

    if 19 <= temp <= 21 and 30 <= rv <= 60:
        print('Temp is ' + str(temp) + ': Temp is in range')
        print('Rv is ' + str(rv) + ': Rv is in range')

        if lowValue - lvMin <= reading <= lowValue + lvPlus:
            print('pass')
            # set Pass Flag for High Value
            lvPassFlag = 1
        else:
            print('fail')
            lvPassFlag, hvPassFlag = 0

    else:
        print('Check temp and Rv!!!')

    print(lvPassFlag)


def validation_pass(lvPassFlag, hvPassFlag):
    print('inside fn')
    print(lvPassFlag, hvPassFlag)
    if hvPassFlag and lvPassFlag == 1:
        print('Full Pass')
    elif hvPassFlag == 0 and lvPassFlag == 1:
        print('High value Fail')
    elif lvPassFlag == 0 and hvPassFlag == 1:
        print('Low value Fail')
    elif lvPassFlag and hvPassFlag == 0:
        print('Full Fail!!')


hv_validator(20, 40, 8, 8, 0.4, 0.4)

lv_validator(21, 35, 1.1, 1, 0.1, 0.1)

validation_pass(lvPassFlag, hvPassFlag)
