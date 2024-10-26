import sys
from app.commands import Command


class MenuCommand(Command):
    def execute(self):
        print("""addition - ex add 1 2
subtraction - ex subtract 4 3
multiplication - ex multiply 2 2
division - ex divide 4 2""")