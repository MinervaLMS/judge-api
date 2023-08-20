"""This module contains Middleware class"""


class Middleware:
    """
    This class handles code submission validation for the application.
    The Middleware class validates incoming code submissions and ensures
    they meet the necessary criteria.
    """

    def __init__(self, data_dict):
        """
        Initializes an instance of Middleware for request validation.

        Parameters:
        - data_dict (dict):
        A dictionary containing request data to be validated.
        """
        self.code = data_dict["code"]
        self.input_data = data_dict["input"]
        self.output_data = data_dict["output"]
        self.time_limit = data_dict["time_limit"]
        self.memory_limit = data_dict["memory_limit"]
        self.language = data_dict["language"]

    def validate_code(self):
        """
        Validating if the language name is standardized
        if the code is not empty
        if the time limit is reasonable
        """
        if not self.standardize_language_name():
            return False

        if self.code == "":
            return False

        if self.time_limit > 10:
            return False

        return True

    def standardize_language_name(self):
        """Mapping of language names to standardized names"""

        language_mapping = {
            "python3": "py",
            "py": "py",
            "py2": "py",
            "py3": "py",
            "pypy": "py",
            "pypy3": "py",
            "java": "java",
            "java10": "java",
            "java11": "java",
            "java8": "java",
            "java9": "java",
            "cpp": "cpp",
            "clangx": "cpp",
            "cpp03": "cpp",
            "cpp11": "cpp",
            "cpp14": "cpp",
            "cpp17": "cpp",
        }

        standardized = language_mapping.get(self.language.lower())
        if standardized is None:
            return False
        self.language = standardized
        return True
