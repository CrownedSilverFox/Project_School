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
from utilities import clear, get_full_name, search, location


def welcome():
    print("*" * 24)
    print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
    print("*" * 24)


def menu_1():
    welcome()
    print("     MENU")
    print("1. Информация")
    print("2. Редактировать")
    print("3. Выйти")


def menu_1_1():
    welcome()
    print("     MENU > Информация")
    print("1. О классах")
    print("2. Об учениках")
    print("3. Об учителях")
    print("4. Назад")


def menu_1_1_1():
    global choice
    welcome()
    print("     MENU > Информация > О классах")
    print("Все классы нашей школы")
    print("||", " || ".join(school_data['classes']), "||", '\n')
    while True:
        class_room = input("Введите класс, для подробной информации по нему или Enter для возврата\n:")
        if not class_room:
            choice = 'menu_1_1()'
            menu_1_1()
            return
        if class_room in school_data["classes"]:  # FIXME(complete): сообщить, если выбран несуществующий класс
            print("\nИнформация по %s классу:" % class_room)
            # TODO(complete): вывести всех учеников и учителей указанного класса
            print("     Учителя: ...")
            for teacher in teachers_data:
                if teacher['class'] == class_room:
                    print('*' * 50)
                    print('* %s %s %s *' % (teacher['surname'], teacher['name'], teacher['middle_name']))
                    print('*' * 50)
            print("     Ученики: ...")
            for student in students_data:
                if student['class'] == class_room:
                    print('*' * 50)
                    print("     ", get_full_name(student))
                    print('*' * 50)
            # TODO*(complete): Сделать возврат в предыдущее меню(во всех местах программы).
            # TODO(complete):Выход из программы только по пункту "выйти"
        else:
            print('Выбран несуществующий класс')


def menu_1_1_2():
    welcome()
    print("     MENU > Информация > Об учениках")
    print("-" * 24)
    for class_room in school_data["classes"]:
        print("Ученики '%s' класса: " % class_room)
        for number, student in enumerate(search(students_data, class_room=class_room)):
            # FIXME(Complete): учесть(во всей программе), в файле могут быть ученики из других школ
            print("     %s)%s" % (number+1, get_full_name(student)))
            # TODO(complete): Добавить нумерацию учеников для каждого класса
    print('Ожидают принятия в школу:')
    for number, student in enumerate(search(students_data, class_room='')):
        print("     %s)%s" % (number, get_full_name(student)))
    print("-" * 24)
    _choice = '1'
    while _choice:
        _choice = input("Нажмите Enter для возврата в предыдущее меню")
    global choice
    choice = 'menu_1_1()'
    menu_1_1()


def menu_1_1_3():
    welcome()
    print("     MENU > Информация > Об учителях")
    print("-" * 24)
    for class_room in school_data["classes"]:
        print("Учителя, преподающие в '%s' классе: " % class_room)
        for number, teacher in enumerate(search(teachers_data, class_room=class_room)):
            print("     %s)%s" % (number+1, get_full_name(teacher)))
        print("-" * 24)
    _choice = '1'
    while _choice:
        _choice = input("Нажмите Enter для возврата в предыдущее меню")
    global choice
    choice = 'menu_1_1()'
    menu_1_1()


def menu_1_2():
    print("     MENU > Редактировать")
    print("1. Класс")
    print("2. Ученика")
    print("3. Учителя")


def menu_1_2_1():
    print("     MENU > Редактировать > Класс")
    print("     Классы: ")
    print("     ||", " || ".join(school_data['classes']), "||")
    print()
    print("1. Удалить существующий")
    print("2. Создать новый")
    print("3. Назад")  # TODO(completed): Реализовать ВСЕ(во всей программе) пункты 'назад'


def menu_1_2_1_1():
    globals(school_data, students_data, teachers_data)
    class_room = input("Введите класс: ")
    global choice
    while True:
        if class_room in school_data["classes"]:
            # TODO(complete): 1. Удалить класс из school.json
            school_data['classes'].remove(class_room)
            # TODO(complete): 2. Удалить класс у всех учителей
            map(teachers_data, lambda x: x['class'].remove(class_room))
            # TODO(complete):3 Заменить класс у всех учеников на '' (считается что ученик ожидает перевод в новый класс)
            for i, student in enumerate(students_data):
                if student['class'] == class_room:
                    students_data[i]['class'] = ''
            # TODO(complete): 4. Не забыть обновить информацию в файлах
            # TODO(complete):5 Сделать изменения в меню 'MENU > Информация > Об учениках' (вывести учеников без классов)
            break
        else:
            print('Вы ввели несуществующий класс')
            # TODO(complete): и предложить ввести класс повторно
            class_room = input('Введите корректный класс или нажмите Enter для возврата в пердыдущее меню\n:')
            if not class_room:
                choice = 'menu_1_2_1()'
                menu_1_2_1()
                return


def menu_1_2_2():
    welcome()
    print("     MENU > Редактировать > Ученика")
    for num, student in enumerate(students_data):
        print("%s) %s || %s" % (num+1, get_full_name(student), student['class']))
    student_num = int(input('Укажите номер ученика(или НОЛЬ, для создания нового): '))-1
    print()
    if student_num != 0:
        print("Вы выбрали %s " % get_full_name(students_data[student_num]))
        print('ID: %s\nКласс: %s\nДата рождения: %s' % (students_data[student_num]['id'], students_data[student_num]['class'], students_data[student_num]['birth_day']))
        # TODO: Указать выбранного ученика и отобразить по нему полную информацию
        # FIXME: не забыть обработать ввод номера несуществующего ученика
        print('1. Удалить ученика')
        print('2. Перевести в другой класс')
        print('3. Назад')
        # TODO: реализовать удаление и перевод ученика
    # TODO*: реализовать создание нового ученика с вводом всех необходимых параметров
    # TODO: не забыть, нельзя задать ученику несуществующий класс

# Load data
with open(location('data/school.json'), encoding='utf-8') as f:
    school_data = json.load(f)

with open(location('data/Students.json'), encoding='utf-8') as f:
    students_data = json.load(f)
students_data = [student for student in students_data if student['school'] == '67 школа']

with open(location('data/Teachers.json'), encoding='utf-8') as f:
    teachers_data = json.load(f)
teachers_data = [teacher for teacher in teachers_data if teacher['school'] == '67 школа']

# MAIN

menu_back_dict = {'menu_1()': '3', 'menu_1_1()': '4', 'menu_1_2_1()': '3'}

clear()
# Про цветной текст ищите в гугле
print("\033[1;34m*\033[1;m" * 24)
print("\033[1;34m* Welcome to %s %s *\033[1;m" % (school_data['number'], school_data['type']))
print("\033[1;34m*\033[1;m" * 24)
choice = 'menu_1()'
while True:
    print('———————————', choice, '———————————')
    clear()
    if menu_back_dict.get(choice[:-4]+'()') == choice[-3]:
        if choice != 'menu_1_3':
            print('Goodbye')
            break
        choice = choice[:-6]+'()'
    try:
        eval(choice)
    except NameError:
            print('Действие невозможно. Такого пункта нет или вы нажали Enter в корневом меню. Возврат в корневое меню')
            choice = 'menu_1()'
            menu_1()
    if choice != 'menu_1()':
        choice_1 = input('Нажмите Enter для возврата в предыдущее меню\n:')
    else:
        choice_1 = input(':')
    if choice_1:
        choice = choice[:-2]+'_'+choice_1+'()'
    else:
        choice = choice[:-4]+'()'
with open('C:/Users/CrownedSilverFox/PycharmProjects/Project_School/data/school.json', 'w', encoding='utf-8') as f:
    f.write(json.dump(school_data))

with open('C:/Users/CrownedSilverFox/PycharmProjects/Project_School/data/Students.json', 'w', encoding='utf-8') as f:
    f.write(json.dump(students_data))

with open('C:/Users/CrownedSilverFox/PycharmProjects/Project_School/data/Teachers.json', 'w', encoding='utf-8') as f:
    f.write(json.dump(teachers_data))