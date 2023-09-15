"""This module contains the classes to spawns a judge ."""

import atexit
import readline

from typing import List, cast, Any

from dmoj.commands.base_command import GradedSubmission
from dmoj.judge import Judge
from dmoj.packet import PacketManager
from app.utils.constants import RUNTIME, JUDGE_ROOT
from dmoj.commands import all_commands, register_command

import logging
from dmoj import judgeenv, contrib, executors


class LocalPacketManager:
    def __init__(self, judge: Judge) -> None:
        """
        Initializes an instance of the LocalPacketManager class.

        Args:
            judge: The judge object associated with this instance.
        """
        self.judge = judge
        self.judge_connection = SingletonJudge()

    def _receive_packet(self, packet: Any) -> None:
        """
        This function is created solely for the purpose of enabling the class
        to be cast to the LocalPacketManager type.
        """
        pass

    def supported_problems_packet(self, problems: Any) -> None:
        """
        This function is created solely for the purpose of enabling the class
        to be cast to the LocalPacketManager type.
        """
        pass

    def test_case_status_packet(self, position: int, result: Any) -> None:
        """
        Appends a test case status packet to the response list of the judge connection.

        Args:
            position (int): The position or index of the test case.
            result (Result): The result object containing test case information.
        """
        self.judge_connection.response.append(
            {
                "flag": result.result_flag,
                "execution_time": result.execution_time,
                "max_memory": result.max_memory,
                "feedback": result.feedback,
                "points": result.points,
            }
        )

    def compile_error_packet(self, log: Any) -> None:
        """
        This function is created solely for the purpose of enabling the class
        to be cast to the LocalPacketManager type.
        """
        pass

    def compile_message_packet(self, log: Any) -> None:
        """
        This function is created solely for the purpose of enabling the class
        to be cast to the LocalPacketManager type.
        """
        pass

    def internal_error_packet(self, message: Any) -> None:
        """
        This function is created solely for the purpose of enabling the class
        to be cast to the LocalPacketManager type.
        """
        pass

    def begin_grading_packet(self, is_pretested: Any) -> None:
        """
        This function is created solely for the purpose of enabling the class
        to be cast to the LocalPacketManager type.
        """
        pass

    def grading_end_packet(self) -> None:
        """
        This function is created solely for the purpose of enabling the class
        to be cast to the LocalPacketManager type.
        """
        pass

    def batch_begin_packet(self) -> None:
        """
        This function is created solely for the purpose of enabling the class
        to be cast to the LocalPacketManager type.
        """
        pass

    def batch_end_packet(self) -> None:
        """
        This function is created solely for the purpose of enabling the class
        to be cast to the LocalPacketManager type.
        """
        pass

    def current_submission_packet(self) -> None:
        """
        This function is created solely for the purpose of enabling the class
        to be cast to the LocalPacketManager type.
        """
        pass

    def submission_aborted_packet(self) -> None:
        """
        This function is created solely for the purpose of enabling the class
        to be cast to the LocalPacketManager type.
        """
        pass

    def submission_acknowledged_packet(self, sub_id: Any) -> None:
        """
        This function is created solely for the purpose of enabling the class
        to be cast to the LocalPacketManager type.
        """
        pass

    def run(self) -> None:
        """
        This function is created solely for the purpose of enabling the class
        to be cast to the LocalPacketManager type.
        """
        pass

    def close(self) -> None:
        """
        This function is created solely for the purpose of enabling the class
        to be cast to the LocalPacketManager type.
        """
        pass


class LocalJudge(Judge):
    graded_submissions: List[GradedSubmission]

    def __init__(self) -> None:
        """
        Initializes an instance of the LocalJudge class.

        This constructor sets up the LocalJudge with a LocalPacketManager
        and initializes other necessary attributes.

        """
        super().__init__(cast(PacketManager, LocalPacketManager(self)))
        self.submission_id_counter = 0
        self.graded_submissions = []


class SingletonJudge:
    _instance = None
    response: list
    judge: Judge

    def __new__(cls) -> "SingletonJudge":
        """
        Ensures that only one instance of SingletonJudge is created.

        This method overrides the __new__ method to ensure that only one instance
        of SingletonJudge is created and initializes it with necessary configurations.
        """

        if cls._instance is None:
            cls._instance = super(SingletonJudge, cls).__new__(cls)

            judgeenv.env["runtime"] = RUNTIME

            executors.load_executors()
            contrib.load_contrib_modules()

            judgeenv.load_env(cli=True)

            logging.basicConfig(
                filename=judgeenv.log_file,
                level=judgeenv.log_level,
                format="%(levelname)s %(asctime)s %(module)s %(message)s",
            )

            try:
                readline.read_history_file(judgeenv.cli_history_file)
            except FileNotFoundError:
                pass
            atexit.register(readline.write_history_file, judgeenv.cli_history_file)

            judgeenv._root = JUDGE_ROOT
            judgeenv.problem_dirs = ""

            print("Running local judge...")
            cls._instance.response = list()
            cls._instance.judge = LocalJudge()

            for command in all_commands:
                register_command(command(cls._instance.judge))

            cls._instance.judge.listen()

        return cls._instance
