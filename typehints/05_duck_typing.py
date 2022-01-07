from asyncio import Protocol
from typing import List


class Bird:
    def fly(self):
        print('fly with wings')

class Airplain:
    def fly(self):
        print('fly with fuel')

class Fish:
    def swim(self):
        print('fly with fuel')

def process_flyables(flyables):
    for c in flyables:
        c.fly()

#это УТИНАЯ ТИПИЗАЦИЯ в питоне
process_flyables([Bird(), Airplain()])
#process_flyables([Bird(), Airplain(), Fish()]) ругнется только в момент выполнения

#ПРОТОКОЛ (как интерфейс маркер) нотка статической типизации
class Flyable(Protocol):
    def fly(self): ...

def process_flyables2(flyables: List[Flyable]):
    for c in flyables:
        c.fly()

process_flyables([Bird(), Airplain()])
#process_flyables2([Bird(), Airplain(), Fish()]) ругнется сразу