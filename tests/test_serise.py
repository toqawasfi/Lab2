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

def test_sum_series_test1():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_test2():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_sum_series_test3():
    actual = sum_series(7)
    expected = 13
    assert actual == expected

def test_sum_series_test4():
    actual = sum_series(0,2,1)
    expected = 2
    assert actual == expected

def test_sum_series_test5():
    actual = sum_series(1,2,1)
    expected = 1
    assert actual == expected

def test_sum_series_test6():
    actual = sum_series(2,1,2)
    expected = 3
    assert actual == expected

def test_sum_series_test7():
    actual = sum_series(3,2,1)
    expected = 4
    assert actual == expected

def test_sum_series_test9():
    actual = sum_series(4,2,1)
    expected = 7
    assert actual == expected

def test_sum_series_test10():
    actual = sum_series(5,2,1)
    expected = 11
    assert actual == expected
    
    # 3,5,8,13,21,34,55
def test_sum_series_test11():
    actual = sum_series(2,3,5)
    expected = 8
    assert actual == expected


def test_sum_series_test12():
    actual = sum_series(0,3,5)
    expected = 3
    assert actual == expected

def test_sum_series_test13():
    actual = sum_series(3,3,5)
    expected = 13
    assert actual == expected


def test_sum_series_test17():
    actual = sum_series(5,3,5)
    expected = 34
    assert actual == expected


#  7,11,18,29,47,76,...
def test_sum_series_test14():
    actual = sum_series(0,7,11)
    expected = 7
    assert actual == expected

def test_sum_series_test15():
    actual = sum_series(3,7,11)
    expected = 29
    assert actual == expected

def test_sum_series_test16():
    actual = sum_series(5,7,11)  
    expected = 76
    assert actual == expected