# ДД/ММ/ГГГГ
# дни изменяются от 01 до 31
# месяцы — от 01 до 12
# а годы — от 1000 до 2999
# Если день или месяц задан одиночной цифрой, то добавляется начальный нуль.
# не обязано определять корректное количество дней для каждого месяца или високосного года

import re
def serch_date(text):
    REGEX_CODE = re.compile(r'(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/(1\d{3}|2\d{3})')
    check_date = REGEX_CODE.search(text)
    return check_date.group(1), check_date.group(2), check_date.group(3)

text = 'abc 15/04/2024 xyz'
day, month, year = serch_date(text)
print(f'Day: {day}\nMonth: {month}\nYear: {year}')
