def tip ():
    a = 2
    b = 2.5
    c = "Hello"
    d = [5, "Hello"]
    e = {}
    f = ("qwerty", 10.5)
    g = set("abcdefg")
    i = 3 + 0.2j
    w = True
    dict = {type(a): a,
            type(b): b,
            type(c): c,
            type(d): d,
            type(e): e,
            type(f): f,
            type(g): g,
            type(i): i,
            type(w): w
            }
    return dict
print(tip())

def func(x: int):
    if isinstance(x, int):
        a = x+4
        b = x-7
        c = x*2
        d = x//3
        e = x**2
        f = x%3
        g = x/3
        dictionaries={"сложение чисел": a,
                  "вычитание чисел": b,
                  "умножение чисел": c,
                  "целочисленное деление":d,
                  "возведение в степень":e,
                  "остаток от деления":f,
                  "деление чисел":g
                  }
        return dictionaries
    else:
        print("Можно вводить только целые числа")
print(func(5))
