import re

def my_strip(text, char=' '):
    char = re.escape(char)
    FILER = re.compile(fr'^[{char}]+|[{char}]+$')
    text = FILER.sub('', text)
    return(text)

string = 'asasasПривет мир!aass'
print(my_strip(string))
print(my_strip(string, 'as'))
# Пробелема в том что он во многом не может соблюдать порядок.
# В том же 'as' из за чего он удаляет и a и s но не as