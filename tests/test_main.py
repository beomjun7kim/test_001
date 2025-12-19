import subprocess
import sys
import pathlib

# 테스트 실행 시 현재 작업 디렉터리를 모듈 경로에 추가합니다.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from main import add, greet  # noqa: E402


def test_add():
    assert add(2, 3) == 5


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_name():
    assert greet("Alice") == "Hello, Alice!"


def test_cli_greet():
    p = subprocess.run(
        [sys.executable, "main.py", "--greet", "Bob"], capture_output=True, text=True
    )
    assert "Hello, Bob!" in p.stdout


def test_cli_sum():
    p = subprocess.run(
        [sys.executable, "main.py", "--sum", "4", "6"], capture_output=True, text=True
    )
    assert "10" in p.stdout
