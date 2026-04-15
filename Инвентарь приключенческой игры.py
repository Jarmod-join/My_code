# Написать функцию, которая получает в качестве аргумента словарь-инвентарь игрока и выводит его в консоль.

inventory = {
    'Веревка': 1,
    'Факел': 6,
    'Золотая монета': 42,
    'Кинжал': 1,
    'Стрела': 12
}

def display_inventory(inv): #Довольно красиво получилось, однако мне кажется использование f'' я забуду, так как впервые использую
    all_num = 0
    lines = []
    
    for name,count in inv.items():
        lines.append(f'{name} - {count}')
        all_num += count

    lines.append(f'Всего предметов: {all_num}' )

    return '\n'.join(lines)

print(display_inventory(inventory))