import logging

from app.commands import Command
from calculator import Calculator

class MulitplyCommand(Command):
    def execute(self, a, b):
        logging.info("Multiplication")
        print(Calculator.multiply(a, b))