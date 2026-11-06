import pytest
from textutils.casing import capitalize_words, kebab_case


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


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello world", "hello-world"),
        ("Hello World", "hello-world"),
        ("hello_world", "hello-world"),
        ("", ""),
        ("   multiple   spaces   ", "multiple-spaces"),
    ],
)
def test_kebab_case(text, expected):
    assert kebab_case(text) == expected


def test_kebab_case_type_error():
    with pytest.raises(TypeError):
        kebab_case(None)
    with pytest.raises(TypeError):
        kebab_case(123)