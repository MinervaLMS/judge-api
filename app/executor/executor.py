"""Module with executor class."""

import io
import sys
from app.DMOJ.submission import Submission
from app.DMOJ.judge import Judge
from app.DMOJ.judge_connection import SingletonJudge
from app.utils.constants import FLAGS_ERRORS

class Executor:
    """Class that conects the judge with the code."""

    def __init__(self, problem_id: str, submission_id: str, time_limit: int, memory_limit: int, language: str, code: str):
        self.problem_id = problem_id
        self.submission_id = submission_id
        self.time_limit = time_limit
        self.memory_limit = memory_limit
        self.language = language 
        self.code = code

    def judge(self) -> dict:
        """Method that runs the code on the judge."""
        """Return a resume of veredicts as a dict"""

        judge_connection = SingletonJudge()

        submission = Submission(id=1,
                                problem_id=self.problem_id,
                                submission_id=self.submission_id, 
                                time_limit=self.time_limit,
                                memory_limit=self.memory_limit,
                                language=self.language, 
                                source=self.code
                                )
        ans = Judge.submit(submission, judge_connection)
        
        memories=[dic['max_memory'] for dic in ans]
        wa=[dic['flag'] for dic in ans]
        exec_times=[dic['execution_time'] for dic in ans]
        
        """If there are not WA"""
        if(sum(wa)==0):
            return {
                "submission_id": self.submission_id,
                "verdict": FLAGS_ERRORS[0],
                "max_memory":round(max(memories),1),
                "max_time":round(max(exec_times),2)}  
        
        """If there are at least WA"""
        L_first_wa=[1 if flag!=0 else 0 for flag in wa]                
        first_wa_index=L_first_wa.index(1)
        return {
            "submission_id": self.submission_id,
            "verdict": FLAGS_ERRORS[wa[first_wa_index]],
            "wrong_case": first_wa_index+1,
            "max_memory": round(max(memories),1),
            "max_time": round(max(exec_times),2)}

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