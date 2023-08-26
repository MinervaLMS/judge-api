"""Import the Middleware class from the corresponding module"""
import pytest
from app.middleware.request_validations import Middleware
from utils.exceptions import RequestFormatError
from tests.resources import DATA


@pytest.fixture(name="data")
def data_example():
    """Fixture providing example data for testing"""
    return DATA


@pytest.fixture(name="submission_data")
def submission(data):
    """Fixture providing a Middleware instance with example data for testing"""
    return Middleware(data)


def test_validate_code_valid_py(submission_data: Middleware):
    """verify validate_code method for valid data for a python submission"""
    submission_data.language = "py3"
    assert submission_data.validate_code() == "Valid submission"


def test_validate_code_valid_java(submission_data: Middleware):
    """verify validate_code method for valid data for a java submission"""
    submission_data.language = "java"
    assert submission_data.validate_code() == "Valid submission"


def test_validate_code_valid_cpp(submission_data: Middleware):
    """verify validate_code method for valid data for a cpp submission"""
    submission_data.language = "cpp"
    assert submission_data.validate_code() == "Valid submission"


def test_validate_code_long_time_limit(submission_data: Middleware):
    """verify that code execution time doesn't exceed the limit"""
    submission_data.time_limit = 12000
    expected_error_message = "Invalid time limit provided."
    with pytest.raises(RequestFormatError, match=expected_error_message):
        submission_data.validate_time_limit()


def test_validate_code_long_memory_limit(submission_data: Middleware):
    """verify that code execution memory doesn't exceed the limit"""
    submission_data.memory_limit = 300
    expected_error_message = "Invalid memory limit provided."
    with pytest.raises(RequestFormatError, match=expected_error_message):
        submission_data.validate_memory_limit()


def test_standardize_language_name_invalid(submission_data: Middleware):
    """
    Verify if the standardize_language_name method
    not standardized the language when it doesn´t exist
    """
    submission_data.language = "py2"
    expected_error_message = "Unsupported language provided."
    with pytest.raises(RequestFormatError, match=expected_error_message):
        submission_data.standardize_language_name()


def test_validate_empty_code(submission_data: Middleware):
    """verify that code is not empty"""
    submission_data.code = ""
    expected_error_message = "Missing or empty code field."
    with pytest.raises(RequestFormatError, match=expected_error_message):
        submission_data.empty_data()


def test_validate_empty_input(submission_data: Middleware):
    """Verify if the data is not empty"""
    submission_data.input = ""
    expected_error_message = "Missing or empty input field."
    with pytest.raises(RequestFormatError, match=expected_error_message):
        submission_data.empty_data()


def test_validate_empty_output(submission_data: Middleware):
    """verify that input is not empty"""
    submission_data.output = ""
    expected_error_message = "Missing or empty output field."
    with pytest.raises(RequestFormatError, match=expected_error_message):
        submission_data.empty_data()


def test_validate_empty_time_limit(submission_data: Middleware):
    """verify that time limit is not empty"""
    submission_data.time_limit = ""
    expected_error_message = "Missing or empty time_limit field."
    with pytest.raises(RequestFormatError, match=expected_error_message):
        submission_data.empty_data()


def test_validate_empty_memory_limit(submission_data: Middleware):
    """verify that memory limit is not empty"""
    submission_data.memory_limit = ""
    expected_error_message = "Missing or empty memory_limit field."
    with pytest.raises(RequestFormatError, match=expected_error_message):
        submission_data.empty_data()


def test_validate_empty_language(submission_data: Middleware):
    """verify that language is not empty"""
    submission_data.language = ""
    expected_error_message = "Missing or empty language field."
    with pytest.raises(RequestFormatError, match=expected_error_message):
        submission_data.empty_data()
