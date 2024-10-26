import pytest
from app import App
from app.plugins.add import AdditionCommand
from app.plugins.subtract import SubtractionCommand
from app.plugins.multiply import MulitplyCommand
from app.plugins.divide import DivideCommand

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    # assert str(e.value) == "Exiting...", "The app did not exit as expected"