from PressoTestWare.Resources.SerialProcess import close_serial_connection, open_serial_connection, setup_comm_settings
from PressoTestWare.Resources.PrinterProcess import user_print_config
print("Presso Test Ware V 0.1 /n")
print("Setup Comm port settings /n")
print("---------------------------")
setup_comm_settings()
close_serial_connection()
print("Setup master printer: /n")
print("---------------------------")
user_print_config('master')
