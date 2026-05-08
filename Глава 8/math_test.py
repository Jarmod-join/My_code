import pyinputplus, time, random

def math(KOLVO=10, MIN_NUM=1, MAX_NUM=9):
    pravilnii = 0
    nipravilii = 0

    start = time.time()
    for i in range(KOLVO):
        first_num = random.randint(MIN_NUM,MAX_NUM)
        second_num = random.randint(MIN_NUM,MAX_NUM)
        otv = first_num * second_num
        print(f'Вопрос №{i}\n {first_num} * {second_num}')
        user_num = pyinputplus.inputNum()
        if user_num == otv:
            pravilnii += 1
        else:
            nipravilii += 1
    end = time.time()
    print(f'Вы прошли тест!\nПравильных ответов: {pravilnii}\nНеправильных ответов: {nipravilii}\nЗатраченное время: {end-start:.2f}')
math()