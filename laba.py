
import csv  
from collections import ChainMap

with open('s_voprosom_pro_blondinov.csv', newline='', encoding='UTF-8') as csvfile:
    
    reader = csv.DictReader(csvfile, delimiter=',')
    student_dict = ChainMap(*reader).maps
     
    questions = ('вы мужчина?', 
                 'вы из Питера?',
                 'ваш первый язык программирования - Python?', 
                 'вы курите? (не важно что)', 
                 'у вас плохое зрение?', 
                 'вы блондин?', 
                 'у вас карие глаза?', 
                 'день рождения до июля?', 
                 'вы сбили себе режим?', 
                 'вы хотели бы креативный вопрос в этой гугл форме?')
    
    res_dict = {}
    for num, q in enumerate(questions, 1):
        print(f"{num}: {q}", end='\n\n')
        answer = input("Введите да или нет >> ")
        print()
        res_dict[q] = answer
    
    for elem in student_dict:
        st_name = elem['ФИО']
        elem = {st_name: {k: v for k, v in elem.items() if k != 'ФИО' if k}}
        if elem[st_name] == res_dict:
            print(f"Вы загадали: {st_name}")
            break
    else:
        print('Нет совпадений')