class A:
    def function_a(self):
        return "A"


class B:
    def function_a(self):
        return "B"


class Child(A, B):
    pass


child = Child()
print(child.function_a())  # A