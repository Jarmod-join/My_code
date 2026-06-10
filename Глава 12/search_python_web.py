# 1) получать из аргументов командной строки ключевые слова, по кото­рым должен быть выполнен поиск;
# 2) извлекать страницу с результатами поиска;
# 3) открывать каждый результат в отдельной вкладке браузера.

# 1) читать аргументы командной строки из списка sys . argv;
# 2) извлекать страницу с результатами поиска с помощью модуля requests;
# 3) находить ссылки для каждого результата поиска;
# 4) вызывать функцию webbrowser. open () для открытия браузера.

import sys, webbrowser, requests, bs4

# Как можно догодаться этот проект не получился успешным если кто то уже пробовал нечто подобное делать XD

def main():
    # читать аргументы командной строки из списка sys . argv;
    # python test.py ключевое_слово 
    if len(sys.argv) == 1:
        raise Exception('Введите аргумент для поиска!')
    request = sys.argv[1:]
    request = '+'.join(request)
    web_search('game')

def web_search(request):
    # Открытие страницы с результатами поиска
    headers = {"User-Agent": "Mozilla/5.0"}	
    web_site = requests.get(f'https://pypi.org/search/?q={request}', headers=headers)
    web_site.raise_for_status()
    # Поиск ссылок по: .unstyled > li:nth-child(1) > a:nth-child(1)
    web_site_bs4 = bs4.BeautifulSoup(web_site.text, 'html.parser')
    results = web_site_bs4.select('a.package-snippet') # Тут надо работать, но на рабочем сайте
    # for r in results[:5]:
    #     print(r.text)
    #     print(r.get('href'))
    open_web_site(results)

def open_web_site(results):
    # Открытие первых n вкладок
    for result in results:
        webbrowser.open(f'https://pypi.org{result}')


main()