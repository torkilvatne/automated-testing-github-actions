from createperson.create_person import create_a_person, Mood
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (["Torkil", 26, Mood.Smile], ["Torkil", 26, Mood.Smile]),
        (["Eric", 28, Mood.Angry], ["Eric", 28, Mood.Angry]),
    ],
)
def test_create_a_person(test_input, expected):
    test_person = create_a_person(test_input[0], test_input[1], test_input[2])
    assert test_person.name is expected[0]
    assert test_person.age is expected[1]
    assert test_person.mood is expected[2]
    test_person.increment_age()
    assert test_person.age is expected[1] + 1


@pytest.mark.skip
def test_to_skip():
    print("This test should be skipped")


@pytest.mark.xfail
def test_to_skip():
    test_person = create_a_person("Torkil", 26, Mood.Smile)
    assert test_person.name is "Eric"


def test_invalid_mood():
    with pytest.raises(AttributeError):
        create_a_person("Torkil", 26, Mood.Happy)


def test_fixture_person(basic_person):
    assert basic_person.name == "Torkil Basic"


def test_print(capture_stdout):
    print("This captures the stdout output into a replica buffer")
    assert (
        capture_stdout["stdout"]
        == "This captures the stdout output into a replica buffer\n"
    )


# https://www.youtube.com/watch?v=DhUpxWjOhME
