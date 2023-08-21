"""Module with resources for testing."""

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
