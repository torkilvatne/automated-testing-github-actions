from createperson.create_person import createAPerson, Mood


def test_create_a_person():
    torkil = createAPerson("Torkil", 26, Mood.Sad)
    assert torkil.name is "Torkil"
    assert torkil.age is 26
    assert torkil.mood is Mood.Sad
