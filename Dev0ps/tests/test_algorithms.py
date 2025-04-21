import pytest
from src.algorithms import divide, square_root

def test_divide_correct():
    assert divide(10, 2) == 5

def test_divide_zero_division():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_divide_negative():
    result = divide(-10, 2)
    assert result == -5

def test_square_root_correct():
    assert square_root(4) == 2

def test_square_root_negative():
    with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
        square_root(-1)
