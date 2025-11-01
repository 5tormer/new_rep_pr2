import pytest

from app1 import divide

def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    assert divide(10, 0) == "Error: division by zero is not allowed"
