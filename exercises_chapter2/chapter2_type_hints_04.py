from typing import Union


def greeting(name: Union[str, None]) -> str:
    return f"Hello, {name if name else 'Anonymous'}"


print(greeting(""))
