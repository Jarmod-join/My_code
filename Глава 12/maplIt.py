#! python3
# mapIt.py - открывает в google map адрес записанный в аргументе или в буффере обмена

# 1) получать почтовый адрес из командной строки или буфера обмена;
# 2) открывать в браузере карту Google, соответствующую указанному адресу, считывать аргументы командной строки из списка sys.argv;

# 1) считывать аргументы командной строки из списка sys.argv;
# 2) считывать содержимое буфера обмена;
# 3) вызывать функцию webbrowser.open() для открытия браузера.

#python mapit.py [870 Valencia St, San Francisco, CA 94110] - arg
                #  улица и номер,      город,     шатат почтновый индекс
# https://www.google.com/maps/place/870+Valencia+St+San+Francisco+CA/
# Если арг не задан -> использовать буффер обмена
import webbrowser, pyperclip, sys

def main():
    address = check_arg() # Возращает строку
    webbrowser.open(f'https://www.google.com/maps/place/{address}')

def check_arg():
    if len(sys.argv) > 1:
        return ' '.join(sys.argv[1:])
    else:
        return pyperclip.paste()
    

main()