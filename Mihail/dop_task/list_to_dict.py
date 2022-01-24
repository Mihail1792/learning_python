# дан список my_list = ["first", 1, 2, 3, "second", 10, 20, "third", 15, 56, 70, "fourth", -50]
# нужно создать словарь,
# в котором ключом будет строка а значением будет список из последующих чисел

my_list = ["first", 1, 2, 3, "second", 10, 20, "third", 15, 56, 70, "fourth", -50]
my_dict, temporary_list = {}, []
for el in my_list:
    if isinstance(el, str):
        temporary_list = my_dict.setdefault(el, [])
    else:
        temporary_list.append(el)
print(my_dict)


a = ["first", 1, 2, 3, "second", 10, 20, "third", 15, 56, 70, "fourth", -50]
my_dict = {}
temp = 0
for el in a:
    if type(el) == str:
        my_dict[el] = []
        temp = el
    else:
        my_dict[temp].append(el)

