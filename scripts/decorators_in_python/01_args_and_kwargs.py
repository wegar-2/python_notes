

def my_function(*args):
    print(args)
    return sum(args)


my_function(1, 3, 2.3)


def my_dict_printer(**kwargs):
    print("kwargs: ", kwargs)
    for key_, val_ in kwargs.items():
        print(f"{key_}: {val_}")


my_dict_printer(asf=123, reer=33)
