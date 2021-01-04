import os

import win32api
import win32print

from src.models import MainCounter


def get_printers():
    printer_list = win32print.EnumPrinters(win32print.PRINTER_ENUM_NAME, None, 4)
    result = []
    for printer in printer_list:
        get_printer_name = {key: printer[key] for key in printer.keys() & {'pPrinterName'}}
        # Used the * to get rid of 'dict_values'
        result.append(*get_printer_name.values())

    return result


def print_main(selected_printer):
    printer_name = selected_printer
    win32print.SetDefaultPrinter(printer_name)

    pdf_file_name = 'my.label'
    win32api.ShellExecute(0, "print", pdf_file_name, None, ".", 0)


def print_label():

    get_certificate_id = MainCounter.query.get(1)
    count = get_certificate_id.count + 1

    #win32print.SetDefaultPrinter(selected_printer)

    import sys
    from datetime import datetime, timedelta
    from win32com.client import Dispatch
    dir_path = os.path.dirname(os.path.realpath(__file__))

    mylabel = 'final.label'
    now = datetime.now()
    next = now + timedelta(30)

    labelCom = Dispatch('Dymo.DymoAddIn')
    labelText = Dispatch('Dymo.DymoLabels')
    isOpen = labelCom.Open(mylabel)
    selectPrinter = 'DYMO LabelWriter 450'
    labelCom.SelectPrinter(selectPrinter)

    labelText.SetField('TESTO1', now.strftime('%Y/%m/%d'))
    labelText.SetField('TESTO2', count)

    labelText.SetField('TESTO3', now.strftime('%Y/%m/%d'))
    labelText.SetField('TESTO4', count)

    labelText.SetField('TESTO5', now.strftime('%Y/%m/%d'))
    labelText.SetField('TESTO6', count)

    labelCom.StartPrintJob()
    labelCom.Print(1, False)
    labelCom.EndPrintJob()
