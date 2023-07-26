
def my_decorator(fn_):
    def wrapper(*args, **kwargs):
        print(f"Starting execution of function {fn_.__name__}...")
        fn_(*args, **kwargs)
        print(f"Starting execution of function {fn_.__name__}!")
    return wrapper


@my_decorator
def my_printer_function(arg1, arg2):
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")


my_printer_function(123, "asdf")
