# Для каждого класса студентов вывести количество мальчиков и количество девочек
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '1d', 'students': [{'first_name': 'Вася'}, {'first_name': 'Петя'},
                                 {'first_name': 'Лена'}, {'first_name': 'Саша'}]}
]

is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
    'Вася': True,
    'Петя': True,
    'Лена': False,
    'Саша': True

}

school_sorted = {}
counters = {}

for my_class in school:
    school_sorted.update({my_class.get('class'): []})
    for student in my_class.get('students'):
        school_sorted[my_class.get('class')].append(student.get('first_name'))
for class_name, student_names in school_sorted.items():
    counters.update({class_name: {'boys': 0, 'girls': 0}})
    for student_name in student_names:
        if is_male.get(student_name):
            counters.get(class_name)['boys'] += 1
        else:
            counters.get(class_name)['girls'] += 1
for class_name, students in counters.items():
    a = students['girls']
    b = students['boys']
    print(f'В классе {class_name} {a} девочек и {b} мальчиков')


# На вход функции more_than_five(lst) получает список из
# целых чисел.
# Результатом работы функции должен стать новый список,
# в котором содержатся только те числа, которые повторяются в
# нём более одного раза. Выводимые числа не дoлжны повторяться

def more_than_five(my_lst):
    m = []
    for e in my_lst:
        if my_lst.count(e) > 1:
            m.append(e)
    return set(m)


print(more_than_five([3, 3, 3, 5, 10, 1, 2, 2, 2, 2]))

# есть словарик, в нем ключи - класс и скоринг, в ключе класс содержится
# номер и буква класса, в скоринге список отметок учеников. тебе нужно
# вычислить средний балл по школе и потом вывести на экран среднюю оценку
# по каждому классу в школе
school_journal = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
                  {'school_class': '6b', 'scores': [5, 5, 1, 5, 3]},
                  {'school_class': '3c', 'scores': [1, 5, 2, 2, 4]},
                  {'school_class': '7d', 'scores': [5, 5, 3, 3, 5]},
                  {'school_class': '8e', 'scores': [1, 2, 5, 5, 1]},
                  {'school_class': '9e', 'blabla': [1, 2, 5, 5, 1]}]
all_values = []
for i in school_journal:
    if i.get('scores') is not None:
        all_values.extend(i.get('scores'))
print(f'Средний балл по школе: {(sum(all_values) / len(all_values))}')

my_chool_class = []
my_scores = []
for i in school_journal:
    my_chool_class = i.get('school_class')
    if i in school_journal:
        if i.get('scores') is not None:
            my_scores = i.get('scores')
            print(f'Средний балл по классу {my_chool_class}: {sum(my_scores) / len(my_scores)}')

# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
]

a = []
for i in students:
    a.append(i.get('first_name'))

most_common = None
qty_most_common = 0
for item in a:
    qty = a.count(item)
    if qty > qty_most_common:
        qty_most_common = qty
        most_common = item
print(f'Самое частое имя: {most_common}')

# Дан список lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20].
# Необходимо вывести элементы, которые
# одновременно 1) меньше 30 и 2) делятся на 3 без остатка.
#     Все остальные элементы списка необходимо просуммировать
# и вывести конечный результат.

lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

a, b = [], []
for i in lst:
    if i < 30:
        if i % 3 == 0:
            a.append(i)
    else:
        b.append(i)
print(a)
print(sum(b))

# На вход функция more_than_five(lst) получает список из целых чисел.
# Результатом работы функции должен стать новый список, в котором
# содержатся только те числа, которые больше 5 по модулю.
a = []
lst = [-5, 10, -3, 20, 40, -20]


def more_than_five(lst_1):
    for z in lst_1:
        if abs(z) > abs(5):
            a.append(z)
    return a


print(more_than_five([-11, 4, -2, 90, 400, 0, -5, -400, 6]))

# Очистить  строку от заглавных литер.
letters = 'ЫпВЫиЯСтоДШНККАнЩЙФ!'
new_string = ''

for i in letters:
    if i.isupper():
        continue
    new_string += i
letters = new_string

print(letters)
