import random

import minimalmodbus
import serial
from time import time, sleep

# instrument = minimalmodbus.Instrument('COM7', 1)  # port name, slave address (in decimal)
# # instrument.serial.port  # this is the serial port name
# instrument.serial.baudrate = 115200  # Baud
# instrument.serial.bytesize = 8
# instrument.serial.parity = serial.PARITY_NONE
# instrument.serial.stopbits = 1
# instrument.serial.timeout = 0.2  # seconds
# # instrument.address  # this is the slave address number
# instrument.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode
# instrument.clear_buffers_before_each_transaction = True
# rv = int(instrument.read_register(512, 1))  # Registernumber, number of decimals
# temp = int(instrument.read_register(516, 1))
# press = int(instrument.read_register(520, 1))
# switch = int(instrument.read_register(528, 1))
#
# reading = {
#         'rv': rv,
#         'temp': temp,
#         'press': press,
#         'switch': switch
# }
# print(reading)


def open_modbus_conn(port):
    if port is None:
        print('Com not selected')
    elif port == 'test':
        reading = {
            'rv': random.randint(30, 60),
            'temp': random.randint(19, 21),
            'press': random.randint(18, 20),
            'switch': 5000
        }
        return reading
    else:
        instrument = minimalmodbus.Instrument('' + port + '', 1)  # port name, slave address (in decimal)
        # instrument.serial.port  # this is the serial port name
        instrument.serial.baudrate = 115200  # Baud
        instrument.serial.bytesize = 8
        instrument.serial.parity = serial.PARITY_NONE
        instrument.serial.stopbits = 1
        instrument.serial.timeout = 0.2  # seconds
        # instrument.address  # this is the slave address number
        instrument.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode
        instrument.clear_buffers_before_each_transaction = True
        rv = int(instrument.read_register(512, 1))  # Registernumber, number of decimals
        temp = int(instrument.read_register(516, 1))
        press = int(instrument.read_register(520, 1))
        switch = int(instrument.read_register(528, 1))

        reading = {
            'rv': rv,
            'temp': temp,
            'press': press,
            'switch': switch
        }
        return reading


def serial_ports():
    ports = ['COM%s' % (i + 1) for i in range(256)]

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result