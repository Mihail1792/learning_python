# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.


# number_list = [90, 1, 1, 84, 2, 3, 5, 8, 13, 21, 34, 55, 89, 2, 4, 250]
# for element in number_list:
#     if element < 5:
#         print(element)


# Имея список имен, нужно вывести список, содержащий только те имена, в которых больше 5 букв
# names = ["David", "John" , "Annabelle", " Johnathan", "Veronica"]


# Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
# print(c)


# def bmi_calculator():
#     user_name = input(f'Введите Ваше имя: ')
#     height = input(f'Введите Ваш рост в метрах: ')
#     weight = input(f'Введите Ваш вес в килограммах: ')
#     bmi = float(weight) / float(height) ** 2
#     bmi = int(bmi * 100) / 100
#     if bmi > 25:
#         print(f'{user_name}, с индексом массы тела: {bmi} жиробас')
#
#
# bmi_calculator()


# def exam_questions():
#     question_dict = {
#         1: 'На какой сигнал светофора движение запрещено? зелёный, желтый, красный',
#         2: 'На какой сигнал светофора движение разрешено? зелёный, желтый, красный'
#     }
#     answer_dict = {
#         1: 'красный',
#         2: 'зелёный'
#     }
#     for question in question_dict:
#         print(f'{question}: {question_dict.get(question)}')
#         user_answer = input(f'Введите Ваш ответ: ')
#         for answer in answer_dict:
#             if user_answer == answer_dict.get(answer):
#                 print(f'Ответ верный')
#                 break
#             else:
#                 print(f'Ответ не верный')
#                 break
#
#
# exam_questions()


a = 2
b = 3
print(a, b)
a, b = b, a
print(a, b)
