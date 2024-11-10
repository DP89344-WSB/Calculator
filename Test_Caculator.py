import pytest
from Calculator import SimpleListOperations

@pytest.fixture
def sl_operations():
    """Tworzy obiekt SimpleListOperations do użycia w testach."""
    return SimpleListOperations()

def test_add_number(sl_operations):
    """Test dodawania liczby do listy."""
    sl_operations.add_number(5)
    assert 5 in sl_operations.numbers

def test_remove_number(sl_operations):
    """Test usuwania liczby z listy."""
    sl_operations.add_number(10)
    sl_operations.remove_number(10)
    assert 10 not in sl_operations.numbers

def test_remove_number_not_in_list(sl_operations):
    """Test próby usunięcia liczby, której nie ma na liście."""
    sl_operations.add_number(10)
    sl_operations.remove_number(20)
    assert 10 in sl_operations.numbers  # Nic się nie zmienia

def test_is_empty_when_empty(sl_operations):
    """Test sprawdzenia, czy lista jest pusta, gdy jest pusta."""
    assert sl_operations.is_empty() is True

def test_is_empty_when_not_empty(sl_operations):
    """Test sprawdzenia, czy lista jest pusta, gdy zawiera elementy."""
    sl_operations.add_number(5)
    assert sl_operations.is_empty() is False

def test_average_with_values(sl_operations):
    """Test obliczania średniej z liczb w liście."""
    sl_operations.add_number(10)
    sl_operations.add_number(20)
    sl_operations.add_number(30)
    assert sl_operations.average() == 20

def test_average_empty_list(sl_operations):
    """Test obliczania średniej z pustej listy (powinien rzucić wyjątek)."""
    with pytest.raises(ValueError):
        sl_operations.average()

def test_find_max(sl_operations):
    """Test znajdowania największej liczby w liście."""
    sl_operations.add_number(5)
    sl_operations.add_number(10)
    sl_operations.add_number(3)
    assert sl_operations.find_max() == 10

def test_find_max_empty_list(sl_operations):
    """Test próby znalezienia największej liczby w pustej liście (powinien rzucić wyjątek)."""
    with pytest.raises(ValueError):
        sl_operations.find_max()

def test_add_multiple_numbers(sl_operations):
    """Test dodawania wielu liczb na raz."""
    sl_operations.add_number(1)
    sl_operations.add_number(2)
    sl_operations.add_number(3)
    assert sl_operations.numbers == [1, 2, 3]

def test_remove_multiple_occurrences(sl_operations):
    """Test usuwania kilku wystąpień tej samej liczby."""
    sl_operations.add_number(5)
    sl_operations.add_number(5)
    sl_operations.remove_number(5)
    assert sl_operations.numbers == [5]

def test_edge_case_large_number(sl_operations):
    """Test dodawania dużych liczb."""
    large_number = 10**9
    sl_operations.add_number(large_number)
    assert large_number in sl_operations.numbers

def test_edge_case_small_number(sl_operations):
    """Test dodawania małych liczb (np. zerowych)."""
    sl_operations.add_number(0)
    assert 0 in sl_operations.numbers


def test_remove_number_not_exist(sl_operations):
    """Test próby usunięcia liczby, której nie ma na liście (lista pozostaje niezmieniona)."""
    sl_operations.add_number(7)
    sl_operations.remove_number(99)
    assert sl_operations.numbers == [7]
