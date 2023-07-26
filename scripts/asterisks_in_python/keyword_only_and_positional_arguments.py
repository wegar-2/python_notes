

def test_function_one(*args, x, y=123):
    print(f"sum: {sum(args)}")
    print(f"x: {x}")
    print(f"y: {y}")


# this will throw a TypeError missing 1 required keyword-only argument
try:
    test_function_one(123, 32, 32, 1, 2)
except Exception as e:
    print(e)

# this will run:
test_function_one(123, 32, 32, x=1, y=2)
