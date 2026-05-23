# Программа по поиску и выборочному удалению файлов превышающих более 100МБ памяти
# python clear_prog.py путь

import os, sys
from pathlib import Path

MB = 1024 * 1024
SEARCH_SIZE = 100

def main():
    path_test = check_directory(sys.argv[1])
    deleted = search(path_test)
    print(f'Программа успешно завершила свою работу!\nУдаленно {deleted} файлов.')

def check_directory(selected_directory):
    path_test = Path(selected_directory)
    if not path_test.exists():
        raise Exception('Данного пути не существует')
    return path_test
    
def search(selected_directory):
# Программа проверяет все папки по пути
    deleted = 0
    for folder_name, _, file_names in os.walk(selected_directory):
        print(f'Проверка {folder_name}')
        for file_name in file_names:
            folder_file = Path(folder_name) / file_name
            size_file = os.path.getsize(folder_file)
# Найденные файлы проверяються на 100МБ и больше
            if size_file >= SEARCH_SIZE * MB: 
                if user_choice(folder_file, size_file / MB):
                    deleted += 1
                    print('Успешное удаление!')
                else:
                    print('Пропущенно')
    return deleted

def user_choice(folder_file, size_file):
# Выводиться вопрос к пользователю да/нет удалить
    eds = 'МБ'
    if size_file >= 1024:
        size_file = size_file / 1024
        eds = 'ГБ'
    while True:
        user_request = input(f'Хотите ли вы удалить данный файл\n{folder_file}\nЕго вес составляет {round(size_file, 1)}{eds}?\n')
        if user_request.lower() in ['да', 'д']:
            del_file(folder_file)
            return True
        elif user_request.lower() in ['нет', 'не', 'н']:
            return False
        else:
            print('Повторите ваш ответ!\n')

def del_file(folder_file):
# Непосредственное удаление
    print(f'Удаление {folder_file}')
    # os.unlink(folder_file)

main()