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
# 1. Напишите скрипт(программу), которая будет удалять всех учеников и учителей из файлов с данными, не имеющих отношения
# к текущей школе и текущим класса (указанным в school.json)
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
    print("     MENU")
    print("1. Информация")
    print("2. Редактировать")
    print("3. Выйти")


def menu_2():
    print("     MENU > Информация")
    print("1. О классах")
    print("2. Об учениках")
    print("3. Об учителях")
    print("4. Назад")


def menu_3():
    print("     MENU > Информация > О классах")
    print("Все классы нашей школы")
    print("||", " || ".join(school_data['classes']), "||", '\n')


def menu_4():
    pass

# Load data
with open(location('data/school.json')) as f:
    school_data = json.load(f)

with open(location('data/Students.json')) as f:
    students_data = json.load(f)

# MAIN

clear()
# Про цветной текст ищите в гугле
print("\033[1;34m*\033[1;m" * 24)
print("\033[1;34m* Welcome to %s %s *\033[1;m" % (school_data['number'], school_data['type']))
print("\033[1;34m*\033[1;m" * 24)
menu_1()
choice = input(':')
if choice == '1':  # INFO
# Menu_1_1
    clear()
    welcome_1()
    menu_2()
    choice = input(':')
    if choice == '1':
    # Menu_1_1_1
        clear()
        welcome_1()
        menu_3()


    elif choice == '2':
    #Menu_1_1_2
        clear()
        welcome_1()

    elif choice == '3':
    #Menu_1_1_3
        clear()
        welcome_1()



elif choice == '2':
#Menu_1_2
    clear()
    welcome_1()

    if choice == '1':
    # Menu_1_2_1
        clear()
        welcome_1()


        choice = input(": ")
        if choice == '1':
        # Menu_1_2_1_1



    elif choice == '2':
    # Menu_1_2_2
        clear()
        print("*" * 24)
        print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
        print("*" * 24)

    elif choice == '3':
    #Menu_1_2_3
        clear()
        print("*" * 24)
        print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
        print("*" * 24)
        print("     MENU > Редактировать > Учителя")
        # Заглушка
        print("Данный пункт находится в разработке")
        input("Нажмите Enter для возврата в предыдущее меню")



elif choice == '3':
#Menu_1_3
    print("Goodbye")
else:
#Menu_Exeption
    print("Error: Not correct menu item")


