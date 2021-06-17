
from openpyxl import *


def ver_sheets(namesheet):
    excel_doc = load_workbook('C:\DatosF\partesproduccion.xlsm')
    sheet = excel_doc.get_sheet_by_name(namesheet)

    ultimafilahoja = sheet.max_row
    ultimafila = 1
    for r in range(1, ultimafilahoja):
        if not sheet.cell(row=r, column=3).value is None:
            ultimafila = r + 1
        else:
            break

    all_rows = sheet.iter_rows(min_row=1, max_row=ultimafilahoja,values_only=True)
    return all_rows, ultimafilahoja


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