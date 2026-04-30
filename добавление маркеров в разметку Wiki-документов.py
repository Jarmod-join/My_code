# Проект: добавление маркеров
# в разметку Wiki-документов

# Сало
# Покрытие
# Железы
# Голова

import pyperclip

# Создать функцию которая принимает буфер с уже разбитым текстом добовяет перед ними * и пробел после чего обновляет буфер

def edit_buff(buff):
    buff_list = buff.split('\n')
    for i in range(len(buff_list)):
        buff_list[i] = '* ' + buff_list[i]
    return '\n'.join(buff_list)

pyperclip.copy(edit_buff(pyperclip.paste()))