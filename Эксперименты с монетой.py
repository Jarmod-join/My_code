import random, time
LEN_1 = 1000000 #Сколько делать бросков?
LIST22 = []
for _ in range(LEN_1): #Создаем список с последовательностью
    num = random.randint(0,1)
    LIST22.append(str(num))

def check_1(char): #Способ 1
    start = time.time()
    chel = 0
    for x in range(LEN_1 - 6):
        if LIST22[x] == char:
            if LIST22[x + 1] == char:
                if LIST22[x + 2] == char:
                    if LIST22[x + 3] == char:
                        if LIST22[x + 4] == char:
                            if LIST22[x + 5] == char:
                                chel += 1
                                continue
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
    end = time.time()
    return chel, end - start

def check_2(char_1, char_2): #Способ 2
    start = time.time()
    hashing = list()
    numeral_1 = 0
    numeral_2 = 0
    for x in range(LEN_1):
        hashing += LIST22[x]
        if len(hashing) > 6:
            del hashing[0]
        if ''.join(hashing) == char_1 * 6:
            numeral_1 += 1
        if ''.join(hashing) == char_2 * 6:
            numeral_2 += 1
    end = time.time()
    return 'Количество ' + char_1 + ' равно: ' + str(numeral_1) + '. Количество ' + char_2 + ' равно: ' + str(numeral_2) + '.', end - start

#print(check_1('0'))     Самое интересное что из-за веса .join и "скользящего списка" сумма 51 строки и 52 строки
#print(check_1('1'))                         по времени всегда будет < чем время 53.
print(check_2('0','1'))