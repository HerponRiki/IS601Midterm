import pytest

from decimal import Decimal
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def setup_calculations():
    ''' Clear history and add sample calculations for tests '''
    Calculations.clear_history()  # Ensure a clean state before each test
    # Adding sample calculations to the history for tests
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), multiply))
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('2'), divide))

def test_add_calculation(setup_calculations):
    ''' Test adding a calculation '''
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history(setup_calculations):
    ''' Test retrieving calculation history '''
    history = Calculations.get_history()
    assert len(history) == 4, "History does not contain the expected number of calculations"

def test_clear_history(setup_calculations):
    ''' Test clearing the calculation history.'''
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations):
    ''' Test getting the latest calculation '''
    latest = Calculations.get_latest()
    assert latest.a == Decimal('10') and latest.b == Decimal('2'), "Did not get the correct latest calculation"

def test_find_by_operation(setup_calculations):
    ''' Test finding calculations by operation type '''
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, "Did not find the correct number of calculations with add operation"

    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations with subtract operation"

    multiply_operations = Calculations.find_by_operation("multiply")
    assert len(multiply_operations) == 1, "Did not find the correct number of calculations with multiply operation"

    divide_operations = Calculations.find_by_operation("divide")
    assert len(divide_operations) == 1, "Did not find the correct number of calculations with divide operation"

def test_get_latest_with_empty_history():
    ''' Test getting the latest calculation when history is empty '''
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history"
