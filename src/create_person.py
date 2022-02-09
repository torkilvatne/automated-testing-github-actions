# import enum and auto
from enum import Enum, auto


# Using enum.auto() method
class Mood(Enum):
    Smile = auto()
    Sad = auto()
    Angry = auto()


class Person:
    def __init__(self, name, age, mood):
        self.name = name
        self.age = age
        self.mood = mood


if __name__ == '__main__':
    person = Person("Torkil", 26, Mood.Smile)
    print(person.mood)
