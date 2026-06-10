# в качестве аргументов командной строки обозначим первое число буквой N, второе — буквой М.
# blankRowInserter.py N M file 
# С строки N - M пустых строк

import openpyxl, sys

start = int(sys.argv[1])
numberus_str = int(sys.argv[2])
file = sys.argv[3]

wb = openpyxl.load_workbook(file)
list_1 = wb.active

for i in range(numberus_str):
    for c in range(1, 5):
        r = start + i
        list_1.cell(row=c, column=r).value = None

wb.save(f'{file}_edit.xlsx')