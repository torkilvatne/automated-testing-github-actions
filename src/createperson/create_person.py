from dataclasses import dataclass
from enum import Enum, auto


class Mood(Enum):
    Smile = auto()
    Sad = auto()
    Angry = auto()


@dataclass
class Person:
    name: str
    age: int
    mood: Mood

    def increment_age(self):
        self.age += 1


def create_a_person(name, age, mood) -> Person:
    return Person(name, age, mood)
