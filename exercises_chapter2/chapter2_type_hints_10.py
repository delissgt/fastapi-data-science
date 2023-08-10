from typing import Any, cast


def f(x: Any) -> Any:
    return x


# a = f("a") # inferrent type is any

a = cast(str, f(1.22))  # forced type to be "str"

print("a", a)
print("a-", type(a))
