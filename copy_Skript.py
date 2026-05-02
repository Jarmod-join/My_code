import pyperclip, re
WORK_MOD = 1
def phones_number(text):
    phone_number_filter = re.compile(r'\+?\d?\s?[-.(]?\d{3}[-.)]?\s?\d{3}[-.]?\s?\d{2}[-.]?\s?\d{2}')
    find_list = phone_number_filter.findall(text)
    return find_list

def email_number(text):
    email_number_filter = re.compile(r'[\w\.\-\+\=]+@[\w\-\.]+\.\w+')
    find_list = email_number_filter.findall(text)
    return find_list

user_text = pyperclip.paste()
number_list, email_list  = phones_number(user_text), email_number(user_text)
if WORK_MOD == 0:
    print('Найденные номера в тексте:\n' + '\n'.join(number_list))
    print('Найденные почты:\n' + '\n'.join(email_list))
elif WORK_MOD == 1:
    pyperclip.copy('\n'.join(number_list) + '\n'.join(email_list))