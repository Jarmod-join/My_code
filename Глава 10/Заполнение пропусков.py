# Программа создает фалы spam000.txt с нумерацией от 000 до 999, при этом добавляя пропуски.
# нейтрализатор пропусков по заданому файлу
from pathlib import Path
import os, random, shutil

directory = Path.cwd() / 'test'
def test_test():
    if directory.exists():
        pass
    else:
        Path.mkdir(directory)

def create_file_spam():
    for num in range(1000):
        number = counter(num)
        with open(directory / f'spam{number}.txt', 'w') as _:
            pass
    random_del(directory)

def random_del(directory):
    for _ in range(random.randint(100, 400)):
        file_list = os.listdir(directory)
        os.unlink(directory / random.choice(file_list))

def main():
    file_list = sorted(os.listdir(directory))
    number = 0
    for file in file_list:
        edit_num = file[4:7]
        now_couter = counter(number)
        if edit_num != now_couter:
            shutil.move(directory / file, directory / f'spam{now_couter}.txt')
        else:
            continue
        number += 1

def counter(number):
    number = str(number)
    if len(number) == 1:
        return '00' + number
    elif len(number) == 2:
        return '0' + number
    else:
        return number
    
test_test()
# create_file_spam() # Для создания фалов со случайными пропусками
main() # Для непосредственного переименования