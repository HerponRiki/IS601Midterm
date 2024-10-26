from calculator.operations import add, subtract, multiply, divide

# Defines Calculation class
class Calculation:
    def __init__(self, a, b, operation):
        self.a = a 
        self.b = b 
        self.operation = operation # Get the names of the functions in operations

    def get_result(self):
        return self.operation(self.a, self.b)

# Defines Calculator class
class Calculator:
    @staticmethod
    def add(a,b):
        calculation = Calculation(a, b, add)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def subtract(a,b):
        calculation = Calculation(a, b, subtract)  # Pass the subtract function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def multiply (a,b):
        calculation = Calculation(a, b, multiply)  # Pass the multiply function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def divide(a,b):
        calculation = Calculation(a, b, divide)  # Pass the divide function from calculator.operations
        return calculation.get_result()