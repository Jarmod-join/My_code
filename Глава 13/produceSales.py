# produceSales.xlsx
import openpyxl

# 1. просматривать все строки в цикле;
# 2. изменять значения цены для чеснока, сельдерея и лимонов.

# Garlic  1,27
# Parsnips   1,19
# Asparagus  3,07

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active

PRICE_UPDATES = {'Garlic': '1,27',
                 'Parsnips': '1,19',
                 'Asparagus': '3,07'}

for row_num in range(2, sheet.max_row):
    produce_name = sheet.cell(row=row_num, column=1).value
    if produce_name in PRICE_UPDATES:
        sheet.cell(row=row_num,column=2).value = PRICE_UPDATES[produce_name]
wb.save('UPDproduceSales.xlsx')

        