# Python.3.13_3.13.3568.0_x64
# В стакан кладется 13 кубов к примеру из них 6 зеленых 4 желтых 3 красных 
# Зеленый - 3 грани мозгов 2 грани следов 1 грань дробовик
# Желтый - 2 грани мозгов 2 грани следов 2 грани дробовиков
# Красный - 1 грань мознов 2 грани следов 3 грани дробовика
# 1. Если набрать 3 дробовика очки анулируются
# 2. Каждый бросок кубиков должен состоять из 3 случайных кубиков
# 3. Игрок может продолжать свой ход до тех пор пока игрок не сможет набрать кубиков из стакана до 3 или он не соберет 3 дробовика или сам не завершит ход
# 4. При продолжении хода игрок добирает недостоющие кубики(заменяя мозги или дробовики убирая их из хода игрока)
# если у него их меньше 3, при этом оставляя те на которых выпали следы
# 5. По итогам раунда все мозги полученные игроками прибавляются к итоговым балам игрока
# 6. Победа засчитывается если игрок набрал 13 или более мозгов по итогам раунда, в случае если у игроков равное количество мозгов проводится еще один
# раунд

import random, copy

LENGTH_MASSEGE = 58

GREEN_DICE =  ['B', 'B', 'B', 'T', 'T', 'S'] # T - trace; B - brain; S - shotgun.
YELLOW_DICE = ['B', 'B', 'T', 'T', 'S', 'S']
RED_DICE =    ['B', 'T', 'T', 'S', 'S', 'S']
# Значения на кубиках

BASE_STACK = [GREEN_DICE, GREEN_DICE, GREEN_DICE, GREEN_DICE, GREEN_DICE, GREEN_DICE, YELLOW_DICE, YELLOW_DICE, YELLOW_DICE, YELLOW_DICE, RED_DICE, RED_DICE, RED_DICE]
# Базовая конфигурация кубиков в стакане

def sys_new_stack(BASE_STACK): # Создание списка с стаканом игрока. Начало хода игрока
    round_stack = copy.copy(BASE_STACK)
    return round_stack

def sys_choice_of_the_dice(round_stack, hand_dice): # Случайный выбор n кубов для броска из стакана игрока
    for _ in range(3 - len(hand_dice)):
        number_dice = random.choice(round_stack)
        hand_dice.append(number_dice)
        round_stack.remove(number_dice) # Удаляет кубики после их взятия из стакана
    return round_stack, hand_dice

def sys_roll_of_the_dice(hand_dice, player): # Случайный бросок кубика c занесением значений в игрока и удалением кубиков из руки
    stack_char = []
    hand_dice_ = copy.copy(hand_dice)
    for dice in hand_dice_:
        random_char = random.choice(dice)
        if random_char != 'T':
            hand_dice.remove(dice)
        stack_char.append(random_char)
        count(random_char, player)
    return hand_dice, stack_char # новая рука, выпавшие значения

def count(char, player):
    if char == 'B':
        player[0] += 1
    elif char == 'S':
        player[1] += 1

def color_dice(round_stack): # Обычный вывод количества оставшихся кубиков
    green, yellow, red = 0, 0, 0
    for i in round_stack: 
        if i == GREEN_DICE: 
            green += 1 
        elif i == YELLOW_DICE: 
            yellow += 1 
        elif i == RED_DICE: 
            red += 1
    return green, yellow, red

def clean():
    for k in range(20):
        print()

def check_shot(player):
    if player[1] >= 3:
        player[0] = 0
        print('Вы собрали 3 дробовика, ваши очки анулированы!')
        input()
        return True
    return False

def check_brain(player):
    if player[0] >= 13: # Доделать она запускает ласт круг
        return True
    return False

def gambling(player, game_mode):
    round_stack = sys_new_stack(BASE_STACK) # Создание стакана
    player[1] = 0
    hand_dice = []
    green, yellow, red = color_dice(round_stack)
    while True:
        if len(round_stack) >= 3: # Проверка на количество кубов в стакане >= 3
            clean()
            print(f'Вы игрок {player[2]}'.center(LENGTH_MASSEGE, '='))
            print(f'Ваш счет:\tМозги: {player[0]}\tДробовики: {player[1]}')
            print(f'Осталось: \tЗеленых: {green}\tЖелтых: {yellow}\tКрасных: {red}')
            if game_mode == True:
                print('Завершающий круг!'.center(LENGTH_MASSEGE, ' '))
            choice = input('Хотите ли вы совершить ход?'.center(LENGTH_MASSEGE, ' '))
            if choice == '+':
                # Функционал
                round_stack, hand_dice = sys_choice_of_the_dice(round_stack, hand_dice) # Добор кубиков для начала хода
                hand_dice, stack_char = sys_roll_of_the_dice(hand_dice, player) # Бросок кубиков
                green, yellow, red = color_dice(round_stack)
                # Вывод информации
                print('Выпавшие значения: ' + ' '.join(stack_char))
                if check_shot(player):
                    break
            elif choice == '-':
                break
            else:
                continue
        else: # Иначе принудительное завершение
            print('Ваш стакан закончился!')
            break
    print('Вы завершаете свой ход!')
    input()
    return player

def check_players(player_list):
    score = 0
    player_win = ''
    for player in player_list:
        if player[0] >= score:
            score = player[0]
            player_win = player
    return score, player_win

def game(player_list):
    end_game = False
    while not end_game:
        for player_ in player_list: # Определяет один круг игры
            player = gambling(player_, end_game)
            game_mode = check_brain(player) # Когда у любого игрока 13 и боле мозгов передает True
            if game_mode:
                end_game = True
    print('Игра окончена!')
    score, player_win = check_players(player_list)
    print(f'По итогам игры победил игрок {player_win[2]}, поздравляем его он набрал {score}')


# Игроки
player_0 = [0, 0, 'player_0']
player_1 = [0, 0, 'player_1']

player_list = [player_0, player_1]

game(player_list)