import time, sys

char = '*'
numb = 5
delay = 0.1

ins = True
k = 0

try:
    while True:
        print(' ' * k, end='')
        print(char * numb )
        time.sleep(delay)
        if ins:
            k = k + 1
            if k == 5:
                ins = False
        else:
            k = k - 1
            if k == 0:
                ins = True
except KeyboardInterrupt:
    exit()