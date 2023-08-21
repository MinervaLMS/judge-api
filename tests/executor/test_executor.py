"""Test for executor class."""

import pytest
from app.executor.executor import Executor


@pytest.mark.parametrize(
    "output, input_data, code",
    [
        ("1", "1", "print(1)"),
        ("1", "1", "x=input()\nprint(x)"),
        ("10", "5", "x=int(input())\nprint(x*2)"),
        ("6", "6", "print(sum([1,2,3]))"),
        ("[0, 1]", "2", "x=input()\nprint(list(i for i in range(x)))"),
        ("***", "3", "x=input()\nprint('*'*3)"),
    ],
)
def test_executioner(output, input_data, code):
    """Test for executioner method"""
    assert Executor(output, input_data, code).executioner()
