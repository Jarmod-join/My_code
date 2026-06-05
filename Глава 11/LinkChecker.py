# Напишите программу, которая получает URL-адрес веб-страницы, аза­
# тем пытается загрузить каждую страницу, на которую там имеется ссылка.
# Программа должна помечать все страницы, для которых получен код со­
# стояния 404 “Страница не найдена”, и выводить на экран информацию о
# неработающих ссылках.

from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
import requests
from selenium.webdriver.firefox.options import Options

def main():
    # Находит все гипер ссылки и передает их в список
    # Открывает браузер

    firefox_options = Options()
    firefox_options.set_preference("security.fileuri.strict_origin_policy", False)

    url = 'https://ru.wikipedia.org/wiki/%D0%92%D0%BE%D0%B4%D0%BE%D1%80%D0%BE%D0%B4'
    with webdriver.Firefox(options=firefox_options) as browser:
        browser.get(url)
        browser.minimize_window()
        # Находит все эллементы которые имеют селектор гипер ссылки с атребутом rel
        # так как иначе может попасться переход по странице(а он нам зачем?)
        web_list = browser.find_elements(By.CSS_SELECTOR, 'a[href]')
        # Заносит заключенные в них ссылки
        links = []
        for href in web_list:
            link = href.get_attribute('href')
            if link and link.startswith(('http://', 'https://')):
                links.append(link)
        error, ok, error_list = open_windows(links)
    error_recording(error_list)
    print(f'Работа завершена!\nУспешно: {ok}\n Ошибок: {error}')
def open_windows(links):
    headers = {"User-Agent": "Mozilla/5.0"}
    error = 0
    ok = 0
    error_list = []
    # Открывает ссылки и ведет счет открывшихся и не открывшихся в случае ошибок добавляет их в текстовый файл с сылками

    for link in links:
        try: 
            web_site = requests.get(link, headers=headers, timeout=5)
            # Маленький анализ ссылок
            print(f'Успешно!: {link}')
            ok += 1
        except requests.RequestException as e:
            print(f'{e} Ошибка: {link}')
            error_list.append(link)
            error += 1

    return error, ok, error_list

def error_recording(error_list):
    # Отработка ошибок с созданием ошибочных ссылок 404
    if not error_list:
        return
    else:
        with open(Path.cwd() / 'Error_404.txt', 'w') as folder:
            for error in error_list:
                folder.write(error + '\n')
    # К слову можно добавить даты и тип ошибки в файле, а то не особо ясно с большим html файлом
main()