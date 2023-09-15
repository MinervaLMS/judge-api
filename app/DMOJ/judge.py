"""This module contains the class for interacting with the judge DMOJ."""
from app.DMOJ.submission import Submission
from app.DMOJ.judge_connection import SingletonJudge


class Judge:
    """
    Represents a judge to evaluate the submissions with dmoj.
    """

    @classmethod
    def submit(self, submission: Submission, judge_connection: SingletonJudge) -> list:
        """
        Makes a submission in DMOJ.
        Args:
            submission (Submission): The submission to be graded.
            judge_connection (SingletonJudge): A connection to the DMOJ judge.

        Returns:
            list: A list of dictionaries containing grading information for the submission.
        """

        judge_connection.judge.begin_grading(
            submission,
            blocking=True,
        )
        response = list(judge_connection.response)
        judge_connection.response = []
        return response
