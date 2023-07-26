

class Sample:

    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3


obj1 = Sample()
print(obj1.__dir__())
_Sample__c

class SecondClass(Sample):
    pass

