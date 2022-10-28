# * Callable types


from typing import Callable


def add(a: int, b: int) -> str:
    return "a" + "b"


def test_add(func: Callable[[int, int], str]) -> int:
    return func(2, 3)


print(test_add(add))
