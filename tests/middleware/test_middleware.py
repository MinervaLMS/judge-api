"""Import the Middleware class from the corresponding module"""
import pytest
from app.middleware.request_validations import Middleware
from tests.resources import DATA


@pytest.fixture(name="data")
def data_example():
    """Fixture providing example data for testing"""
    return DATA


@pytest.fixture(name="submission_data")
def submission(data):
    """Fixture providing a Middleware instance with example data for testing"""
    return Middleware(data)


def test_validate_code_long_time_limit(submission_data):
    """verify that code execution time doesn't exceed the limit"""
    submission_data.time_limit = 12000
    assert submission_data.validate_code() is False


def test_validate_code_valid_py(submission_data):
    """verify validate_code method for valid data"""
    submission_data.language = "py3"
    assert submission_data.validate_code() is True
    assert submission_data.standardize_language_name() is True


def test_validate_code_valid_java(submission_data):
    """verify validate_code method for valid data"""
    submission_data.language = "java"
    assert submission_data.validate_code() is True
    assert submission_data.standardize_language_name() is True


def test_validate_code_valid_cpp(submission_data):
    """verify validate_code method for valid data"""
    submission_data.language = "cpp"
    assert submission_data.validate_code() is True
    assert submission_data.standardize_language_name() is True


def test_standardize_language_name_invalid(submission_data):
    """
    Verify if the standardize_language_name method
    not standardized the language when it doesn´t exist
    """
    submission_data.language = "py2"
    assert submission_data.standardize_language_name() is False
    assert submission_data.validate_code() is False


def test_validate_empty_code(submission_data):
    """verify that code is not empty"""
    submission_data.code = ""
    assert submission_data.empty_data() is False
    assert submission_data.validate_code() is False


def test_validate_empty_input(submission_data):
    """Verify if the data is not empty"""
    submission_data.input = ""
    assert submission_data.empty_data() is False
    assert submission_data.validate_code() is False


def test_validate_empty_output(submission_data):
    """verify that input is not empty"""
    submission_data.output = ""
    assert submission_data.empty_data() is False
    assert submission_data.validate_code() is False


def test_validate_empty_time_limit(submission_data):
    """verify that time limit is not empty"""
    submission_data.time_limit = ""
    assert submission_data.empty_data() is False
    assert submission_data.validate_code() is False


def test_validate_empty_memory_limit(submission_data):
    """verify that memory limit is not empty"""
    submission_data.memory_limit = ""
    assert submission_data.empty_data() is False
    assert submission_data.validate_code() is False


def test_validate_empty_language(submission_data):
    """verify that language is not empty"""
    submission_data.language = ""
    assert submission_data.empty_data() is False
    assert submission_data.validate_code() is False
