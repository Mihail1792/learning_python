# ### **Рекурсивный вычислитель глубины**
# ![Идти глубже](https: // i.imgur.com / k7lADiM.jpg)
#
# Ваша задача — реализовать класс `DepthCalculator` с
# методом `calculate_depth`, который принимает массив и возвращает его ** глубину **.

# Метод `calculate_depth` должен
# проходить полученный массив ** рекурсивно **.Глубина ** плоского ** массива — 1.
# Метод должен корректно работать с массивами, не содержащими элементов
# или содержащими пустые массивы, метод должен быть свойством класса.
# Например:
# `some_arr = [[[]]]
# `depth_calc = DepthCalculator(arr: list = some_arr);`
# `depth_calc.calculate_depth([[[]]])` = > `3`
lst = [1, 2, [3, 4, [5, 6], [[7, 5], 8]]]
lst_2 = [[[0]],[1]]

def get_depth(list_):
    return 1 + max(get_depth(itm) for itm in list_) if type(list_) == list else 0


print(get_depth(lst))
