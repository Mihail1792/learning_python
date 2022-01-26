# import random
#
#
# def random_item():  # генерит случайное число
#     control_item = random.randint(0, 100)
#     return control_item
#
#
# def input_user_item():  # Пользовательский ввод
#     while True:
#         try:  # Проверка входящих данных
#             user_item = int(input('Введите целое число от 0 до 100: '))
#             if user_item > 100:
#                 print('Нужно вводить числа от 0 до 100')
#             elif user_item < 0:
#                 print('Нужно вводить числа от 0 до 100')
#             else:
#                 break
#         except:
#             print("ValueError: Нужно вводить целые числа")
#
#     return user_item  # Возвращает число, которое ввёл пользователь
#
#
# def operation(control_item, user_item):
#     reference_value = control_item - user_item  # Отнимаем рандомное от загаданного, чтобы потом сравенить
#     if control_item - user_item == 0:  # Если ранломное и загаданное совпало, то завершаем функцию
#         print('Поздравляем! Вы угадали число с первого раза')
#         return
#     elif reference_value >= 50:
#         print('Холодно')
#     elif reference_value <= 49:
#         print('Тепло')
#     key = 1
#     user_item_dict = {}  # Создаём пустой словарь, в который будем складывать по порядку числа вводимые пользователь
#     user_item_dict.update({key: user_item})  # Сразу вносим первое значение, которое ввёл пользователь (1: user_item)
#     while user_item_dict[key] != control_item:  # Запускаем цикл с условием, пока юзер число не равно рандомному, он будет работать
#         while user_item_dict[key] != control_item:
#             key += 1  # Счетчик ключей в словаре добавляет по одному (1, 2, 3, 4 и тд)
#             user_item_dict.update({key: input_user_item()})  # Дополняем словарь ключами key и числами ,которые введёт юзер
#             key_2 = key - 1  # Номер предыдущего ключа пользователя
#             primary_number = user_item_dict[key_2]  # Значение предыдущего ключа пользователя
#             if control_item - user_item_dict[key] == 0:  # Если рандомное число совпало с числом юзера, то
#                 print(f'Поздравляем! Вы угадали число с {key} попытки')  # Выводим на печать
#                 break  # Останавливаем цикл, тк условие совпало
#             if key == 2:
#                 if 0 - (primary_number - user_item_dict[key]) < 0:  # При первом вводе юзером дважды цифр подряд, которые больше рандомного, срабатывал ("Теплее 1")
#                     print('Теплее00')  # Эта строка правит проблему ('Холоднее0')
#             elif key == 2:
#                 if 0 - (primary_number - user_item_dict[key]) > 0:
#                     print('Холоднее0')
#             elif 0 - (control_item - primary_number) > 0 - (control_item - user_item_dict[key]):  # Если выражение True,
#                 print('Холоднее1')  # то холоднее ('Холоднее1')
#             elif 0 - (control_item - primary_number) < 0 - (control_item - user_item_dict[key]):  # Если выражение True,
#                 print('Теплее1')  # то теплее ("Теплее 1")
#             if 0 - (control_item - user_item_dict[key]) > 0:  # Если выражение True, то переходит к телу цикла while-->
#                 while user_item_dict[key] != control_item:  # Проверка условий в этом цикле осуществляется по тому же принципу,
#                     key += 1  # что в предыдущем
#                     user_item_dict.update({key: input_user_item()})
#                     key_2 = key - 1
#                     primary_number = user_item_dict[key_2]
#                     if control_item - user_item_dict[key] == 0:
#                         print(f'Поздравляем! Вы угадали число с {key} попытки')
#                         break
#                     elif 0 - (control_item - primary_number) < 0 - (control_item - user_item_dict[key]):
#                         print('Холоднее2')
#                     elif 0 - (control_item - primary_number) > 0 - (control_item - user_item_dict[key]):
#                         print('Теплее2')
#                         if 0 - (control_item - user_item_dict[key]) < 0:
#                             break
#
#
# def result():  # Функция, которая запускает всё вместе
#     control_item = random_item()
#     print('Случайное число, которое загадал ПК:', control_item)
#     user_item = input_user_item()
#     operation(control_item, user_item)
#
#
# result()

# Попробуй вводить числа меньше "0", больше "100", буквы, буквы с цифрами.
# Ну и само собой абсолютно любые числа от "0" до "100" в любой последовательности.
# Прога не должна выдавать ничего некорректного
# Попробуй при запуске программы дважды ввести число больше рандомного
# Попробуй при запуске программы дважды ввести число меньше рандомного
# Попробуй при запуске программы число меньше рандомного, больше введенного до рандомного
# Попробуй при запуске программы число больше рандомного, меньше введенного до рандомного










import random


def random_item():
    control_item = random.randint(0, 100)
    return control_item


def input_user_item():
    while True:
        try:
            user_item = int(input('Введите целое число от 0 до 100: '))
            if user_item > 100:
                print('Нужно вводить числа от 0 до 100')
            elif user_item < 0:
                print('Нужно вводить числа от 0 до 100')
            else:
                break
        except:
            print("ValueError: Нужно вводить целые числа")

    return user_item


def operation(control_item, user_item):
    reference_value = control_item - user_item
    if control_item - user_item == 0:
        print('Поздравляем! Вы угадали число с первого раза')
        return
    elif reference_value >= 50:
        print('Холодно')
    elif reference_value <= 49:
        print('Тепло')
    key = 1
    user_item_dict = {}
    user_item_dict.update({key: user_item})
    while user_item_dict[key] != control_item:
        while user_item_dict[key] != control_item:
            key += 1
            user_item_dict.update({key: input_user_item()})
            key_2 = key - 1
            primary_number = user_item_dict[key_2]
            if control_item - user_item_dict[key] == 0:
                print(f'Поздравляем! Вы угадали число с {key} попытки')
                break
            if key == 2:
                if 0 - (primary_number - user_item_dict[key]) < 0:
                    print('Теплее00')
            elif key == 2:
                if 0 - (primary_number - user_item_dict[key]) > 0: # Попробуй создать условие, в котором сравнивается с сдумя числами, а не с одним предыдущим, типа больше первого, но меньше второго
                    print('Холоднее0')
            elif 0 - (control_item - primary_number) > 0 - (control_item - user_item_dict[key]):
                print('Холоднее1')
            elif 0 - (control_item - primary_number) < 0 - (control_item - user_item_dict[key]):
                print('Теплее1')
            elif 0 - (control_item - primary_number) < 0 - (control_item - user_item_dict[key]):
                print('Холоднее2')
            elif 0 - (control_item - primary_number) > 0 - (control_item - user_item_dict[key]):
                print('Теплее2')
                if 0 - (control_item - user_item_dict[key]) < 0:
                    break


def result():
    control_item = random_item()
    print('Случайное число, которое загадал ПК:', control_item)
    user_item = input_user_item()
    operation(control_item, user_item)


result()