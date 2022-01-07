from typing import overload


@overload
def add(x: int) -> int: ...

@overload
def add(x: int) -> str: ...