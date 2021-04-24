from heapq import nlargest

# Задача 1
# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.
list_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
s = slice(0, 4)
print(list_numbers[s])

# Задача 2
# Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
list_numbers_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = list(set(list_numbers_1) & set(list_numbers_2))
print(result)

# Задача дополнительно
# Отсортировал список по значению в порядке возрастания и убывания.
# Получилось доп задание на списки. Невнимательно прочитал условие=)
list_numbers_1_1 = [7, 65, 34, 4, 65, 98, 5, 11, 1, 2, 16]
list_numbers_1_1.sort()
print(list_numbers_1_1)
list_numbers_1_1.reverse()
print(list_numbers_1_1)

# Задача 3
# Отсортируйте словарь по значению в порядке возрастания и убывания.
my_dict = {'a': 5, 'b': 1, 'c': 8, 'd': 2, 'e': 30}
e = {}
my_dict_1 = sorted(my_dict.items(), key=lambda key_value: key_value[1], reverse=True)
e = my_dict_1
print(e)
my_dict_2 = sorted(my_dict.items(), key=lambda key_value: key_value[1])
print(my_dict_2)

# Задача 4
# Найдите три ключа с самыми высокими значениями
# в словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
my_dict = {j: i for i, j in my_dict.items()}
x = dict(nlargest(3, my_dict.items()))
x = {z: y for y, z in x.items()}
print(x)
# Задача 5
# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
def sec(s):
    days = s // (24 * 3600)
    hours = s % (24 * 3600) // 3600
    minutes = s % (24 * 3600) // 3600 // 60
    seconds = s % (24 * 3600) % 3600 % 60
    return(f'{days}:{hours}:{minutes}:{seconds}')
print(sec(938358))

