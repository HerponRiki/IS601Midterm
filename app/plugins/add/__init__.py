import logging

from app.commands import Command
from calculator import Calculator

class AdditionCommand(Command):
    def execute(self, a, b):
        logging.info("Addition")
        print(Calculator.add(a, b))
    
