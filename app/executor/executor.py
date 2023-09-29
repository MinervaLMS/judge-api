"""Module with executor class."""

import io
import sys
from app.DMOJ.submission import Submission
from app.DMOJ.judge import Judge
from app.DMOJ.judge_connection import SingletonJudge
from app.utils.constants import FLAGS_ERRORS
from flask import jsonify

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
        
        
        """If ans is empty"""
        if(len(ans)==0):
            return {
                "submission_id": self.submission_id,
                "verdict": "Judge execution: code compilation or problem_id don't exist.",
            }
        
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
        wa=[dic['flag'] for dic in ans]

        """If ans is empty or If there are at least WA"""
        if (ans==[] or sum(wa)!=0):
            return False
        
        """If there are not WA"""
        if(sum(wa)==0):
            return True
        
