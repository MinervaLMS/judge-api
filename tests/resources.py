"""Module with resources for testing."""

"""Submission for the unit tests"""
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
