"""judge_api constants"""

KEYS_REQUESTED = (
    "problem_id",
    "submission_id",
    "time_limit",
    "memory_limit",
    "language",
    "code"
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

PROBLEMS_FOLDER = "/mnt/problems/"

FLAGS_ERRORS={
    0: {"verdict": "AC",
        "message": "Accepted"},
    1: {"verdict": "WA",
        "message": "Wrong Answer"},
    17: {"verdict": "IR",
        "message": "Invalid Return"},
    3: {"verdict": "RTE",
        "message": "Runtime Error"},
    25: {"verdict": "MLE",
        "message": "Memory Limit Exceeded"},
    9: {"verdict": "MLE",
        "message": "Memory Limit Exceeded"},
    7: {"verdict": "TLE",
        "message": "Time Limit Exceeded"},
    #Without OLE - Output Limit Exceeded  and IE - Internal Error
}
