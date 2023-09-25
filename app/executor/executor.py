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
        """Return a resume of veredicts as a dict"""

        judge_connection = SingletonJudge()

        submission = Submission(id=1,
                                submission_id="TEST", 
                                problem_id="ALA4", #Se debe especificar manualmente el ID de problema, deberia ser automatico. 
                                source=self.code, 
                                language="PY3", 
                                time_limit=1, 
                                memory_limit=80760)
        ans = Judge.submit(submission, judge_connection)
        
        memories=[dic['max_memory'] for dic in ans]
        wa=[dic['flag'] for dic in ans]
        exec_times=[dic['execution_time'] for dic in ans]
        
        """If there are not WA"""
        if(1 not in wa):
            return {
                "verdict": "AC",
                "max_memory":round(max(memories),1),
                "max_time":round(max(exec_times),2)}  
        
        """If there are at least WA"""
        first_wa_index=wa.index(1)
        return {
            "submission_id": "TEST",
            "verdict": "WA",
            "wrong_case": {"case_number": first_wa_index+1,
                           "input": self.input_data[first_wa_index],
                           "output_expected": self.output[first_wa_index]},
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