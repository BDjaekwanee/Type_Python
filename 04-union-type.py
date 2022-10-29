from typing import Union

xxx: Union[int, str] = 3

xxx = "jaekwan"  # 가능 pyright 안걸림.


def test(x: Union[int, str]) -> None:
    print(x)


test(16)
test("ok")
