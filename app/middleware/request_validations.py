"""This module contains Middleware class"""
from typing import Dict
from utils.exceptions import RequestFormatError


class Middleware:
    """
    This class handles code submission validation for the application.
    The Middleware class validates incoming code submissions and ensures
    they meet the necessary criteria.
    """

    def __init__(self, data: Dict[str, str]):
        """
        Initializes an instance of Middleware for request validation.

        Parameters:
        - data (dict):
        A dictionary containing request data to be validated.
        """
        self.code = data["code"]
        self.input = data["input"]
        self.output = data["output"]
        self.time_limit = int(data["time_limit"])
        self.memory_limit = int(data["memory_limit"])
        self.language = data["language"]

    def validate_code(self) -> str:
        """
        Check if the language name is standardized
        if the code, input and output are not empty
        if the time and memory limit is reasonable

        Returns:
            str: A message indicating the result of the validation.
        """
        try:
            self.empty_data()
            self.standardize_language_name()
            self.validate_time_limit()
            self.validate_memory_limit()
            return "Valid submission"
        except RequestFormatError as error:
            return str(error)

    def empty_data(self) -> None:
        """
        Check if the code, input, output, time_limit,
        memory_limit, and language fields are not empty.

        Raises:
            RequestFormatError: If any of the required fields is missing or empty.
        """
        fields_to_check = [
            ("code", self.code),
            ("input", self.input),
            ("output", self.output),
            ("time_limit", self.time_limit),
            ("memory_limit", self.memory_limit),
            ("language", self.language),
        ]

        for field_name, field_value in fields_to_check:
            if not field_value:
                raise RequestFormatError(
                    field_name, f"Missing or empty {field_name} field."
                )

    def standardize_language_name(self) -> None:
        """
        Check if the provided language is supported.

        Raises:
            RequestFormatError: If the provided language is not supported.
        """
        supported_languages = {"py3", "java", "cpp"}
        if self.language not in supported_languages:
            raise RequestFormatError("language", "Unsupported language provided.")

    def validate_time_limit(self) -> None:
        """
        Validate if the provided time limit is within a reasonable range.

        Raises:
            RequestFormatError: If the time limit is invalid.
        """
        if self.time_limit > 10000:
            raise RequestFormatError("time_limit", "Invalid time limit provided.")

    def validate_memory_limit(self) -> None:
        """
        Validate if the provided memory limit is within a reasonable range.

        Raises:
            RequestFormatError: If the memory limit is invalid.
        """
        if self.memory_limit > 256:
            raise RequestFormatError("memory_limit", "Invalid memory limit provided.")
