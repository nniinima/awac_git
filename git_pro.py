def hello():
    return "Hello World!"

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_age(self, x):
        self._name = x

    def set_age(self, x):
        self._age = x

    def __str__(self):
            return f'name: {self._name}, age: {self._age}'