from typing import Any


def f(x: Any) -> Any:
    return x


f("a")  # a
print(f("a"))
f(10)  # 10
print(f(10))
f([1, 2, 3])  # [1, 2, 3]
print(f([1, 2, 3]))
