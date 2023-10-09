"""Test for executor class."""

import pytest
from app.executor.executor import Executor
from tests.resources import CODE_EXECUTOR


@pytest.mark.parametrize(
    "problem_id, submission_id, time_limit, memory_limit, language, code",
    [
        ("test_1", "submit_1",1,9999,"PY3","print(1)"),
        ("test_2", "submit_2",1,9999,"PY3", "x=input()\nprint(x)"),
        ("test_3", "submit_3",1,9999,"PY3", "x=int(input())\nprint(x*2)"),
        ("test_4", "submit_4",1,9999,"PY3", "x=int(input())\nprint(list(i for i in range(x)))"),
        ("test_5", "submit_5",1,9999,"PY3", CODE_EXECUTOR),
    ],
)
def test_executioner(problem_id: str, submission_id: str, time_limit: int, memory_limit: int, language: str, code: str, test_problems_executor):
    """Test for executioner method."""
    
    """Creating problems for test executor"""
    test_problems_executor
    
    assert Executor(problem_id, submission_id, time_limit, memory_limit, language, code).executioner()


@pytest.mark.parametrize(
    "problem_id, submission_id, time_limit, memory_limit, language, code",
    [
        ("test_1", "submit_1",1,9999,"PY3", "print(2)"),
        ("test_2", "submit_2",1,9999,"PY3", "x=input()\nprint('*'*3)"),
        ("test_3", "submit_3",1,9999,"PY3", "w=input()\nprint(word[::-1])"),
        ("test_4", "submit_4",1,9999,"PY3", "print(sum(list(range(1, int(input())+1)))))"),
    ],
)
def test_executioner_error(problem_id: str, submission_id: str, time_limit: int, memory_limit: int, language: str, code: str, test_problems_executor):
    """Test for executioner method."""
    
    """Creating problems for test executor"""
    test_problems_executor
    
    assert not Executor(problem_id, submission_id, time_limit, memory_limit, language, code).executioner()
