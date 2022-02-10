from createperson.create_person import create_a_person, Mood
import pytest
import sys


@pytest.fixture
def basic_person():
    return create_a_person("Torkil Basic", 99, Mood.Angry)


@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = {"stdout": "", "write_calls": 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, 'write', fake_write)
    return buffer
