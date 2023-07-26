

def my_decor(fn_):
    def wrapper_(*args, **kwargs):
        print(f"Starting execution of function {fn_.__name__}...")
        out = fn_(*args, **kwargs)
        print(f"Completed execution of function {fn_.__name__}! ")
        print(f"returning the output: {out}")
        return out
    return wrapper_


@my_decor
def function_accepting_argument(int_len: int):
    return list(range(int_len))


function_accepting_argument(10)
