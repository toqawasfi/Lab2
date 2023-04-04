import pytest
from serise.serise import fibonacci
from serise.serise import lucas
from serise.serise import sum_series
def test_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected 

def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected 

def test_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected 

def test_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected 
    
def test_zero_lucas():
    actual = lucas(0)
    expected = 2
    assert actual == expected 

def test_one_lucas():
    actual = lucas(1)
    expected = 1
    assert actual == expected 

def test_zero_one():
    actual=sum_series(3)
    expected = 2
    assert actual == expected 
def test_two_one():
    actual=sum_series(3,2,1)
    expected =4
    assert actual == expected 

def test_four_five():
    actual=sum_series(3,4,5)
    expected = 6
    assert actual == expected 

