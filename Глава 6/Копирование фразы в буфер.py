import pyperclip # Выполняет основную функцию
def clean(): # Костыль. Очищает консоль
    for i in range(50):
        print()

def viz_list(list_answer):
    for j,k in list_answer.items():
        print(f'• {j} - {k}')

def main(list_answer):  #Основная функция входа в программу
    while True:
        clean()
        hi_user()
        choice = input()
        if choice == '1': # Переход в режим редактирования
            edit_list_answer(list_answer)
        elif choice == '2': # Переход в рабочий блок
            copy_work(list_answer)
        elif choice == '3': # Кастомный вывод словаря
            clean()
            viz_list(list_answer)
            input("Нажми Enter, чтобы продолжить...")
        elif choice == '4':
            break
        else:
            print('Повторите еще раз, мы вас не поняли!')

        
def edit_list_answer(list_answer): #Менюшка режима редактирования
    while True:
        clean()
        print('''
Что вы хотите сделать?
1. Добавить значение
2. Удалить значение
3. Выйти из режима редактирования
''')
        choice = input()
        if choice == '1':
            add_list_answer(list_answer)
        elif choice == '2':
            del_list_answer(list_answer)
        elif choice == '3':
            return
        else:
            print('Я тебя не понял повтори еще раз!')


def add_list_answer(list_answer): #Функция добавления в словарь нового значения с ключем
    clean()
    choice_M = input('Введите вставляемое значение: ')
    choice_K = input('Введите сокращенное значнение: ').lower()
    choice = input('Вы уверены?(н\д) ')
    if choice.lower() in ['д','да']:       
        list_answer[choice_K] = choice_M
        print(f'Значение от ключа "{choice_K}" было успешно добавленно!')
        print('Успешно добавлено!')
        input("Нажми Enter, чтобы продолжить...")
    else:
        print('Давайте попробуем еще раз!')


def del_list_answer(list_answer): #Функция удаления существующего значения с ключем
    clean()
    viz_list(list_answer)
    while True:
        choice = input('\nКакое значение вы хотите удалить? ')
        if choice == 'none':
            break
        try:
            print(f'Значение от ключа "{choice}" было успешно удаленно!')
            del list_answer[choice]
            input("Нажми Enter, чтобы продолжить...")
            break
        except KeyError:
            print('Данного значения нет в словаре!')


def copy_work(list_answer): #Рабочий блок копирования
    while True:
        clean()
        print('Вводите краткое слово и мы будет копировать ответ.\n"ex" если вы хотите выйти\n')
        viz_list(list_answer)
        choice = input()
        if choice.lower() == 'ex':
            return
        try:
            pyperclip.copy(list_answer[choice])
            print(f'Значние от ключа "{choice}" успешно скопированно!')
            input("Нажми Enter, чтобы продолжить...")
        except KeyError:
            print('Неверное значение ключа. Попробуйте еще раз')
            input("Нажми Enter, чтобы продолжить...")


def hi_user(): #Главная навигационная информация для пользователя
    prest = '''
Привет!
Это программа для быстрых ответов в буфере копирования.
Введите значение соответствующее вашим требованиям:
1. Обновить базовый список
2. Приступить к работе
3. Отобразить текущий список
4. Выйти из программы
'''.strip().split('\n')
    for i, line in enumerate(prest):
        if i == 0:
            print(line.center(55, '='))
        else:
            print(line.ljust(55))


base_list_answer = {'привет': 'Привет как ты там?', 'занят': 'У меня тута жесть позже раскажу'} #Базовый словарь
main(base_list_answer) #Функция с аргументов в виде словаря(база)