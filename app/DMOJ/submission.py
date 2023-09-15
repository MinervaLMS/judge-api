"""This module contains Submissions class"""


class Submission:
    """
    Represents a submission for a programming problem in Minerva.
    """

    def __init__(
        self,
        id: int = None,
        submission_id: str = None,
        problem_id: str = None,
        source: str = None,
        language: str = None,
        time_limit: int = None,
        memory_limit: int = None,
        meta: dict = {},
        short_circuit: bool = False,
    ):
        """
        Initializes an instance of Submission for make submissions.

        Args:
            - id (int): The id of the submission for DMOJ
            - submission_id (str): The submission_id.
            - problem_id (str): The problem_id to grade
            - source (str): The the source code
            - language (str): Language to grade in (e.g., PY2)
            - time_limit (int): Time limit for grading, in seconds
            - memory_limit (int): Memory limit for grading, in kilobytes
            - meta (Dic): under review, studying dmoj functionality
            - short_circuit (bool): under review, studying dmoj functionality
        """

        self.id = id
        self.submission_id = submission_id
        self.problem_id = problem_id
        self.source = source
        self.language = language
        self.time_limit = time_limit
        self.memory_limit = memory_limit
        self.meta = meta
        self.short_circuit = short_circuit
