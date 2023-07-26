# article URL: https://realpython.com/python-iterators-iterables/#getting-to-know-python-iterables

# Iterators: power and control the iteration process
# Iterables: typically hold data that you want to iterate over one value at a time

# Iterator - definition: an object that allows you to iterate over collections of data, such as lists,
#                       tuples, dictionaries, and sets.

# Iterator protocol: __iter__() and __next__() methods
# NOTE: The .__iter__() method of an iterator typically returns self, which holds a
# reference to the current object: the iterator itself.


class MyNumberVault:

    def __init__(self):
        self.l_vault = []
        self.counter = 0

    def get_numbers(self):
        return self.l_vault

    def add_number_to_vault(self, num: int):
        self.l_vault.append(num)

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.l_vault):
            out = self.l_vault[self.counter]
            self.counter += 1
        else:
            raise StopIteration
        return out


obj1 = MyNumberVault()
obj1.add_number_to_vault(123)
obj1.add_number_to_vault(13)
obj1.add_number_to_vault(12)
obj1.add_number_to_vault(12111)

for key, num in enumerate(obj1):
    print(f"element {key}: {num}")

