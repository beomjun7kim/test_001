import subprocess
import sys

from test_001.main import add, greet


def test_add():
    assert add(2, 3) == 5


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_name():
    assert greet("Alice") == "Hello, Alice!"


def test_cli_greet():
    p = subprocess.run(
        [sys.executable, "-m", "test_001.main", "--greet", "Bob"], capture_output=True, text=True
    )
    assert "Hello, Bob!" in p.stdout


def test_cli_sum():
    p = subprocess.run(
        [sys.executable, "-m", "test_001.main", "--sum", "4", "6"], capture_output=True, text=True
    )
    assert "10" in p.stdout
