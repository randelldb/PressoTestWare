import random

import minimalmodbus

minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True
import serial
import time

instrument = {}


def opennModbus(port='COM9'):
    try:
        print('openmodbus')
        global instrument
        instrument = minimalmodbus.Instrument(port, 1, minimalmodbus.MODE_RTU)
        instrument.serial.baudrate = 115200
        instrument.serial.bytesize = 8
        instrument.serial.parity = serial.PARITY_NONE
        instrument.serial.stopbits = 1
        instrument.serial.timeout = 0.2  # 0.2 seconds
        instrument.clear_buffers_before_each_transaction = True
        instrument.close_port_after_each_call = True
        # instrument.debug = True
    except:
        print('Error in communication')


def readModbus():
    global instrument
    if instrument is None:
        opennModbus()
    try:
        rv = instrument.read_register(512, 2, signed=True)
        temp = instrument.read_register(516, 2, signed=True)
        press = instrument.read_register(520, 2, signed=True)
        switch = instrument.read_register(528, 2, signed=True)

        reading = {
            'rv': rv + random.randint(1, 5),
            'temp': temp + random.randint(1, 5),
            'press': press + random.randint(1, 5),
            'switch': switch + random.randint(1, 5)
            # 'rv': random.randint(1, 5),
            # 'temp': random.randint(1, 5),
            # 'press':random.randint(1, 5),
            # 'switch': random.randint(1, 5)
        }
        return reading
    except:
        # print('Error in Reading registers')
        pass


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
