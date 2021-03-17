# 1. Объявить функцию в которой будет объявляться все типы данных python как отдельная переменная,
# функция должна вернуть dict(словарь) со всеми объявлеными типами данных,
# в котором ключем будет тип данных переменной, а значение сама переменная. Функция должна быть взвана в файле.

# 2. Объявить функцию которая будет принимать в аргументах какое то число,
# и производить с этим числом какие нибудь арифметические действия ( минимум 7), функция должна вернуть dict,
# в котором ключем будет являться название арифметического действия, а значением сам результат.
# * Сделать промверку на входящие данные в функцию
# ** Написать тестовую функцию которая будет проверять логику функции.

def variables():
    i = 1
    f = 2.0
    c = 2+3j
    s = "abc"
    l = []
    d = {}
    t = (1, 1)
    m = set("qwertyuiop")
    thisdict = {"Integer": i,
                "Float": f,
                "Complex": c,
                "String": s,
                "List": l,
                "Dictionaries": d,
                "Tuples": t,
                "Multitudes": m,
                "Boolean:": True }
    return thisdict


print(variables())


def func(number: int):
    if isinstance(number, int):
        sum = number+1
        subrtract = number -1
        multiplication = number * 2
        exponentiation = number ** 3
        division = number / 2
        integerDivision = number // 2
        ost = number % 2
        d = {"Суммирование": sum ,
             "Вычитание": subrtract,
             "Умножение": multiplication,
             "Возведение в степень": exponentiation,
             "деление": division,
             "Целочисленное деление": integerDivision,
             "Остаток от деления": ost}
        print(d)
    else :
        return None
    return  d

def test_func(func):
    result: int = func(9)
    assert isinstance(result, dict)
    result: None = func({})
    assert not result
    result: None = func(())
    assert not result
    result: None = func("1")
    assert not result
    result: None = func([])
    assert not result


print(test_func(func))