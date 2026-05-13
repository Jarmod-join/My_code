import os, re, shutil
from pathlib import Path
import test_2
# Создать 1000 файлов с разными датами типа ММ-ДД-ГГГГ

REGEX = re.compile(r'([1-9]|1[0-2])-([1-9]|[12]\d|3[01])-(2\d{3})')
local = Path.cwd() / 'pink'

def creat(): # ММ-ДД-ГГГГ
    for c in range (12):
        for i in range(30):
            with open(local / f'{c+1}-{i+1}-2001', 'w'):
                pass

def main():
    create_temp_dir()
    for name_file in os.listdir(local):
        fix(name_file)
    cleanup_temp_dir()

def fix(name_file): # должен передать файл в Path
    mo = REGEX.fullmatch(name_file)
    if mo:
        date = mo.groups() # month
        shutil.move(local/name_file, local/'temp'/f'{date[1]}-{date[0]}-{date[2]}')
    else:
        return

def cleanup_temp_dir():
    for file_name in os.listdir(local/'temp'):
        shutil.move(local/'temp'/file_name, local)
    os.rmdir(local/'temp')

def create_temp_dir():
    os.makedirs(local/'temp')

main()
# creat()
# test_2.delll(local) Сугубая фунция для удобства

# Мне не особо нравиться этот код, по этому я его буду переделывать слегка. Вероятно после того как я пройду все главы я закрою пробелы в коде
# 13.05.2026