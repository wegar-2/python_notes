

class ExampleClass:

    def __init__(self):
        pass

    @classmethod
    def member_class_method(cls, x):
        print(f"Called method of class {cls.__name__} with argument x = {x}...")

    @staticmethod
    def add_two_numbers(x, y):
        return x + y


ex_ = ExampleClass()
print(ex_.add_two_numbers(12, 2))
ex_.member_class_method(993)

