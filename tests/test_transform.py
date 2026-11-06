import pytest
from textutils.transform import character_count, reverse, word_count


# --- character_count ---
@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", 5),
        ("", 0),
        ("a", 1),
        ("hello world", 11),
    ],
)
def test_character_count(text, expected):
    assert character_count(text) == expected


def test_character_count_type_error():
    with pytest.raises(TypeError):
        character_count(None)


# --- reverse ---
@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", "olleh"),
        ("radar", "radar"),
        ("", ""),
        ("12345", "54321"),
    ],
)
def test_reverse(text, expected):
    assert reverse(text) == expected


def test_reverse_type_error():
    with pytest.raises(TypeError):
        reverse(123)


# --- word_count ---
@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello world", 2),
        ("hello", 1),
        ("", 0),
        ("   ", 0),
        ("many   spaces   between", 3),
    ],
)
def test_word_count(text, expected):
    assert word_count(text) == expected


def test_word_count_type_error():
    with pytest.raises(TypeError):
        word_count(None)