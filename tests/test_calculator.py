'''Pull the Calculator class in the calculator folder from the __init__.py file'''
from calculator import Calculator

def test_addition():
    '''Test addition'''    
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test subtraction'''    
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    '''Test multiplication'''
    assert Calculator.multiply(2,3) == 6

def test_divide():
    '''Test divide'''
    assert Calculator.divide(6,3) == 2
