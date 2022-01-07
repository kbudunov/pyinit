from typing import Literal, Final, final, Dict, Any


# f = open(r'readme.md', 'v')  # WTF?


# Literal (лучше использовать енумерейшн)
def open_file(file, mode: Literal['r', 'v']):
    pass


# установи плагин и пакет mypy
# open_file(r'readme.md', 's') #проверяет что нет s в Literal['r', 'v']


# константы
pi: Final = 3.14


# pi = 1.2 не позволяет изменять


# запечатаные классы Final (без наследования)
@final
class Dog:
    def __init__(self):
        self.paws = 4

    def bark(self):
        print('hello!')


# class SuperDog(Dog):
class SuperDog():
    def __init__(self):
        self.paws = 5
        self.health = 100


dog = SuperDog()
print(dog.health)
# dog.bark()


person: Dict[str, str] = {"name": "Ivan", "lastname": "Ivanov"}
person2: Dict[str, Any] = {"name": "Ivan", "age": 23}
person2['name'] = 123  # пролезет другой тип

# в 3.8 появился TypedDict
from typing import TypedDict


class WordStat(TypedDict):
    name: str
    age: int


person3: WordStat = {"name": "Ivan", "age": 23}
