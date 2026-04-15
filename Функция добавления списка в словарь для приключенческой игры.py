# Реализация получения лута в инвентарь
inventory = {
    'Веревка': 1,
    'Факел': 6,
    'Золотая монета': 42,
    'Кинжал': 1,
    'Стрела': 12
}
dragon_loot = ['Золотая монета', 'Кинжал', 'Золотая монета', 'Золотая монета', 'Рубин']

def display_inventory(inv):
    all_num = 0
    lines = []

    for name, count in inv.items():
        lines.append(f'{name} - {count}')
        all_num += count

    lines.append(f'Всего предметов: {all_num}')

    return '\n'.join(lines)

def add_to_inventory(add_items, inv):
    for i in add_items:
        inv[i] = inv.get(i, 0) + 1

add_to_inventory(dragon_loot, inventory)
print(display_inventory(inventory))