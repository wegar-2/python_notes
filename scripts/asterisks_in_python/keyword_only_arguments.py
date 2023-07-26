

def my_benchmark_function(x, y, z):
    print(x)
    print(y)
    print(z)


def my_keyword_only_args_function(*, x, y, z):
    print(x)
    print(y)
    print(z)


my_benchmark_function(3, 4, 1)
my_benchmark_function(y=4, x=3, z=1)

try:
    my_keyword_only_args_function(1, 2, 3)
except Exception as e:
    print(e)



