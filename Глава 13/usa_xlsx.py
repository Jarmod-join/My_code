# подсчитывать количество censusTract в каждом country;
# подсчитывать human, проживающего в каждом country;

import openpyxl
from pathlib import Path
full_docs = openpyxl.load_workbook('censuspopdata.xlsx')
docs = full_docs['Population by Census Tract']

# {country: [[censusTract,...,], human_number],...} 

def edit_dictionary():
    # TUPLE_FULL_LIST = docs['A2':'D55']
    TUPLE_FULL_LIST = docs['A2':'D72865']
    all_country = {}
    for line in TUPLE_FULL_LIST:
        if line[2].value not in all_country.keys():
            all_country[line[2].value] = [[],0]

        if line[0].value not in all_country[line[2].value][0]:
            all_country[line[2].value][0].append(line[0].value)
        
        all_country[line[2].value][1] = all_country[line[2].value][1] + line[3].value
    create_file(all_country)

def create_file(dictionary):
    with open(Path.cwd() / 'all_info.txt', 'w', encoding='utf-8') as folder:
        for i in dictionary.keys():
            folder.write(f'Округ {i}, Количество преписных районов: {len(dictionary[i][0])} Количество людей в округе: {dictionary[i][1]}\n')

edit_dictionary()