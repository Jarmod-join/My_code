import pyperclip, shelve, sys, os

# mcd.pyw - программа для реализации расширенного буфера обмена

# Использование py.exe mcd.pyw save <ключевое слово> - сохраняет текущий буфер с указанным ключем
# Использование py.exe mcd.pyw list - передает в буфер обмена список всех используемых ключей
# Использование py.exe mcd.pyw <ключевое слово> - вставляет в текущий буфер обмена указанное значение по ключу
# Использование py.exe mcd.pyw del <ключевое слово> - удаляет ключ-аргумент со значением
# Использование py.exe mcd.pyw delete - удаляет ВСЕ ключ-аргумент со значением

data_file = shelve.open('data_copy')

def main():
    '''Осуществляет проверку аргументов'''
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        save()
    
    if len(sys.argv) == 2 and sys.argv[1].lower() == 'list':
        keys_list()

    elif len(sys.argv) == 2 and sys.argv[1] not in ['list', 'delete']:
        paste(sys.argv[1])

    elif len(sys.argv) == 2 and sys.argv[1] == 'delete':
        delete_all_data()
        return # Костыль что бы два раза не закрывать файл

    elif len(sys.argv) == 3 and sys.argv[1] == 'del':
        if sys.argv[2] not in data_file.keys():
            print('Error, unknown key!')
            return
        else:
            delete(sys.argv[2])

    data_file.close()

def save():
    '''Реализует сохранение буфера по аргументу после save'''
    data_file[sys.argv[2]] = pyperclip.paste()
    print('Сохранено!')

def keys_list():
    '''Реализует вставку в буфер всего списка ключей'''
    print('\n'.join(data_file.keys()))

def paste(massage):
    '''Реализует вставку сохраненого сообщения по ключ-аргументу'''
    pyperclip.copy(data_file[massage])
    print(f'Значение по ключу {massage} успешно вставленно!')

def delete(massage):
    '''Реализация чистки data_file по ключ-аргументу'''
    del data_file[massage]
    print('Успешное удаление!')

def delete_all_data():
    data_file.close()
    os.remove('data_copy')
    print('БД успешно удалена!')
    
main()