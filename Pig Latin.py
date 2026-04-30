# Pig Latin proggram
# если слово начинается с гласной, то в конце добавляется уау;
# если слово начинается с одной или нескольких согласных (напри
# мер, ch или gr), то они перемещаются в конец слова, и к ним добавля
# ется ау.
VOWELS = ('e', 'y', 'u', 'i', 'o', 'a')

def pig_latin(text):
    edit_text = text.split()
    for k in range(len(edit_text)): 

        if edit_text[k][0].lower() in VOWELS: # vowels
            edit_text[k] += 'YAY'

        else: # consonats
            if len(edit_text[k]) == 1: # Проверка на одиночный символ для согласных
                edit_text[k] = edit_text[k] + 'AY'
                continue
            
            consonats = 0
            for i in range(len(edit_text[k])):
                if edit_text[k][i].lower() not in VOWELS:
                    consonats += 1
                else:
                    break

            if consonats == len(edit_text[k]) - 1:
                edit_text[k] = edit_text[k] + 'AY'
                continue

            else:
                edit_text[k] = edit_text[k][consonats:] + edit_text[k][:consonats] + 'AY'
                continue

# Сделать учитывание знаков препинания

    return ' '.join(edit_text) # Возращает строчку 

def iik(text):
    text = text.split('.') # Разбивает предложение на части ограниченные точкой
    edc = []
    for toth in range(len(text)): # Цикл на каждую рабитую часть # Выполняет преобразования над каждой частью
        edc.append(pig_latin(text[toth])) # Заносит каждую измененную часть в список
    return '. '.join(edc) # Выполняет соединение списков через точку

in_text = "English a fsdsfx texts for beginners to. practice reading and c'omprehension online and for free"
print(iik(in_text))

# На деле основной смысл программа исполняет, но для работы с любым текстом с ' к примеру она не подходит(странный результат)
# или иная пунктуация. Когда то может доделаю, но основной смысл программы я создал, что и требовалось. 23.04.26