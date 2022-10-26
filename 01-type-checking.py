from typing import List, Tuple, Dict


int_변수: int = 88
str_변수: str = "jaekwanee"
float_변수: float = 88.9
bool_변수: bool = True
list_변수: List[int] = [1, 2, 3]
tuple_변수: Tuple[int, ...] = (1, 3, 4)
dic_변수: Dict[str, int] = {"jaekwan": 26}


def type_check(obj, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"Type Error: {typer}")


def cal_add(x: int, y: int) -> int:
    type_check(x, int)
    type_check(y, int)
    return x + y


print(cal_add(1, 3))

print(cal_add(1, "sgsd")) # TypeError: Type Error: <class 'int'>
