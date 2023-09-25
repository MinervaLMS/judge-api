"""judge_api constants"""

KEYS_REQUESTED = (
    "code",
    "language",
    "submission",
    "input",
    "output",
    "time_limit",
    "memory_limit",
)

RUNTIME = {
    "g++": "/usr/bin/g++",
    "g++11": "/usr/bin/g++",
    "g++14": "/usr/bin/g++",
    "g++17": "/usr/bin/g++",
    "g++20": "/usr/bin/g++",
    "python3": "/usr/bin/python3",
}

JUDGE_ROOT = "/mnt"

PROBLEMS_FOLDER = "/../mnt/problems/"