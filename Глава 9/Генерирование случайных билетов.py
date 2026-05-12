import random, copy, os
from pathlib import Path

us_state_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}

# 1) создать 35 разных билетов; +
# 2) создать для каждого билета по 50 вопросов с несколькими варианта­ми ответа, расположив их в случайном порядке; +
# 3) предоставить на каждый вопрос правильный ответ и три случайным образом выбранных неправильных ответа, располагая их в с лучайном порядке;+
# 4) записать билеты в 35 текстовых файлов; +
# 5) записать ключи ответов в 35 текстовых файлов.  +

ticket_palce = Path.home() / 'ticket'

try:
    os.makedirs(ticket_palce)
except FileExistsError:
    None

def create_ticket(ticket_palce):
    for i in range(35):
        questions, answer = create_list_questions(i + 1) # Передавть строчку  вопросов и ее просто добавить

        with open(ticket_palce / f'ticket_{i + 1}.txt', 'w', encoding='utf-8') as file_edit:
            file_edit.write(questions)

        with open(ticket_palce / f'ticket_{i + 1}_answer.txt', 'w', encoding='utf-8') as file_edit:
            file_edit.write(answer)

def create_list_questions(number_ticket):
    us_state_capitals_copy = copy.copy(us_state_capitals)
    total_string = f'Билет №{number_ticket}'
    total_answer = f'Билет №{number_ticket} Ответы'
    for i in range(50):
        question = random.choice(list(us_state_capitals_copy.keys()))
        us_state_capitals_answer_copy = copy.copy(list(us_state_capitals.values()))
        us_state_capitals_answer_copy.remove(us_state_capitals[question])
        answers = []
        for _ in range(3):
            choice = random.choice(us_state_capitals_answer_copy)
            us_state_capitals_answer_copy.remove(choice)
            answers.append(choice)
        answers.append(us_state_capitals[question])
        random.shuffle(answers)
        total_string += f'\n\nВопрос {i+1}.\nСтолица {question}?\n1. {answers[0]}\t2. {answers[1]}\t3. {answers[2]}\t4.{answers[3]}'
        total_answer += f'\n\nВопрос {i+1}.\nСтолица {question}?\nОтвет: {us_state_capitals_copy[question]}'
        del us_state_capitals_copy[question]
    return total_string, total_answer
    

create_ticket(ticket_palce)
