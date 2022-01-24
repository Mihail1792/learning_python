# import random
#
#
# def random_item():
#     control_item = random.randint(0, 100)
#     if control_item > 50:
#         print(control_item, "Hello Kyzbass")
#     else:
#         print(control_item, "Hello Keratas")
#     return control_item
#
#
# def sum_item(control_item):
#     a = 50 + control_item
#     return a
#
# # print(sum_item(random_item()))
# # control_item = random_item()
# # print(sum_item(control_item))
#
# def my_list_append(control_item, a):
#     my_list = [1, 3, 5]
#     b = control_item + a
#     my_list.append(b)
#     return my_list
#
# control_item = random_item()
# a = sum_item(control_item)
# print(my_list_append(control_item, a))
#
#
# def multiply(a, b):
#     a * b
#     return a * b
#
#
# multiply(1, 2)
#
# def get_key(my_dict):
#     my_list = []
#     for key in my_dict:
#         my_list.append(my_dict.get(key))
#         # print(my_list)
#     return my_list
#
# my_dict = {'a': 1, 'b': 2}
# a = get_key(my_dict)
# a.reverse()
# print(a)

# если н больше 20, ТО РЕТЁРН НОЛЬ, если меньше или равно 20, то
# пройтись по диапазону от 1 до числа н и все четные числа возвести в степень к и сложить всё, что получилось

# def func(n, k):
#     if n > 20:
#         return 0
#     else:
#         a = 0
#         for i in range(1, n + 1):
#             if i % 2 == 0:
#                 print(i)
#                 a += i ** k
#         return a
#
# print(func(4, 2))

# Пользователь делает вклад в размере RUB рублей сроком на years лет под 10% годовых
# (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада,
# и на них в следующем году тоже будут проценты).
#
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму,
# которая будет на счету пользователя.


# def bank(RUB, years):
#     i = 0
#     while i != years:
#         i += 1
#         RUB += RUB * 0.10
#     return RUB
#
#
#
#
# # print(bank(10000, 3))
#
#
# def bank_1(a, years):
#     for i in range(1, years + 1):
#         a += a * 0.1
#     return a
#
# print(bank(10000, 3))

# lst = []
# for i in range(1, 10):
#     lst.append(i)
# print(lst)


# my_list = [9, 8, 7, 3, 1, 0, -2, -7, -1000]
# my_list2 = ["Kyzbass", "Liza", "1", "lol", 1, -100, 9, 7]
# ff = []
# for i in my_list2:
#     if i not in my_list:
#         ff.append(i)
# print(ff)
#
# my_list_4 = [x for x in my_list2]
# print(my_list_4)


# my_list = [9, 8, 7, 3, 1, 0, -2, -7, -1000]
# my_list2 = ["Kyzbass", "Liza", "1", "lol", 1, -100, 9, 7]
# my_list2 = [x for x in my_list2 if not x in my_list]
# print(my_list2)

# Премия Оскар
# Представьте, что мы с вами сами можем решать кому и сколько статуэток Оскара уйдет
# (Лео бы тогда давно купался в этих статуэтках)
# Ваша задача написать программу, которая находит информацию,
# кто из актеров получил наибольшее и наименьшее количество статуэток
# Входные данные
# Программа принимать на вход в первой строке натуральное число n - количество вручаемых сегодня наград.
# И затем в n следующих строках вводятся имена актеров - победителей.
# Выходные данные
# Нужно вывести в  отдельных строках имена актеров набравших наибольшее и наименьшее количество статуэток
# и через запятую их количество. Гарантируется, что всегда будет только один человек, набравших наибольшее
# и наименьшее количество статуэток.


# reward = int(input(f'Ведите количество статуэток: '))
# actors_dict = {}
# count = 0
# count_reward = 0
#
# while count != reward:
#     actors = input(f'Введите актёров, которые номинируются на статуэтку: ')
#     actors_dict.setdefault(actors, 0)
#     actors_dict[actors] += 1
#     count += 1
# print(f'{max(actors_dict, key=actors_dict.get)}, {max(actors_dict.values())}')
# print(f'{min(actors_dict, key=actors_dict.get)}, {min(actors_dict.values())}')
#
#
# actors_dict = {'ggg': 3, 'hh': 2, 'j': 1}
# max_reward = max(actors_dict.values())
# print(f'{max(actors_dict, key=actors_dict.get)}, {max(actors_dict.values())}')
# print(max(actors_dict, key=actors_dict.get))


# 6
# Леонардо Ди Каприо
# Джонни Депп
# Леонардо Ди Каприо
# Леонардо Ди Каприо
# Джонни Депп
# Мэтт Деймон
#
# lst_actors = {}
# count_reward = int(input())
# for i in range(count_reward):
#     actors = input()
#     if actors in lst_actors:
#         lst_actors[actors] += 1
#         lst_actors.setdefault(actors, i)
#     else:
#         lst_actors.setdefault(actors, i)
#         lst_actors[actors] = 1
# for i in sorted(lst_actors.items(), key=lambda para: -para[1]):
#     print(*i)


# a = 5
# b = 10
# print(a, b)
# (a, b) = (b, a)
# print(a, b)


# my_list = ["first", 1, 2, 3, "second", 10, 20, "third", 15, 56, 70, "fourth", -50]
# my_dict = {}
# for el in my_list:
    # if type(el) is str:
    #     print('dsfdsf')
    # my_dict.setdefault(el if type(el) is str else my_dict.get(el))
    # print(type(el))
    # if isinstance(el, str):
    #     f = my_dict.setdefault(el, [])
    # elif isinstance(el, int):
# print(my_dict)
    #     # print(f)
    #     # print(my_dict)
    # elif
    #     print(el)
    #     a = my_dict.get(el)
    #     print(a)
#     if a is not None:
#         a.append(el)
# print(my_dict)








#     else:
#         f.append(el)
#
# print(my_dict)

    # else:
    #     print(el)
    #     a = my_dict.get(el)
    #     print(a)

        # print(type(my_dict.get(el)))
        # print(el)
        # if isinstance(el, int):
        #     print(my_dict.get(el))
            # my_dict.get(el).append(el)

# print(my_dict)
# for i in my_dict:
#     print(my_dict.get(i))






# my_list = ["first", 1, 2, 3, "second", 10, 20, "third", 15, 56, 70, "fourth", -50]
# my_dict = {}
# list_1 = []
# for el in my_list:
#     if isinstance(el, str):
#         f = my_dict.setdefault((el), [])
#     elif isinstance(el, int):
#         list_1.append(el)
# print(my_dict)
# print(list_1)



my_list = ["first", 1, 2, 3, "second", 10, 20, "third", 15, 56, 70, "fourth", -50]
my_dict = {}
temporary_list = []
for el in my_list:
    if isinstance(el, str):
        temporary_list = my_dict.setdefault(el, [])
    else:
        temporary_list.append(el)

print(my_dict)