import typing
from collections import Counter

# Задача 1
# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.

def list_check(a: list) -> typing.Optional[None]:
    for i in a:
        if i < 5:
            print(i)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_check(a)


# Задача 2
# Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.


def list_check2(a: list, b: list) -> typing.Optional[list]:
    result = []
    for i in a:
        for j in b:
            if i == j:
                result.append(i)
    return result


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(list_check2(a, b))


# Задача 3
# Отсортируйте словарь по значению в порядке возрастания и убывания.


def sort_dict(d):
    sorted_values = sorted(d.values())  # Sort the values
    sorted_dict = {}

    for i in sorted_values:
        for k in d.keys():
            if d[k] == i:
                sorted_dict[k] = d[k]
                break
    return sorted_dict


dict1 = {99: 1, 92: 9, 193: 4}
print(sort_dict(dict1))


# Задача 4
# Найдите три ключа с самыми высокими значениями
# в словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.


def max_key(d: dict):
    maxes = Counter(d).most_common(3)
    return [x[0] for x in maxes]


# print(max_key({'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}))


# Задача 5
# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.


def time_convert(t: int):
    d: int = t // (24*3600)
    h: int = t % (24*3600) // 3600
    m: int = t % (24*3600) % 3600 // 60
    s: int = t % (24*3600) % 3600 % 60
    time_list = [d, h, m, s]
    return time_list


print(time_convert(999856))
