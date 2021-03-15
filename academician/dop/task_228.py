# You must write a function that takes a number as a string as arguments, and returns a number.
# Otherwise, return None
# Pay attention to the documentation of the function.

import typing


def is_number(number: str) -> typing.Optional[int]:
    # Your code
    if isinstance(number, str) :
        if number.isdigit():
            return int(number)
        else:
            return None
    else :
        return None


def test_func(func):
    result: int = func('1')
    assert isinstance(result, int)
    result: None = func({})
    assert not result
    result: None = func(())
    assert not result
    result: None = func(1)
    assert not result
    result: None = func([])
    assert not result


test_func(is_number)