import time, random
MIN = 1
MAX = 9
def math_game():
    plus_kryto = 0
    for i in range(10):
        start = time.time()
        error = 0
        print(f'Задание №{i+1}')
        first_number = random.randint(MIN, MAX)
        second_number = random.randint(MIN, MAX)
        otv = first_number * second_number
        while True:
            user_num = input(f'{first_number} * {second_number} = ')
            try:
                user_num = int(user_num)
                break
            except ValueError:
                print('Введите число!\n')
        while True:
            if user_num != otv:
                print('Ответ неправильный!\n')
                error += 1
                user_num = input(f'{first_number} * {second_number} = ')
                if error >= 2:
                    print('Неправильный ответ переходим к следующему')
                    break
            else:
                print('Правильный ответ!\n')
                end = time.time()
                if end-start <= 8:
                    plus_kryto += 1
                else:
                    print('Время истекло!')
                break
    print(f'Вы прошли тест\nПравильных ответов: {plus_kryto}')
math_game()