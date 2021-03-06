# ### **Ханойская башня**
#
# ![Визуализация алгоритма](https://ioecapsule.com/wp-content/uploads/2019/08/tower_of_hanoi_3_disks.gif)
#
# [Ханойская башня](https://www.britannica.com/topic/Tower-of-Hanoi) — знаменитая математическая головоломка 18 столетия.
# Она состоит из трех стержней и некоторого числа дисков разных размеров, которые могут быть надеты на стержень.
# Головоломка начинается с того, что диски расположены друг на друге, причем наименьший расположен сверху. Диски образуют конус.
#
# Цель головоломки — переместить всю стопку на другой стержень, следуя этим простым **правилам**:
# * перемещать можно только **один** диск за раз
# * можно брать только **верхний** диск с одной из стопок и помещать на **верхушку** другой стопки или на пустой стержень
# * диск **большего** размера нельзя класть на диск **меньшего** размера
#
# Ваша задача значительно легче, чем придумывать алгоритм, решающий эту задачу :)
#
# Реализуйте функцию `calculate_hanoi`, которая принимает параметры `disk_number` и `turns_speed`.
# `disk_number` — это число **дисков**,
# а `turns_speed` — скорость перемещения дисков (в **ходах** в **час**). Оба параметра являются числами (тип `int`)
#
# Функция `calculate_hanoi` возвращает объект с 2 свойствами:
# * `turns` (минимальное число (тип `int`) ходов, необходимое для решения головоломки)
# * `seconds` (минимальное число (тип `int`) **секунд**, необходимое для решения головоломки при заданной скорости;
# должно быть целым числом, полученным в результате округления результата расчетов в меньшую сторону)
# Вам не нужно валидировать входные параметры.
# Например:
# `calculate_hanoi(9, 4308) => { turns: 511, seconds: 427 }`
# Напишите свой код в `.{your_name}/hanoi_calc.py`.
import math

def calculate_hanoi(disk_number: int, turns_speed: int):
    turns = 2**disk_number - 1
    seconds = math.floor(turns * (3600/turns_speed))
    return {"turns": turns, "seconds": seconds}

print(calculate_hanoi(9, 4308))
