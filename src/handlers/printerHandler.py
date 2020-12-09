import tempfile
import win32api
import win32print

printer_name = "Brouwer Printer boven"
win32print.SetDefaultPrinter(printer_name)

# coding: utf-8

# ref: http://timgolden.me.uk/python/win32_how_do_i/print.html
# ref: http://docs.activestate.com/activepython/2.7/pywin32/win32api__ShellExecute_meth.html

pdf_file_name = 'test.html'
win32api.ShellExecute(0, "print", pdf_file_name, None, ".", 0)

# filename = "test.pdf"
# win32api.ShellExecute(
#     0,
#     "print",
#     filename,
#     #
#     # If this is None, the default printer will
#     # be used anyway.
#     #
#     '/d:"%s"' % win32print.GetDefaultPrinter(),
#     ".",
#     0
# )
