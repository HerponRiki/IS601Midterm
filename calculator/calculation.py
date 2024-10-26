from decimal import Decimal
from typing import Callable

from calculator.operations import add, subtract, multiply, divide


# Calculation class with type hints
class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation  # Store the operation function
    
    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        ''' Return a new Calculation object initialized with the provided arguments '''
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        ''' Perform the stored calculation and return the result '''
        return self.operation(self.a, self.b)

    def __repr__(self):
        ''' Return a simplified string representation of the calculation '''
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
