# 2028_virt.py программа для эмуляции ходов через консоль игры 2028
# на сайте https://play2048.co/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyinputplus as pyip
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

GAME_COMMANDS = ('вверх', 'вниз', 'вправо', 'влево', 'exit')
# План:
# 1. Релизовать запуск сайта 
# 2. Внедрить цикл с вводом
# 3. Реализовать отправки команд
# 4. Реализовать получение результатов
def main():
    # Запуск сайта и передача аргумента в функции игры
    with webdriver.Firefox() as browser:
        browser.get('https://play2048.co/')
        score = game(browser)
    print(f'Ваш итоговый счет: {score}')

def game(browser):
    mess = 'Выберите куда вы хотите совершить свой ход:\n'
    actions = ActionChains(browser)
    while True:
        clear()
        user_choice = pyip.inputMenu(GAME_COMMANDS, numbered=True, prompt=mess)
        if user_choice == 'вверх':
            actions.send_keys(Keys.UP).perform()
        elif user_choice == 'вниз':
            actions.send_keys(Keys.DOWN).perform()
        elif user_choice == 'вправо':
            actions.send_keys(Keys.RIGHT).perform()
        elif user_choice == 'влево':
            actions.send_keys(Keys.LEFT).perform()
        elif user_choice == 'exit':
            # Надо как то на досуге, почитать про это, так как это довольно важная фигня особоенн если говорить про результат
            # Я столько raise наловил на этом моменте
            score = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="shrink-1 truncate"]')))
            score = score.text
            return score

def clear():
    for _ in range(20):
        print()

main()