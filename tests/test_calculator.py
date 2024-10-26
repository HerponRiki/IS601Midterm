'''Gets the functions from folder'''
from calculator import add, subtract

def test_addition():
    '''Test addition'''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test subtraction'''    
    assert subtract(2,2) == 0
