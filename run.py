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

import json
from utilities import search, get_full_name, location, clear, save

school_data = []
students_data = []


def load_data():
    global school_data
    global students_data
    global teachers_data

    with open(location('data/school.json'), encoding='utf-8') as f:
        school_data = json.load(f)

    with open(location('data/Students.json'), encoding='utf-8') as f:
        students_data = json.load(f)

    with open(location('data/Teachers.json'), encoding='utf-8') as f:
        teachers_data = json.load(f)


def menu_do(menu_x, **kwargs):
    while True:
        clear()
        print("*" * 24)
        print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
        print("*" * 24)
        print("MENU > ", kwargs.get("sub_menu", ''))
        for number, el in enumerate(menu_x, start=1):
            print("%s. %s" % (number, el["text"]))
        choice = input(": ")
        if not choice:
            if menu != menu_x:
                return
            else:
                print('Если вы случайно нажали Enter, то нажмите 1')
                choice = input('Для выхода нажмите 2\n:')
                if choice == '1':
                    continue
                elif choice == '2':
                    end()
                    return
        menu_select = menu_x[int(choice-1)]
        if menu_select.get("do"):
            if menu_select["do"]():
                return
        else:
            menu_do(menu_select["sub_menu"], sub_menu=menu_select['text'])


def about_students():
    for class_room in school_data["classes"]:
        print("Ученики '%s' класса: " % class_room)
        for number, student in enumerate(search(students_data, class_room=class_room), start=1):
            # FIXME(Complete): учесть(во всей программе), в файле могут быть ученики из других школ
            print("     %s)%s" % (number, get_full_name(student)))
            # TODO(complete): Добавить нумерацию учеников для каждого класса
    print('Ожидают принятия в школу:')
    for number, student in enumerate(search(students_data, class_room='X'), start=1):
        print("     %s)%s" % (number, get_full_name(student)))
    print("-" * 24)
    input("Нажмите Enter для возврата в предыдущее меню\n:")


def about_classes():
    print("Все классы нашей школы")
    print("||", " || ".join(school_data['classes']), "||\n")
    input("Нажмите Enter для возврата в предыдущее меню\n:")


def about_teachers():
    for class_room in school_data["classes"]:
        print("Учителя, преподающие в '%s' классе: " % class_room)
        for number, teacher in enumerate(search(teachers_data, class_room=class_room)):
            print("     %s)%s" % (number+1, get_full_name(teacher)))
        print("-" * 24)
    input("Нажмите Enter для возврата в предыдущее меню\n:")


def delete_class():
    global school_data
    global students_data
    global teachers_data
    class_room = input("Введите класс\n:")
    while True:
        if class_room in school_data["classes"]:
            # TODO(complete): 1. Удалить класс из school.json
            school_data['classes'].remove(class_room)
            # TODO(complete): 2. Удалить класс у всех учителей
            map(lambda x: x['class'].remove(class_room), teachers_data)
            # TODO(complete):3 Заменить класс у всех учеников на '' (считается что ученик ожидает перевод в новый класс)
            for i, student in enumerate(students_data):
                if student['class'] == class_room:
                    students_data[i]['class'] = 'X'
            # TODO(complete): 4. Не забыть обновить информацию в файлах
            # TODO(complete):5 Сделать изменения в меню 'MENU > Информация > Об учениках' (вывести учеников без классов)
            save_all()
            input('Класс успешно удалён, нажмите Enter для возврата в предыдущее меню\n:')
            break
        else:
            print('Вы ввели несуществующий класс')
            # TODO(complete): и предложить ввести класс повторно
            class_room = input('Введите корректный класс или нажмите Enter для возврата в пердыдущее меню\n:')
            if not class_room:
                return


def create_class():
    global school_data
    class_room = input("Введите класс или Enter для возврата в предыдущее меню\n:")
    if class_room:
        school_data['classes'].append(class_room)
        save(school_data, 'school.json')
        input('Класс успешно создан, нажмите Enter для возврата в предыдущее меню\n:')
    else:
        return


def edit_create_student():
    for num, student in enumerate(students_data):
        print("%s) %s || %s" % (num+1, get_full_name(student), student['class']))
    student_num = (input('Укажите номер ученика(или НОЛЬ, для создания нового)\nНажмите Enter для возврата в предыдущее'
                         ' меню\n:'))
    if not student_num:
        return
    student_num = int(student_num)-1
    if student_num != -1:
        print("Вы выбрали %s " % get_full_name(students_data[student_num]))
        print('ID: %s\nКласс: %s\nДата рождения: %s' % (students_data[student_num]['id'],
                                                        students_data[student_num]['class'],
                                                        students_data[student_num]['birth_day']))
        # TODO: Указать выбранного ученика и отобразить по нему полную информацию
        # FIXME: не забыть обработать ввод номера несуществующего ученика
        print('1. Удалить ученика')
        print('2. Перевести в другой класс')
        print('3. Назад')
        choice_2 = input('Или нажмите Enter для возврата в предыдущее меню.\n:')
        if choice_2 == '1':
            delete_human(students_data[student_num]['id'])
        if choice_2 == '2':
            global students_data
            class_room = 'da'
            while not (class_room in school_data['classes']):
                class_room = input('Введите корректный класс или нажмите Enter для возврата в пердыдущее меню\n:')
                if not class_room:
                    return
            students_data[student_num]['class'] = class_room
        # TODO(complete): реализовать удаление и перевод ученика
        # TODO*(complete): реализовать создание нового ученика с вводом всех необходимых параметров
        # TODO(complete): не забыть, нельзя задать ученику несуществующий класс
    else:
        global students_data
        std_name = input('Введите ФИО ученика\n:')
        std_name = std_name.split()
        class_room = 'da'
        while not (class_room in school_data['classes']):
            class_room = input('Введите корректный класс или нажмите Enter для возврата в пердыдущее меню\n:')
            if not class_room:
                return
        birth_day = input('Введите дату рождения в формате ДД.ММ.ГГГГ\n:')
        std_id = students_data[-1]['id']+1
        students_data.append({'name': std_name[1], 'surname': std_name[0], 'middle_name': std_name[2],
                              'class': class_room, 'birth_day': birth_day, 'id': std_id, 'school': '67 школа'})


def delete_human(human_id, human_race='students'):
    if human_race == 'students':
        global students_data
        students_data = [human for human in students_data if human_id != human['id']]
    elif human_race == 'teachers':
        global teachers_data
        teachers_data = [human for human in teachers_data if human_id != human['id']]


def edit_teacher():
    input('Функция в разработке. Нажмите Enter для возврата в предыдущее меню\n:')


def end():
    global run
    print("Goodbye")
    run = False
    return True


def save_all():
    save(students_data, 'Students.json')
    save(teachers_data, 'Teachers.json')
    save(school_data, 'school.json')


load_data()

menu = [
    {
        "text": "Информация",
        "sub_menu": [
            {
                "text": "О классах",
                "do": about_classes
            },
            {
                "text": "Об учениках",
                "do": about_students,
            },
            {
                'text': 'Об учителях',
                'do': about_teachers
            },
            {
                "text": "Назад",
                "do": lambda: True
            }
        ]
    },
    {
        "text": "Редактировать",
        'sub_menu': [
            {
                'text': 'Редактировать класс',
                'sub_menu': [
                    {
                        'text': 'Удалить класс',
                        'do': delete_class
                    },
                    {
                        'text': 'Создать класс',
                        'do': create_class
                    },
                    {
                        "text": "Назад",
                        "do": lambda: True
                    }
                ]
            },
            {
                'text': 'Редактировать Ученика',
                'do': edit_create_student
            },
            {
                'text': 'Редактировать Учителя',
                'do': edit_teacher
            },
            {
                "text": "Назад",
                "do": lambda: True
            }
        ]
    },
    {
        "text": "Выход",
        "do": end
    }
]

run = True

menu_do(menu)
