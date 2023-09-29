"""Module with resources for testing."""

DATA = {
    "code": "print(int(input())**2)",
    "problem_id": "test_power2",
    "submission_id": "18",
    "time_limit": 1,
    "memory_limit": 9999,
    "language": "py3",
}


CODE_EXECUTOR = """
n, k = map(int,input().split("-"))
circle = list(range(1, n + 1))
index = 0
result = []
for i in range(n-1):
    index = (index + k - 1) % len(circle)
    circle.pop(index)
print(circle[0])
"""

DATA_ENDPOINT = {
    "code": "print(int(input())**2)",
    "problem_id": "test_power2",
    "submission_id": "18",
    "time_limit": 1,
    "memory_limit": 9999,
    "language": "py3",
}

DATA_PROBLEM = {
    "input": ["4\n1\n2\n3\n4", "8\n1\n5\n2\n3\n2\n3\n4\n5"],
    "output": ["La suma es 10", "La suma es 25"],
    "problem_id": "EDM05E01",
    "points": [45, 75],
}
