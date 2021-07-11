# import random
#
#
# def random_item():
#     control_item = random.randint(0, 100)
#     return control_item
#
#
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
#
#
#
#
# def operation(control_item, user_item):
#     reference_value = control_item - user_item
#     if reference_value >= 50:
#         print('Холодно')
#     # elif control_item - user_item == 0:
#     #     print('Поздравляем! Вы угадали число')
#     elif reference_value <= 49:
#         print('Тепло')
#     return reference_value
#
#
# def area(reference_value, control_item, user_item):
#     result_item_reference = 0 - reference_value  # опорное число
#     result_item_user = 0 - user_item
#     if control_item - user_item == 0:
#         print('Поздравляем! Вы угадали число')
#     elif result_item_user > result_item_reference:
#         print('Холоднее')
#     elif abs(result_item_user) > control_item:  # сравниваем с контрольным числом по модулю
#         print('Холоднее')
#     elif result_item_user < result_item_reference:
#         print('Теплее')
#
#
# def result():
#     control_item = random_item()
#     print(f'Контрольное число: {control_item}')
#     user_item = input_user_item()
#     operation(control_item, user_item)
#     reference_value = operation(control_item, user_item)
#     while True:
#         if control_item == user_item:
#             break
#         else:
#             user_item = input_user_item()
#             area(reference_value, control_item, user_item)


# result()
#
# # с какой попытки угадал число добавить
#
#
#
#
#
#
#
# def prit():
#     print(f'Первый запуск функции: {random_item()}')
#     a = 0
#     while a < 20:
#         print(random_item())
#         a += 1
#
# # prit()


# def operation(control_item, user_item):
#     reference_value = control_item - user_item
#     pervichnoe_chislo = user_item
#     if control_item - user_item == 0:
#         print('Поздравляем! Вы угадали число')
#     elif reference_value >= 50:
#         print('Холодно')
#     elif reference_value <= 49:
#         print('Тепло')
#         return pervichnoe_chislo


# def area_1(control_item, user_item, pervichnoe_chislo):
#     if control_item - user_item == 0:
#         print('Поздравляем! Вы угадали число')
#     elif pervichnoe_chislo < user_item < control_item:
#         print('Теплее')
#     elif pervichnoe_chislo > user_item < control_item:
#         print('Холоднее')
#     elif pervichnoe_chislo < user_item > control_item:
#         print('Холоднее')




# pervichnoe_chislo = operation(60, 50)
# print('Контрольное число: 60')
# print('Первичное число:', pervichnoe_chislo)
# user_item = input_user_item()
# area_1(60, user_item, pervichnoe_chislo)






# def area(reference_value, control_item, user_item):
#     result_item_reference = 0 - reference_value  # опорное число
#     print("разность между нулём и первым загаданным числом (result_item_reference)", result_item_reference)
#     result_item_user = 0 - user_item
#     print("разность между нулём и следующим загаданным числом (result_item_user)", result_item_user)
#     if control_item - user_item == 0:
#         print('Поздравляем! Вы угадали число')
#     elif result_item_user > result_item_reference:
#         print('Если (result_item_user) больше (result_item_reference) ---> \nХолоднее')
#     elif abs(result_item_user) > control_item:  # сравниваем с контрольным числом по модулю
#         print('Если (result_item_user) больше по модулю (result_item_reference) ---> \nХолоднее')
#     elif result_item_user < result_item_reference:
#         print('Если (result_item_user) меньше (result_item_reference) ---> \nТеплее')
#     return result_item_user

# print(area(20, 80, 80))

# print(60 < 65 and 65 < 80)
# print(60 < 65 > 80)
# print(60 < 100 < 80)
# print(65 > 60 < 80)





def operation(control_item, user_item):
    reference_value = control_item - user_item
    if control_item - user_item == 0:
        print('Поздравляем! Вы угадали число')
        return
    elif reference_value >= 50:
        print('Холодно')
    elif reference_value <= 49:
        print('Тепло')
    key = 0
    while user_item != control_item:
        key += 1
        user_item_dict = {}
        user_item_dict.update({key: input_user_item()})
        print(user_item_dict)
        pervichnoe_chislo = user_item_dict[key]
        print(pervichnoe_chislo)
        # if pervichnoe_chislo == user_item:
        #     input_user_item()
        # elif control_item - user_item == 0:
        #     print('Поздравляем! Вы угадали число')
        # elif pervichnoe_chislo < user_item < control_item:
        #     print('Теплее')
        # elif pervichnoe_chislo > user_item < control_item:
        #     print('Холоднее')
        # elif pervichnoe_chislo < user_item > control_item:
        #     print('Холоднее')


operation(20, 12)


        # b = {}
        # page_link = 0
        # for item in parsed:
        #     page_link += 1
        #     b.update({(page_link): item})
        # z = b.values()
        # print(z)



        # if control_item - user_item == 0:
        #     print('Поздравляем! Вы угадали число')
        # elif pervichnoe_chislo < user_item < control_item:
        #     print('Теплее')
        # elif pervichnoe_chislo > user_item < control_item:
        #     print('Холоднее')
        # elif pervichnoe_chislo < user_item > control_item:
        #     print('Холоднее')

















# buf = pervichnoe_chislo
# pervichnoe_chislo = user_item
# user_item = buf

# pervichnoe_chislo = 5
# user_item = 6
#
# buf = pervichnoe_chislo
# pervichnoe_chislo = user_item
# user_item = buf
#
# print(pervichnoe_chislo)
# print(user_item)

