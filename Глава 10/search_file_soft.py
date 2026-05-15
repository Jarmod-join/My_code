# Программа осуществляющая обход всех каталогов с вложенными папким и копирующая
# установлейные найденные файлы в новую папку(лучше наверное архив)

# План
# 1. Функция которая встречает пользователя просит ввести расширение и начальную папку для анализа, после передает в 2. и информирует
# 2. Фунция которая принимает 1, осуществляет обход всех папок и подпапок, и каждый найденный файл передает в 3
# 3. Функция которая получает файл и проверяет его расширение и передает ее в функцию которая добавляет в архив найденные файлы

# ПОМЕТКА! аккуратно если вы имеете много файлов pdf, mp3 или подобного рода, так как никто же не хочет отойти
# от компьютера и придя увидеть что когда вы выполняли поиск на всем диске вы внезапно видите что вес этого архива
# перевалил за 50GB и более

import zipfile, os, sys
from pathlib import Path

def validate_path(str_path):
# Проверка на валидность пути
    path_test = Path(str_path)
    if not path_test.exists():
        raise Exception('Переданный путь не существует!\n' + r'Для правильного ввода пути введите по форме Диск:\Папка\...')
    return path_test

def main():
# Информация и проверка аргументов
    try:
        if sys.argv[1].startswith('.'):
            extension = sys.argv[1]
        else:
            raise Exception('Для правильного ввода расширения введите .расширение!')
        
        selected_directory = validate_path(sys.argv[2])

    except IndexError:
        raise Exception(r'Введите необходимые аргументы .Расширение Диск:\Папка\...')
        
    current_directory = Path.cwd()
    add_file = search_files(extension, selected_directory, current_directory)
    print(f'Успешное выполнение!\nВсего файлов: {add_file}\nДобавлены в архив по пути {current_directory / 'search.zip'}')

def search_files(extension, selected_directory, current_directory):
# Пребирает все файлы в папках и при нахождении файла отправляет его в архив
    add_file = 0
    zip_file_dir = current_directory / 'search.zip'
    with zipfile.ZipFile(zip_file_dir, 'a') as zip_search:
        for folderName, _, filenames in os.walk(selected_directory):
            for filename in filenames:
                folder_file = Path(folderName) / filename
                if folder_file.suffix.lower() == extension:
                    if folder_file.name == "search.zip":
                        continue
                    zip_search.write(folder_file, arcname=folder_file.name, compress_type=zipfile.ZIP_DEFLATED)
                    print(folder_file)
                    add_file += 1
    return add_file
main()