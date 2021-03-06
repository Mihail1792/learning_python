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


reward = int(input(f'Ведите количество статуэток: '))
actors_dict = {}
count = 0
count_reward = 0

while count != reward:
    actors = input(f'Введите актёров, которые номинируются на статуэтку: ')
    actors_dict.setdefault(actors, 0)
    actors_dict[actors] += 1
    count += 1
print(f'{max(actors_dict, key=actors_dict.get)}, {max(actors_dict.values())}')
print(f'{min(actors_dict, key=actors_dict.get)}, {min(actors_dict.values())}')