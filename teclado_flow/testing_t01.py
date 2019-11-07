import t01 as te
import pytest
import sys

def test_add():
    assert te.add(7, 3) == 10
    assert te.add(7) == 9
    assert te.add(5) == 7

@pytest.mark.skipif(sys.version_info < (3,3), reason="do not run number add test")
def test_product():
    assert te.product(2, 4) == 8
    assert te.product(5) == 10
    print(te.add(7, 3), '-------------------')

def test_add_strings():
    result = te.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Heldo' not in result

@pytest.mark.strings
def test_product_strings():
    assert te.product('hello ', 3) == 'hello hello hello '
    result = te.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result
