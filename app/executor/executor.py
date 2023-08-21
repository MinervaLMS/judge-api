"""Module with executor class."""

import io
import sys
import time
import psutil


class Executor:
    """Class that conects the judge with the code."""

    def __init__(self, output, input_data, code):
        self.output = output
        self.input_data = input_data
        self.code = code

    def judge(self) -> dict:
        """Method that runs the code on the judge."""

        start_time = time.time()

        memory_before = psutil.virtual_memory().available

        result = self.executioner()

        end_time = time.time()

        memory_after = psutil.virtual_memory().available

        if result:
            return {
                "execution_time": end_time - start_time,
                "memory_used": (memory_before - memory_after) / (1024**2),
                "verdict": "AC",
            }
        return {
            "execution_time": end_time - start_time,
            "memory_used": memory_before - memory_after,
            "verdict": "WA",
        }

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
            print(self.output)
            print(output_value)

            if output_value == self.output:
                return True
            return False
        except ZeroDivisionError:
            output_value = new_stdout.getvalue().strip()
            sys.stdout = old_stdout
            return False
