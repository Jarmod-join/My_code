import time, copy, random#, os

#Необходимо создать поле 6 на 6 единиц и расположить в них нн-ое количество клеток. Правила их распространения
# 1.Сущетвует два состояния клетки: Живой или мертвый.
# 2.Если у живой клетки есть два или три живых соседа, на следующем переходе она остается жить.
# 3.Если у мертвой клетки есть три живых соседа, она становится живой.
# 4.Если У живой клетки менее двух соседей она умирает.
# 5.Соседи считаются клетки в радиусе 3 на 3.

LIVE_CELLS_IN_ROUND = 0.4 #Процент заполнения клетками
LENGTH = 20
WIDTH = 20
DELAY = 0.5
DEAD = '░░'
LIVE = '██'

zone = [[DEAD for _ in range(WIDTH)] for _ in range(LENGTH)] # Эти 5 строк писала нейронка. Создание и заполнение списка
all_cells = [(y, x) for y in range(LENGTH) for x in range(WIDTH)] # 08.04.26. Я узнал как ими пользоваться возможно перепишу
live_positions = random.sample(all_cells, int(LENGTH * WIDTH * LIVE_CELLS_IN_ROUND)) # когда будет время
for y, x in live_positions:
    zone[y][x] = LIVE

def sys_chek(a,b,c,d): #Проверка на выход за границы
    if c == 0 and d == 0:
        return False
    if 0 <= a + c < LENGTH:
        if 0 <= b + d < WIDTH:
            return True
    return False

def chek_die():   # Нахождение живых клеток
    for y in range(len(zone)):
        for x in range(len(zone[y])):
            if zone[y][x] == LIVE:
                cell_die(y,x)

def chek_live():   # Нахождение живых клеток
    for y in range(len(zone)):
        for x in range(len(zone[y])):
            if zone[y][x] != LIVE:
                cell_grow(y,x)

def cell_die(y,x):  # Убийство клетки если < 2 соседей или > 4
    cell_num = 0
    for z in (-1, 0, 1):
        for c in (-1, 0, 1):
            if sys_chek(y, x, z, c):
                if zone[y + z][x + c] == LIVE:
                    cell_num += 1
    if cell_num not in (2,3):
        zone_hash[y][x] = DEAD

def cell_grow(y,x):  # Разрастание клетки если у нее больше 3 живых соседей
    cell_num = 0
    for z in (-1, 0, 1):
        for c in (-1, 0, 1):
            if sys_chek(y, x, z, c):
                if zone[y + z][x + c] == LIVE:
                    cell_num += 1
    if cell_num == 3:
        zone_hash[y][x] = LIVE

while True: #Вывод поля и сама реализация последовательности игры
    zone_hash = copy.deepcopy(zone)
    #os.system('cls' if os.name == 'nt' else 'clear') Если консоль поддерживает очистку то это пожалуй лучше на низких DELAY
    for l in range(20):
        print()
    for i in zone:
        print(''.join(i)) #Помогла нейронка(с красивым выводом, не знаю что такое функция .join() )
    chek_live()
    chek_die()
    zone = zone_hash
    time.sleep(DELAY)