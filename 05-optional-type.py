from typing import Union, Optional

jaekwan: Union[str, None] = "Hi"

jaekwan: Optional[str] = "Hi"


def test(name: str) -> Optional[str]:
    if name == "jaekwan":
        return None
    else:
        return name
