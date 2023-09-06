"""Module with resources for testing."""

DATA = {
    "code": "print(int(input())**2)",
    "input": "3",
    "output": "9",
    "time_limit": 5000,
    "memory_limit": 256,
    "language": "py3",
}


CODE_EXECUTOR = """
n, k = map(int,'input()'.split("-"))
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
    "submission": "19Aa7B",
    "input": "3",
    "output": "9",
    "time_limit": 5000,
    "memory_limit": 256,
    "language": "py3",
}

DATA_PROBLEM = {
    "input": ["4\n1 2 3 4", "8\n1 5 2 3 2 3 4 5"],
    "output": ["La suma es 10", "La suma es 25"],
    "problem_id": "EDM05E01",
    "points": [45, 75],
}
