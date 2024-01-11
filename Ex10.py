def test_phrase():
    phrase = input("Введите фразу короче 15 символов: ")
    assert len(phrase) < 15, "Фраза длиннее 15 символов"