#Complete the solution so that it reverses the string passed into it.

import typing


def revers_str(s: str) -> typing.Optional[str]:
    s = s[::-1]
    return  s


print(revers_str("Words"))


def rever_str_2(s: str) -> typing.Optional[list]:
    if isinstance(s, str):
        f = []
        for l in s.split(" "):
            f.append(l[::-1])
        return f
    else:
        return None
#print(rever_str_2("qweqwe uiop rtyuio dfghjkl cvbnm,"))

def test_func(rever_str_2):
    result: str = rever_str_2("9qweqwe uiop rtyuio dfghjkl cvbnm,")
    assert isinstance(result, list)
    result: None = rever_str_2({})
    assert not result
    result: None = rever_str_2(())
    assert not result
    result: None = rever_str_2(1)
    assert not result
    result: None = rever_str_2([])
    assert not result

print(test_func(rever_str_2))