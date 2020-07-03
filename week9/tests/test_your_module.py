from your_module import *
import pytest

def test_multiply_by_two():
    assert multiply_by_two(2) == 4
    assert multiply_by_two(3.6) == 7.2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        3/0
