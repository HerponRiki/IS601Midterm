from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, arg: str):
        try:
            """
            Tracks how long the string is then seperates it.
            ex. add 10 2 will print 12
            """
            command_name = arg.split(" ")[0]
            if len(arg.split(" ")) == 3:
                arg1 = arg.split(" ")[1]
                arg2 = arg.split(" ")[2]
                self.commands[command_name].execute(float(arg1), float(arg2))
            else:
                self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")