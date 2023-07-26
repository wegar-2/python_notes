
# create a dict
dict1 = {"a": 1, "b": 2}
dict2 = dict([("a", 1), ("b", 2)])

print(dict1 == dict2)


# add new dict member (setter features)
dict1.update(c=3)
dict1.update({"d": 4})

print(dict1.get("e") is None)
print(dict1.get("z", "not available..."))

