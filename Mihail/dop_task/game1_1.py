import sys
import random

if __name__ == "__main__":

    control_item = random.randint(0, 100)
    print(control_item)

    tries = 0
    previous_choice = 0
    difference = 0
    limit = 100

    while True:
        try:
            tries += 1
            user_item = int(input('Введите целое число от 0 до 100: '))

            if control_item - user_item == 0:
                if tries == 1:
                    print('Поздравляем! Вы угадали число с первого раза')
                else:
                    print(f'Поздравляем! Вы угадали число с {tries} попытки')
                break

            if user_item == previous_choice and tries != 1:
                print('Введите число, отличное от предыдущего')
            else:
                if tries > 1:
                    if abs(control_item - user_item) > abs(difference):
                        print('Холоднее!')
                    else:
                        print('Теплее!')

            if tries == limit:
                print(f'Сожалею! Вы не смогли разгадать число с {tries} попыток')
                break

            difference = control_item - user_item
            previous_choice = user_item

        except ValueError as e:
            print('Необходимо вводить числа от 0 до 100 включительно')
        except KeyboardInterrupt as e:
            print('\nПока!')
            sys.exit(0)