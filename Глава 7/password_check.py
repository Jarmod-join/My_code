#  8 символов
# содержат символы в верхнем и нижнем регистрах
# хотя бы 1 цифра

import re

password = '123abcDExyz'
REGEX_FORM = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}')

if REGEX_FORM.search(password):
    print('Ваш пароль являеться хорошим!')
else:
    print('Ваш пароль не очень хорош(')