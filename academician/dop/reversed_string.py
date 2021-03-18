#Complete the solution so that it reverses the string passed into it.

import typing


def revers_str(s: str) -> typing.Optional[str]:
    s = s[::-1]
    return  s


print(revers_str("Words"))


def rever_str_2(s: str) -> typing.Optional[str]:
    if isinstance(s, str):
        f = []
        for l in s.split(" "):
            l1 = l[::-1]
            f.append(l1)
        return str(f)
print(rever_str_2("qweqwe uiop rtyuio dfghjkl cvbnm,"))