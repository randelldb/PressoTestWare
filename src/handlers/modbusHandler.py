import minimalmodbus
import serial
from time import time, sleep


def open_modbus_conn(port):
    instrument = minimalmodbus.Instrument(port, 1)  # port name, slave address (in decimal)
    instrument.serial.port  # this is the serial port name
    instrument.serial.baudrate = 115200  # Baud
    instrument.serial.bytesize = 8
    instrument.serial.parity = serial.PARITY_NONE
    instrument.serial.stopbits = 1
    instrument.serial.timeout = 0.2  # seconds
    instrument.address  # this is the slave address number
    instrument.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode
    instrument.clear_buffers_before_each_transaction = True

    return instrument

def read_data(instrument):
    rv = instrument.read_register(512, 1)  # Registernumber, number of decimals
    temperature = instrument.read_register(516, 1)  # Registernumber, number of decimals
    pressure = instrument.read_register(520, 1)  # Registernumber, number of decimals
    switch = instrument.read_register(528, 1)  # Registernumber, number of decimals
    reading = {
        'rv': rv,
        'temp': temperature,
        'press': pressure,
        'swt': switch
    }
    return reading

open_conn = open_modbus_conn('COM6')
read_data = read_data(open_conn)
while True:
    print(read_data)
    sleep(0.2)