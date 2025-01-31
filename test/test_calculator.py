import pytest
from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3

def test_subtract():
    calc = Calculator()
    assert calc.subtract(4, 2) == 2

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 5) == 10

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)