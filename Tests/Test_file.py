# *********
# Задание
# *********
# Допишите код програмы в соответствии с примечаниями (TODO и FIXME) в коде программы
# Реализовать нужно только те пункты меню, о которых сказано в примечаниях
# Все неработающие пункты(если такие останутся) пометьте каким-нить символом(например *) и сделайте к ним заглушки
# TОDО-шки не удаляйте, а меняйте TODO --> TODO(complete)
# Меняйте структуру программы, если это нужно
# Дописывайте вспомогателные функции
# Постарайтесь убрать существующие дублирования кода(где это возможно) и избежать дальнейших повторений
# TODO* - наиболее сложные задачи

# *********
# Доп. Задания (для желающих и тех, у кого осталось время)
# *********
# 1. Напишите скрипт(программу), которая будет удалять всех учеников и учителей из файлов с данными,
# не имеющих отношения к текущей школе и текущим класса (указанным в school.json)
# 2. Сделайте функцию обертку, для удобного вывода цветного текста
# 3. Разукрасьте текст программы, сделав его удобнее для восприятия

import os
import json
from utilities import location, clear, get_full_name, search


def welcome_1():
    print("*" * 24)
    print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
    print("*" * 24)


def menu_1():
    welcome_1()
    print("     MENU")
    print("1. Информация")
    print("2. Редактировать")
    print("3. Выйти")


def menu_1_1():
    welcome_1()
    print("     MENU > Информация")
    print("1. О классах")
    print("2. Об учениках")
    print("3. Об учителях")
    print("4. Назад")


def menu_1_1_1():
    global choice
    welcome_1()
    print("     MENU > Информация > О классах")
    print("Все классы нашей школы")
    print("||", " || ".join(school_data['classes']), "||", '\n')
    while True:
        class_room = input("Введите класс, для подробной информации по нему \n:")
        if not class_room:
            return
        if class_room in school_data["classes"]:  # FIXME(complete): сообщить, если выбран несуществующий класс
            print("\nИнформация по %s классу:" % class_room)
            # TODO(complete): вывести всех учеников и учителей указанного класса
            print("     Учителя: ...")
            for teacher in teachers_data:
                print('*' * 50)
                print('* %s %s %s *' % (teacher['surname'], teacher['name'], teacher['middle_name']))
                print('*' * 50)
            print("     Ученики: ...")
            for student in students_data:
                print('*' * 50)
                print('* %s %s %s *' % (student['surname'], student['name'], student['middle_name']))
                print('*' * 50)
            choice = input("Нажмите Enter для возврата в предыдущее меню\n:")
            # TODO*(complete): Сделать возврат в предыдущее меню(во всех местах программы).
            # TODO(complete?):Выход из программы только по пункту "выйти"
        else:
            print('Выбран несуществующий класс')


def menu_4():
    pass

# Load data
with open(location('data/school.json')) as f:
    school_data = json.load(f)

with open(location('data/Students.json')) as f:
    students_data = json.load(f)

with open(location('data/Teachers.json')) as f:
    teachers_data = json.load(f)

# MAIN

clear()
# Про цветной текст ищите в гугле
print("\033[1;34m*\033[1;m" * 24)
print("\033[1;34m* Welcome to %s %s *\033[1;m" % (school_data['number'], school_data['type']))
print("\033[1;34m*\033[1;m" * 24)
choice = 'menu_1()'
while True:
    eval(choice)
    choice_1 = input('Нажмите Enter для возврата в предыдущее меню\n:')
    if choice_1:
        choice = choice[:-2]+'_'+choice_1+'()'
    else:
        choice = choice[:-4]
