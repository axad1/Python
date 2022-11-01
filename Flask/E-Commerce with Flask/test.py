
class Student:
    def __init__(self, name):
        self._name = name


    @property
    def name(self):
        print('getter method called')
        return self._name

    @name.setter
    def name(self, name):
        print('setter method called')
        self._name = name

s = Student('asad')

print(s.name)

