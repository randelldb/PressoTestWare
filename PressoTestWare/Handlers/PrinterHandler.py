# https://smallbusiness.chron.com/sending-things-printer-python-58655.html

import os
import sys
import win32print


def user_print_config(printer_type):
    if type == 'master':
        printer_name = input("Enter name of the master printer")
        setup_master_printer(printer_name)
    else:
        printer_name = input("Enter name of the label printer")
        setup_label_printer(printer_name)


def setup_master_printer():
    printer_name = 'test'
    p = win32print.OpenPrinter(printer_name)
    job = win32print.StartDocPrinter(p, 1, ("test of raw data", None, "RAW"))
    print('selected printer' + printer_name)


def setup_label_printer():
    pass
