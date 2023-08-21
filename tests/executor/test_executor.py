"""Test for executor class."""

import pytest
from app.executor.executor import Executor
from tests.resources import CODE_EXECUTOR


@pytest.mark.parametrize(
    "output, input_data, code",
    [
        ("1", "1", "print(1)"),
        ("1", "1", "x=input()\nprint(x)"),
        ("10", "5", "x=int(input())\nprint(x*2)"),
        ("[0, 1]", "2", "x=input()\nprint(list(i for i in range(x)))"),
        ("41", "80-25", CODE_EXECUTOR),
    ],
)
def test_executioner(output: str, input_data: str, code: str):
    """Test for executioner method."""
    assert Executor(output, input_data, code).executioner()


@pytest.mark.parametrize(
    "output, input_data, code",
    [
        ("1", "5", "print(2)"),
        ("****", "3", "x=input()\nprint('*'*3)"),
        ("this is a test", "tset a is siht", "w=input()\nprint(word[::-1])"),
        ("7", "6", "print(sum(list(range(1, int(input())+1)))))"),
        ("3", "8-4", CODE_EXECUTOR),
    ],
)
def test_executioner_error(output: str, input_data: str, code: str):
    """Test for executioner method."""
    assert not Executor(output, input_data, code).executioner()
