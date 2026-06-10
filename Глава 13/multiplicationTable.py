# multiplicationTable.py

import openpyxl, sys
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font
# получает число N командной строки и создает таблицу умножения размером NxN в электрон­ ной таблице Excel
# В строке 1 и столбце А должны содержаться заголовки, отображаемые полужирным шрифтом.
# py multiplicationTable.ру 6

cfg = Font(bold=True)
CONST_SIZE_R = 26
CONST_SIZE_W = 8
def main(): # Создает лист, меняет имя и создает первые числа
    wb = openpyxl.Workbook()
    number = int(sys.argv[1])
    act_list = wb.active
    act_list.title = f'Таблица умножения. Число {number}'
    for i in range(1, number + 1):
        act_list[f'A{i + 1}'] = i # Столбик
        act_list[f'A{i + 1}'].font = cfg
        ab = get_column_letter(i + 1)
        act_list[f'{ab}1'] = i # Строка
        act_list[f'{ab}1'].font = cfg
    solution(number, act_list)
    size(act_list, number)
    wb.save('test_debug.xlsx')

def solution(number, act_list): # Расчитывает и заполняет области
    for row in range(1, number + 1): # Строка
        ab = get_column_letter(row + 1)
        for column in range(1, number + 1): # Столбец
            act_list[ab + str(column + 1)] = row * column
        act_list.freeze_panes = 'B2' # Чтобы на больших числах все было видно
        
def size(act_list, number):
    for r in range(1, number + 2):
        act_list.row_dimensions[r].height = CONST_SIZE_R

    for w in range(1, number + 2):
        c = get_column_letter(w)
        act_list.column_dimensions[c].width = CONST_SIZE_W

main()
