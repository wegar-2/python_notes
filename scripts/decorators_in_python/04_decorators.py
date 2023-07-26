
def my_decorator(fn):
    def internal_():
        fn()
        fn()
    return internal_


@my_decorator
def print_text():
    print("qwerty")


print_text()
