tableData = [['яблоки', 'апельсины', 'вишни', 'бананы'],
             ['Алиса', 'Боб', 'Кэрол', 'Дэвид'],
             ['собаки', 'кошки', 'лось', 'гусь']]
 
def check_most_large(text): # Ищем наиболее длинную строку по которой будет
    the_most_large = 0      # происходить выравнивание
    for i in range(len(text)):
        for k in text[i]:
            if the_most_large < len(k):
                the_most_large = len(k) 
    return the_most_large

def format_text(text,the_most_large): 
    last = [] 
    for i in range(len(text)): # Разбивает вложенные списки на списки
        lis = []
        for k in (text[i]): # Перебирает каждое слово
            lis.append(k.rjust(the_most_large)) # добавляет каждое слово с отступами в список lis
        lis = ' '.join(lis) # преобразует список lis в строку из набранных значений при переборе
        last.append(lis) # заносит в список значение всей строчки с отредактированными отступами
    return '\n'.join(last) # возращает весь преобразованный список соединяя его части вместе через \n

print(format_text(tableData,check_most_large(tableData)))