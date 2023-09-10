"""Module with executor class."""

import io
import sys
from app.DMOJ.submission import Submission
from app.DMOJ.judge import Judge
from app.DMOJ.judge_connection import SingletonJudge


class Executor:
    """Class that conects the judge with the code."""

    def __init__(self, output: str, input_data: str, code: str):
        self.output = output
        self.input_data = input_data
        self.code = code

    def judge(self) -> dict:
        """Method that runs the code on the judge."""

        judge_connection = SingletonJudge()

        submission = Submission(1, "2323", "TEST", self.code, "PY3", 1, 80760)
        ans = Judge.submit(submission, judge_connection)
        verdict = ans[-1]["flag"]
        return {"verdict": "WA" if verdict == 1 else "AC"}

    def executioner(self) -> bool:
        """Method that returns the result of the execution."""
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        try:
            new_code = self.code.replace("input()", "{}")
            new_code = new_code.format(self.input_data)

            exec(new_code)  # pylint:  disable=exec-used

            output_value = new_stdout.getvalue().strip()
            sys.stdout = old_stdout

            if output_value == self.output:
                return True
            return False

        except Exception:  # pylint: disable=broad-except
            output_value = new_stdout.getvalue().strip()
            sys.stdout = old_stdout
            return False
