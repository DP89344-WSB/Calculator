import pytest
from app import add, subtract, concatenate, reverse_string, get_max, get_average, count_occurrences

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-5, -5) == 0

def test_concatenate():
    assert concatenate("Hello", "World") == "HelloWorld"
    assert concatenate("", "World") == "World"
    assert concatenate("Hello", "") == "Hello"

def test_reverse_string():
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

def test_get_max():
    assert get_max([1, 2, 3, 4, 5]) == 5
    assert get_max([-1, -2, -3]) == -1
    with pytest.raises(ValueError):
        get_max([])

def test_get_average():
    assert get_average([1, 2, 3, 4, 5]) == 3
    assert get_average([-1, -2, -3]) == -2
    with pytest.raises(ValueError):
        get_average([])

def test_count_occurrences():
    assert count_occurrences([1, 2, 2, 3], 2) == 2
    assert count_occurrences([1, 1, 1, 1], 1) == 4
    assert count_occurrences([], 1) == 0
