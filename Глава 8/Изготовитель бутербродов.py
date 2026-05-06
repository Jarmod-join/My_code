# Изготовитель бутербродов
# 1.Используйте функцию inputMenu () для определения типа хлеба: цельнозерновой, белый или ржаной.
# 2.Используйте функцию inputMenu () для определения типа белкового продукта: курица, индейка, ветчина или тофу.
# 3.Используйте функцию inputYesNo (), чтобы спросить, хочет ли поль­зователь добавить сыр.
# 4.Если пользователь ответил утвердительно, используйте функцию inputMenu (), чтобы узнать тип сыра: чеддер, швейцарский или моца­релла.
# 5.Используйте функцию inputYesNo (), чтобы узнать у пользователя, хочет ли он добавить майонез, горчицу, салат или помидор.
# 6.Используйте функцию input Int (), чтобы узнать, сколько бутербро­дов хочет пользователь. Убедитесь в том, что это число не меньше 1.

# Придумайте цены для каждого из параметров бутерброда, и пусть про­грамма отобразит общую стоимость после того, как пользователь сделает свой выбор.

import pyinputplus as pyip

bread_options = {
    'Цельнозерновой (25 рублей)': 25,
    'Белый (20 рублей)': 20,
    'Ржаной (18 рублей)': 18
}

protein_options = {
    'Курица (60 рублей)': 60,
    'Индейка (70 рублей)': 70,
    'Ветчина (55 рублей)': 55,
    'Тофу (50 рублей)': 50
}

cheese_options = {
    'Чеддер (30 рублей)': 30,
    'Швейцарский (35 рублей)': 35,
    'Моцарелла (28 рублей)': 28
}

extras_options = {
    'Майонез (10 рублей)': 10,
    'Горчица (8 рублей)': 8,
    'Салат (12 рублей)': 12,
    'Помидор (15 рублей)': 15
}

def start():
    massage = '''Добро пожаловать в симулятор изготовления бутербродов!
Вам будет по очереди будет предложен список, в котором
вы будите вольны самостоятельно собрать ваш бутерброд
И так начнем?\n'''
    user_choice = pyip.inputYesNo(yesVal='Да', noVal='Нет', prompt=massage)
    if user_choice == 'Нет':
        return
    else:
        buter, price, kolw = main()
    print('Ваш бутерброд состоит из:\n' + '\n'.join(buter) + f'\nКоличество: {kolw}\nИтоговая цена: {price * kolw}\nПриятного вам аппетита!')

def main():
    buter = []
    price = 0
    buter, price = choice_all(buter, price, bread_options, 'Сперва выберем хлеб\n')
    buter, price = choice_all(buter, price, protein_options, 'Затем выберем протэинчик\n')
    user_choice = pyip.inputYesNo(prompt='Хотите ли вы добавить сыр?\n', yesVal='Да', noVal='Нет')
    if user_choice == 'Да':
        buter, price = choice_all(buter, price, cheese_options, 'После выберем сыр\n')
    user_choice = pyip.inputYesNo(prompt='Хотите ли вы выбрать добавки?\n', yesVal='Да', noVal='Нет')
    if user_choice == 'Да':
        buter, price = choice_all(buter, price, extras_options, 'И наконец выберем добавочки\n', True)
    kolw = pyip.inputNum(prompt='Сколько вы хотите таких бутербродов?\n', min=1)
    return buter, price, kolw

def choice_all(buter, price, options, massage, extras=False):
    while True:
        user_choice = pyip.inputMenu(list(options.keys()), prompt=massage, numbered=True)

        buter.append(user_choice)
        price += options.get(user_choice)

        if extras == False:
            return buter, price
        
        if pyip.inputYesNo(prompt='Не хотите ли вы добавить еще чего то?\n', yesVal='Да', noVal='Нет') == 'Нет':
            return buter, price

start()