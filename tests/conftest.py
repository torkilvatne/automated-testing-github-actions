from createperson.create_person import create_a_person, Mood
import pytest


@pytest.fixture
def basic_person():
    return create_a_person("Torkil Basic", 26, Mood.Angry)
