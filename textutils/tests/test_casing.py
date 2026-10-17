import pytest
from textutils.casing import capitalize_words


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello world", "Hello World"),
        ("ensisa", "Ensisa"),
        ("", ""),
        ("multiple   spaces", "Multiple   Spaces"),
        ("123 test", "123 Test"),
    ],
)
def test_capitalize_words(text, expected):
    assert capitalize_words(text) == expected


def test_capitalize_words_type_error():
    with pytest.raises(TypeError):
        capitalize_words(None)
    with pytest.raises(TypeError):
        capitalize_words(123)