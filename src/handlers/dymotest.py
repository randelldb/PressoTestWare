from win32com.client import Dispatch

labelCom = Dispatch('Dymo.DymoAddIn')
labelText = Dispatch('Dymo.DymoLabels')
isOpen = labelCom.Open('label.label')
selectPrinter = 'DYMO LabelWriter 450'
labelCom.SelectPrinter(selectPrinter)

labelText.SetField('VAR_TEXT', 'QGJ2148')

labelCom.StartPrintJob()
labelCom.Print(1,False)
labelCom.EndPrintJob()