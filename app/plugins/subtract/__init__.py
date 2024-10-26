import logging

from app.commands import Command
from calculator import Calculator

class SubtractionCommand(Command):
    def execute(self, a, b):
        logging.info("Subtraction")
        print(Calculator.subtract(a, b))