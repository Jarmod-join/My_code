# Программа Mad Libs

# Напишите программу Mad Libs, которая считывает текстовые файлы
# и дает пользователю возможность ввести собственный текст в любом ме­сте файла,
# где встречается слово 'ПРИЛАГАТЕЛЬНОЕ', 'СУЩЕСТВИТЕЛЬНОЕ', 'НАРЕЧИЕ' или 'ГЛАГОЛ'.

import re
import pyinputplus as pyip

def main():
    '''Порядок выполнения и информация'''

    open_file = open(r'.\Mad_Libs.txt', 'r', encoding='utf-8') # Для выполнения он должен лежать около текста при этом запускаться в том же каталоге
    sentence = open_file.read()
    print(f'Изначальное предложение\n{sentence}')
    sentence = sentence.split('.')
    end_sentence = []
    for sen in sentence:
        end_sentence.append(analis_sentence(sen))
    end_sentence = '.'.join(end_sentence)
    print(f'Итоговое предложение\n{end_sentence}')
    open_file.close()

    # open_new_file = open('Mad_Libs_New.txt', 'w', encoding='utf-8')
    # open_new_file.write(end_sentence)
    # open_new_file.close()
    '''Создание нового файла, можно включить по приколу'''
    
def analis_sentence(sentence):
    '''Regex поиск маячков ПРИЛАГАТЕЛЬНОЕ, СУЩЕСТВИТЕЛЬНОЕ, НАРЕЧИЕ, ГЛАГОЛ'''

    patterns = [r'ПРИЛАГАТЕЛЬНОЕ', r'СУЩЕСТВИТЕЛЬНОЕ', r'ГЛАГОЛ', r'НАРЕЧИЕ']
    for pat in patterns:
        sentence = input_user(sentence, pat)
    return sentence

def input_user(sentence, pat):
    '''Реализация вставки слов в местах маячков'''

    def user_mass(pat):
        return pyip.inputStr(prompt=f'Введите слово за место {pat.group(0)}: ')
    pat = re.compile(pat)
    return pat.sub(user_mass, sentence)

main()