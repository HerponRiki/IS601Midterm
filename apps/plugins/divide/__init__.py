import logging

from app.commands import Command
from calculator import Calculator

class DivideCommand(Command):
    def execute(self, a, b):
        logging.info("Divide")
        print(Calculator.divide(a, b))