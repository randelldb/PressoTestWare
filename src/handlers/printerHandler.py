import win32api
import win32print
from win32com.client import Dispatch


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


def print_label(selected_printer):
    printer_name = selected_printer
    win32print.SetDefaultPrinter(printer_name)

    pdf_file_name = 'test.html'
    win32api.ShellExecute(0, "print", pdf_file_name, None, ".", 0)
