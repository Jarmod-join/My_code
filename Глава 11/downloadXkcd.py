# downloadXkcd.py - загружаем все копиксы от XKCD

import requests, os, bs4
from pathlib import Path

url_site = 'https://xkcd.com/235'
os.makedirs('xkcd', exist_ok=True)


def main(url):
    href = url_site[17:]
    while True:
        # Сделать открытие url_site
        web_site = requests.get(url)
        web_site.raise_for_status()
        now_dir = Path.cwd()
        # Сделать нахождение картинки
        web_site_bs4 = bs4.BeautifulSoup(web_site.text, 'html.parser')
        result = web_site_bs4.select('#comic') # Находит ссылку на картинку

        # Cкачивание картинки
        img = result[0].select('img')
        src = img[0].get('src')
        link = 'https:' + src
        print(link)
        with open(now_dir / 'xkcd' / f'picture_{href}.png', 'wb') as picture:
            imge = requests.get(link, stream=True)
            imge.raise_for_status()
            for data in imge.iter_content(100000):
                picture.write(data)

        # Сделать нахождение кнопки перехода
        result_next = web_site_bs4.select('ul.comicNav:nth-child(4) > li:nth-child(4) > a:nth-child(1)')
        tag = result_next[0]
        href = tag.get('href').strip('/')
        if href == '#':
            print('Готово!')
            return
        # Сделать изменение url_site на новый после перехода
        url = f'https://xkcd.com/{href}' 

main(url_site)

# P.S. Если конечно это кто то будет смотреть, но я отмечу проблемы этого кода.
# Мне не нравиться от слова совсем что он столь неадаптивный, в плане того что
# малейшее изменение на сайте приведет к его поломке, хотя как я понимаю это обычная
# практика в подобных вещах
# И еще один момент, на счет того как я получаю фото. Я так и не смог найти и в правду,
# хорошего варианта как получать ссылку на картинку, я в коде пользуюсь выделенной от автора.
# по большей это проблема именно автора, так как адрес по которому лежит картинка не соответствует
# ни с чем из содержимого страницы(частично с названием, разве что). Хотя если так подумать
# то нет ничего тяжелого что бы зайти на этот сайт и перейти по картинке, тем самым получить
# вкладку чисто с пикчей. Хотя может чего то просто не знаю. Но в ином случае, мой код 
# был бы намного лучше. :D

# Апдейт. Я угадал что все не так, так как нашел сылку на само изображение при его ввыоде на html,
# так что теперь я радуюсь и трясусь от счастья. К слову это не так уж и сложно все оказываеться,
# особенно если использовать теги