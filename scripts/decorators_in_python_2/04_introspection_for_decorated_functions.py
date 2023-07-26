

def my_decor(fn_):
    def wrapper_(*args, **kwargs):
        print(f"Before calling {fn_.__name__}")
        fn_(*args, **kwargs)
        print(f"After call to {fn_.__name__}")
    return wrapper_


@my_decor
def my_decored_fun(x, y, *args, z, **kwargs):
    print(f"Inside {my_decored_fun.__name__}...")
    print(f"\tx: {x}")
    print(f"\ty: {y}")

    print("Printing args...")
    for el in args:
        print(f"Printing consecutive element of args: {el}")
    print("Done printing args! ")

    print(f"\tz: {z}")

    print("Printing kwargs...")
    for key_, val_ in kwargs.items():
        print(f"Printing consecutive element of kwargs ---: {key_}: {val_}")
    print("Done printing args! ")

    return True


my_decored_fun(1, 2, 3, 4, z=123, a=1234, b=12345)

