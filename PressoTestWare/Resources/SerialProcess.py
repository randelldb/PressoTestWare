import serial

def close_serial_connection():
    serial.close()


def open_serial_connection(port, baudrate):
    # Open serial connection
    ser = serial.Serial(
        port=port, \
        baudrate=baudrate, \
        parity=serial.PARITY_NONE, \
        stopbits=serial.STOPBITS_ONE, \
        bytesize=serial.EIGHTBITS, \
        timeout=1)

    print("connected to com port: " + ser.portstr)

    while True:
        s = ser.readline()
        print(s)


def setup_comm_settings():
    port = input("Enter Port: ")
    baudrate = input("Enter Baudrate: ")

    open_serial_connection(port, baudrate)
