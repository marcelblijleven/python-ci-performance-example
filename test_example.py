import pytest

from main import iterate


@pytest.mark.parametrize(
    ["value", "expected"],
    [
        ("1", "11"),
        ("11", "21"),
        ("21", "1211"),
        ("1211", "111221"),
        ("111221", "312211"),
        ("3113322113", "132123222113"),
        ("132123222113", "111312111213322113"),
    ],
)
def test_iterate(value, expected):
    assert expected == iterate(value)
