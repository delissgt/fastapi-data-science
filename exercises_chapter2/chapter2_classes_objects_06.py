class Parent:

    def my_function(self):
        return "A"


class Child(Parent):
    def my_function(self):
        parent_result = super().my_function()
        return f"Child {parent_result}"


child = Child()

print("Child::", child.my_function())
