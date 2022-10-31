import itertools

# itertools.count --- keep counting ad infinitum / until break is reached
for el in itertools.count(1, 5):
    print(el)
    if el > 99:
        break

# itertools.cycle --- keep iterating over an iterable until certain condition is met
str_ = ""
for el in itertools.cycle(["q", "w", "e"]):
    str_ += el
    if len(str_) > 10:
        break
print(str_)

