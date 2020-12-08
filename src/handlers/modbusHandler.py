import minimalmodbus
import serial
from time import time, sleep

instrument = minimalmodbus.Instrument('COM6', 1)  # port name, slave address (in decimal)

instrument.serial.port  # this is the serial port name
instrument.serial.baudrate = 115200  # Baud
instrument.serial.bytesize = 8
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 0.05  # seconds

instrument.address  # this is the slave address number
instrument.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode
instrument.clear_buffers_before_each_transaction = True

# Read temperature (PV = ProcessValue) #
temperature = instrument.read_register(15, 1)  # Registernumber, number of decimals

while True:
    sleep(0.5)
    print(temperature)
