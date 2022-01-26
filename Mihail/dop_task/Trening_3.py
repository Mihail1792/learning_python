# Почитать про *args, **kwargs
# property, classmethod, staticmethod
# mixin
# инструкция raise

# посмотреть задания на почте

#
# class Person:
#
#     def __init__(self, first_name: str, last_name: str):
#         self.first_name = first_name
#         self.last_name = last_name
#
#
#
#     @property
#     def full_name(self):
#         return f'name: {self.first_name}, last_name: {self.last_name}'
#
# person_1 = (
#     'Zubovich',
#     'Illia',
# )

# person1 = {
#     'last_name': 'Zubovich',
#     'first_name': 'Illia',
# }
#
# illia = Person(*person_1)
# illia.age = 5
# print(illia.full_name)
# print(illia.age)
#
# illia.first_name = "fdfdf"
# print(illia.full_name)


# a_dict = {1: "one", 3: "three", 2: "two"}
# k = a_dict.keys()
# print(k)
#
# k = sorted(k)
# for key in k:
#     print(key)

# i = 0
# while i <= 5:
#     print(i)
#     i = i + 1

#
# i = 6
# while i < 10:
#     print(i)
#
#     if i > 5:
#         break
#
#     i += 1

# my_dictionary = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
# c = 1
# for i in my_dictionary:
#     c = c + my_dictionary[i]
# print(c)


# # Есть список учеников в нескольких классах,
# # нужно вывести самое частое имя в каждом классе.
#
# school_students = [
#   [  # это – первый класс
#     {'first_name': 'Вася'},
#     {'first_name': 'Вася'},
#   ],
#   [  # это – второй класс
#     {'first_name': 'Маша'},
#     {'first_name': 'Маша'},
#     {'first_name': 'Оля'},
#   ]
# ]


# Напишите функцию change(lst), которая принимает
# список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.


def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
print(change([1, 2, 3]))


#
# def list_sort(lst):
#     lst.sort(key=lambda x: abs(x), reverse=True)
#     return lst
# print(list_sort([10, 2, 5, 6, -11]))


# my_dict = {}
# my_dict["lol"] = 1
# print(my_dict)
# my_dict.update({"kek": 2})
# print(my_dict)
# my_dict.update({("chebyrec"): ([3])})
# print(my_dict)
# print(my_dict.get("lol"))
# my_dict.pop("lol")
# print(my_dict)
# print(my_dict.keys())

# a = set('12345')
# print(a)
# b = frozenset('123')
# print(b)
# c = a | b
# print(c)
# d = a & b
# print(d)


# необходимо из существующего списка создать словарь
# a = ["first", 1, 2, 3, "second", 10, 20, "third", 15, 56, 70, "fourth", -50]
# словарь имеет один ключ и несколько значений

a = [1, 2, "second", 10, 20, "first", 1, 2, 3, "third", 15, 56, 70, "fourth", -50]

b = {}
c = ''

for i in a:
    if isinstance(i, str):
        c = i
        b.update({i: []})
    else:
        if c != "":
            b[c].append(i)
print(b)


#
# a = ["first", 1, 2, 3, ['hg'], "second", 10, 20, "third", 15, 56, 70, "fourth", -50]
#
# b = {}
# c = ''
#
# for i in a:
#     if isinstance(i, str):
#         b.update({i: []})
#         c =
#     else:


# a = [1, 2, "second", 10, 20, "first", 1, 2, 3, "third", 15, 56, 70, "fourth", -50]
#
# b = {}
# c = 0
# for x in range(len(a)):
#     if type(a[x]) is str:
#         b[a[x]] = []
#         c = x
#     else:
#         if x > c and c != 0:
#             b[a[c]].append(a[x])
#
# print(b)


# is_male = {'2a': ['Маша', 'Оля'], '3c': ['Олег', 'Миша']}
# k = {}
# for i in is_male.items():
#     k.update({i: {'boys': 0, 'girls': 0}})
# print(k)
# print(is_male.items())
# sortirovannye_klassy = {'2a': ['Маша', 'Оля'], '3c': ['Олег', 'Миша']}
# schotchic = {}
# for nazvanija_klassov, imena_studentov in sortirovannye_klassy.items():
#     schotchic.update({nazvanija_klassov: {'boys': 0, 'girls': 0}})
# print(schotchic)


# my_dict = {'a': 1, 'b': 2, 'c': 3}
# k = {}
# for i in my_dict.items():
#     k.update({i: 0})
#     print(k)


#
# boys = {"Кузя": 30,
#         "Саня": 27,
#         "Витя": 30}


# Нaпишите прогрaмму, котoрая принимает на вход спиcок чисел
# в одной cтроке и выводит на экран в oдну строкy значения,
# котoрые повторяются в нём бoлее одного раза.
# Выводимые числа не дoлжны повторяться, пoрядок
# их вывода может быть произвольным.
# Нaпример: 4 8 0 3 4 2 0 3

# Выучить все методы для диктов, списков, множеств и пр
# почитать про словари
# игра контрол посмотри


my_list = [3, 5, 2, 1, 4, 4, 4, 4, 1, 10, 20, 20, 8, 8, 8]
b = [x for x in set(my_list) if my_list.count(x) > 1]
print(b)
b = []
for x in my_list:
    if my_list.count(x) > 1:
        b.append(x)
print(set(b))
#
#
#
# my_list1 = [3, 5, 2, 1, 4, 4, 4, 4, 1, 10, 20, 20, 8, 8, 8]
# numbers = [x for x in my_list1 if my_list1.count(x) > 1]
# set(numbers)
# print(set(numbers))


# есть словарик, в нем ключи - класс и скоринг, в ключе класс содержится
# номер и буква класса, в скоринге список отметок учеников. тебе нужно
# вычислить средний балл по школе и потом вывести на экран среднюю оценку
# по каждому классу в школе

school_journal = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
                  {'school_class': '6b', 'scores': [5,5,1,5,3]},
                  {'school_class': '3c', 'scores': [1,5,2,2,4]},
                  {'school_class': '7d', 'scores': [5,5,3,3,5]},
                  {'school_class': '8e', 'scores': [1,2,5,5,1]},
                  {'school_class': '9e', 'blabla': [1,2,5,5,1]}]
all_scores = []
for i in school_journal:
    if i.get("scores") is not None:
        #print(i.get("scores"))
        all_scores.extend(i.get("scores"))
#print(all_scores)
count = len(all_scores)
print(count)
summa = 0
for x in all_scores:
    summa += x
print(summa)
print(summa / count)

my_chool_class = []
my_scores = []
my_average_scores = []
for i in school_journal:
    i.get('school_class')
    if i in school_journal:
        i.get('scores')
        my_chool_class = i.get('school_class')
        my_scores = i.get('scores')
        count = len(my_scores)
        summa = 0
        for x in my_scores:
            summa += x
        my_average_scores = (summa / count)
        print(f'school_class: {my_chool_class}, scores: {my_average_scores}')



all_values = []
for i in school_journal:
    if i.get('scores') is not None:
        all_values.extend(i.get("scores"))
average_score = (sum(all_values)/len(all_values))
print(f'средний балл по школе: {average_score}')


# Для каждого школьного класса нужно вывести количество девочек и мальчиков в нём и среднюю оценку по классу.
# Вывести средний балл по школе
# Высчитать индекс массы тела через функцию
# Индекс массы тела:
# ИМТ < 18.5:	Ниже нормального веса
# ИМТ >= 18.5 И < 25:	Нормальный вес
# ИМТ >= 25 И < 30:	Избыточный вес
# ИМТ >= 30 И < 35:	Ожирение I степени
# ИМТ >= 35 И < 40:	Ожирение II степени
# ИМТ >= 40:	Ожирение III степени


school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}],
     'scores': [4, 5], 'physical': [{'Маша': [167, 70]}, {'Оля': [170, 50]}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Маша'}],
     'scores': [3, 4, 4], 'physical': [{'Олег': [180, 75]}, {'Миша': [175, 80]}, {'Маша': [170, 40]}]}
]

is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True
}

school_sorted = {}
counters = {}
class_scores = {}
student_conditions = {}

for my_class in school:
    school_sorted.update({my_class.get('class'): []})
    #    print(school_sorted)   создаёт ключи с названием школьного класса
    for student in my_class.get('students'):
        school_sorted[my_class.get('class')].append(student.get('first_name'))
        # print(school_sorted)
        # school_sorted = {'2a': ['Маша', 'Оля'], '3c': ['Олег', 'Миша', 'Маша']}
        for scores in my_class:
            class_scores.update({my_class.get('class'): my_class.get(
                'scores')})
            # class_scores = {'2a': [4, 5], '3c': [3, 4, 4]}
            for student_physical in my_class.get('physical'):
                for i in student_physical:
                    student_conditions.update({i: student_physical.get(i)})
                    # print(student_conditions)

# student_conditions = {'Олег': [180, 75], 'Миша': [175, 80], 'Маша': [170, 40]}

for class_name, student_names in school_sorted.items():
    counters.update({class_name: {'boys': 0, 'girls': 0}})
    for student_name in student_names:
        if is_male.get(student_name):
            counters.get(class_name)['boys'] += 1
        else:
            counters.get(class_name)['girls'] += 1

average_score = []
imt = {}
h = []
for class_name, students in counters.items():
    boys = students['boys']
    girls = students['girls']
    for scores in class_scores:
        average_score = sum(class_scores.get(class_name)) / len(class_scores.get(class_name))
        for i, j in student_conditions.items():
            imt.update({i: []})
            h.append(student_conditions.get(i))
            if j in h:
                imt[i].append(j[0] / j[1])

    print(f'В классе {class_name} обучается: {girls} девочек и {boys} мальчиков, их средняя оценка: {average_score}, '
          f'\n индекс массы тела {imt} ')

print(imt)


# student_conditions = {'Олег': [180, 75], 'Миша': [175, 80], 'Маша': [170, 40]}
# l = {}
# h = []
# for i, j in student_conditions.items():
#     l.update({i: []})
#     h.append(student_conditions.get(i))
#     if j in h:
#         l[i].append(j[0] / j[1])

# print(l)
# h =[[180, 75], [175, 80], [170, 40]]

# print(h)

# f.extend((d[0] / d[1], d[2] / d[3]))
# print(f)


# school = [
#     {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}],
#      'scores': [4, 5], 'physical': [{'Маша': [167, 70]}, {'Оля': [170, 50]}]},
#     {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Маша'}],
#      'scores': [3, 4, 4], 'physical': [{'Олег': [180, 75]}, {'Миша': [175, 80]}, {'Маша': [170, 40]}]}
#     ]
#
# class_sorted = {}
# class_scores = {}
# student_conditions = []
#
# for my_class in school:
#     class_sorted.update({my_class.get('class'): []})
#     for student in my_class.get('students'):
#         class_sorted[my_class.get('class')].append(student.get('first_name'))
#         # print(class_sorted) {'2a': ['Маша', 'Оля'], '3c': ['Олег', 'Миша', 'Маша']}
#         for scores in my_class:
#             class_scores.update({my_class.get('class'): my_class.get('scores')})
#             #{'2a': [4, 5], '3c': [3, 4, 4]}
#     for physical in my_class.get('physical'):
#         for student, conditions in physical.items():
#             student_conditions.append({student: conditions[0] / conditions[1]}) #убрать лишние знаки после запятой
# print(student_conditions)


# for item in physical:
#                     student_conditions.append({item: physical.get(item)})
# student_conditions = {'Маша': [167, 70], 'Оля': [170, 50], 'Олег': [180, 75], 'Миша': [175, 80], 'Юля': [170, 40]}

# print(student_conditions)


# my_dict = {'physical': [{'Олег': [180, 75]}, {'Миша': [175, 80]}, {'Маша': [170, 40]}]}
# student_conditions = {}
#
# for student_physical in my_dict.get('physical'):
#     for i in student_physical:
#         # student_physical = {'Олег': [180, 75]} {'Миша': [175, 80]} {'Маша': [170, 40]}
#         student_conditions.update({i: student_physical.get(i)})
#         print(student_conditions)


# my_dict_items = ([('physical', [{'Олег': [180, 75]}, {'Миша': [175, 80]}, {'Маша': [170, 40]}])])


# counters.items = ([('2a', {'boys': 0, 'girls': 2}), ('3c', {'boys': 2, 'girls': 0})])
# counters = {'2a': {'boys': 0, 'girls': 2}, '3c': {'boys': 2, 'girls': 0}}
# class_scores = {'2a': [4, 5, 4, 5, 3], '3c': [3, 4, 4, 5, 2]}
#
# print(g)
# print(counters.items())
# print(class_scores)
# print(school_sorted.items())


# school_journal = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
#                   {'school_class': '6b', 'scores': [5, 5, 1, 5, 3]},
#                   {'school_class': '3c', 'scores': [1, 5, 2, 2, 4]},
#                   {'school_class': '7d', 'scores': [5, 5, 3, 3, 5]},
#                   {'school_class': '8e', 'scores': [1, 2, 5, 5, 1]},
#                   {'school_class': '9e', 'blabla': [1, 2, 5, 5, 1]}]
# all_values = []
# for i in school_journal:
#     if i.get('scores') is not None:
#         all_values.extend(i.get('scores'))
# print(all_values)
# print(f'Средний балл по школе: {(sum(all_values) / len(all_values))}')
#
# my_chool_class = []
# my_scores = []
# for i in school_journal:
#     my_chool_class = i.get('school_class')
#     if i in school_journal:
#         if i.get('scores') is not None:
#             my_scores = i.get('scores')
#             print(f'Средний балл по классу {my_chool_class}: {sum(my_scores) / len(my_scores)}')


# lst = ['Мавпродош', 'Лорнектиф', 'Древерол', 'Фиригарпиг', 'Клодобродыч']
#
# name = input()
#
# while not name in lst:
#     print("Нюхай бэбру")
#     name = input()
# else:
#     print(f'Привет, пиздюк {name}')
#
# input()
#


# answers = {
#     "Привет!": "Привет!",
#     "Пока!": "Пока!"
# }
#
# def get_answer(answers, key):
#     c = answers.get(key)
#     return c
#
#
#
# while True:
#     a = input("Ky: ")
#     s = get_answer(answers, a)
#     if s == "Пока!":
#         print(s)
#         break
#     if s == "Привет!":
#         print(s)
#         break
#     if s is not None:
#         print(s)


# while True:
#     a = input("Скажи что-нибудь:")
# if a in answers:
