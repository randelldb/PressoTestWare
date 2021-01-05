import minimalmodbus
import serial
from time import time, sleep


def open_modbus_conn(port=None):
    if port is None:
        print('Com not selected')
    else:
        try:
            instrument = minimalmodbus.Instrument(port, 1)  # port name, slave address (in decimal)
            #instrument.serial.port  # this is the serial port name
            instrument.serial.baudrate = 115200  # Baud
            instrument.serial.bytesize = 8
            instrument.serial.parity = serial.PARITY_NONE
            instrument.serial.stopbits = 1
            instrument.serial.timeout = 0.2  # seconds
            #instrument.address  # this is the slave address number
            instrument.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode
            instrument.clear_buffers_before_each_transaction = True
            return instrument
        except:
            print('Select a valid com port')



def read_data():
# def read_data(instrument):
    # rv = instrument.read_register(512, 1)  # Registernumber, number of decimals
    # temperature = instrument.read_register(516, 1)  # Registernumber, number of decimals
    # pressure = instrument.read_register(520, 1)  # Registernumber, number of decimals
    # switch = instrument.read_register(528, 1)  # Registernumber, number of decimals
    # reading = {
    #     'rv': rv,
    #     'temp': temperature,
    #     'press': pressure,
    #     'swt': switch
    # }

    reading = {
        'rv': 40,
        'temp': 20,
        'press': 8,
        'swt': 1
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
