spam = ['яблоки', 'бананы', 'тофу', 'коты']

# 'эллемент'.join(списко с элементами) *Дает ошибку если список пуст

def check(item):
    if len(item) == 0:
        return ('Empty list')
    if len(item) == 1:
        return ''.join(item) + '.'
    elif len(item) == 2:
        return ' и '.join(item) + '.'
    else:
        return ', '.join(item[:-1]) + ' и ' + item[-1] + '.'

def check_old(item):
    viz = str()
    if len(item) == 1:
        for x in range(len(item)):
            char = '.'
            viz += item[x] + char
    elif len(item) == 2:
        for x in range(len(item)):
            char = ' и '
            if x == 1:
                char = '.'
            viz += item[x] + char
    else:
        for x in range(len(item)):
            char = ', '
            if x == len(item) - 1:
                char = '.'
            if x == len(item) - 2:
                char = ' и '
            viz += item[x] + char
    return viz

print(check(spam))

