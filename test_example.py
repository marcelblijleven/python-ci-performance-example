import pytest

from main import example


def test_example():
    assert example('3113322113') == 4666278
