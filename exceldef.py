

from openpyxl import *

def ver_sheets(namesheet):
    #wb = Workbook()
    excel_doc = load_workbook('C:\DatosF\partesproduccion.xlsm')
    sheet = excel_doc.get_sheet_by_name(namesheet)
    all_rows = sheet.iter_rows(min_row=1, max_row=10,values_only=True)
    return all_rows




# grab the active worksheet
#ws = wb.active

# Data can be assigned directly to cells
#ws['A1'] = 42

# Rows can also be appended
#ws.append([1, 2, 3])

# Python types will automatically be converted
#import datetime
#ws['A2'] = datetime.datetime.now()

# Save the file
#wb.save("sample.xlsx")