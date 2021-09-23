employee_numbers = [2, 9, 18, 28]
employee_names = ["Дима", "Марина", "Андрей", "Никита"]

zipped_values = zip(employee_names, employee_numbers)
zipped_list = list(zipped_values)

# print(zipped_list)


employee_numbers = [2, 9, 18, 28]
employee_names = ["Дима", "Марина", "Андрей", "Никита"]

ml = [(name, number) for name, number in zip(employee_names, employee_numbers)]
# print(ml)





def collector():
    adress_list = [{'adress': 'Минск', 'name': 'аптека+'}, {'adress': 'Червень', 'name': 'соц аптека'}, {'adress': 'Гомель', 'name': 'аптека ку'}]
    latlon_list = [{"latlon": [62.031799, 129.754762]}, {"latlon": [42.031566, 229.754987]}, {"latlon": [76.03656, 54.876756]}]
    time_list = [{"time": ['8:00', '21:00']}, {"time": ['8:00', '22:00']}, {"time": ['круглосуточно']}]

    result = [{**x, **y, **z} for x, y, z in zip(adress_list, latlon_list, time_list)]
    return result
# print(collector())


result = [
    {'adress': 'Минск', 'name': 'аптека+', 'latlon': [62.031799, 129.754762], 'time': ['8:00', '21:00']},
    {'adress': 'Червень', 'name': 'соц аптека', 'latlon': [42.031566, 229.754987], 'time': ['8:00', '22:00']},
    {'adress': 'Гомель', 'name': 'аптека ку', 'latlon': [76.03656, 54.876756], 'time': ['круглосуточно']}
]
# adress_list, latlon_list, time_list = zip(*result)
# print(adress_list, latlon_list, time_list)


employees_zipped = [{'Дима': 2}, {'Марина': 9}, {'Андрей': 18}, {'Никита': 28}]
# employee_names, employee_numbers = [{**x} for x in zip(*employees_zipped)]
# print(employee_names)
# print(employee_numbers)
a = zip(*employees_zipped)
# print(a)
# result_1, result_2 = [({**r, **t} for r, t in zip(*employees_zipped))]
# print(result_1, result_2)


employees_zipped = [('Дима', 2), ('Марина', 9), ('Андрей', 18), ('Никита', 28)]
employee_names, employee_numbers = zip(*employees_zipped)

print(employee_names)
print(employee_numbers)




date_info = {'year': "2020", 'month': "01", 'day': "01"}
track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(**date_info,**track_info)
# print(filename)




fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']

a_dict = dict(zip(fields, values))
# print(a_dict)





# def parser(result):
#     adress_list, latlon_list, time_list = zip(*result)
#     return adress_list, latlon_list, time_list
#
# result = collector()
# print(parser(result))