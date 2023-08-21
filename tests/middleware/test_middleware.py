"""Import the Middleware class from the corresponding module"""
from app.middleware.request_validations import Middleware


data_dict_valid_python = {
    "code": "print('Hello, World!')",
    "input": "",
    "output": "Hello, World!",
    "time_limit": 5,
    "memory_limit": 256,
    "language": "python3",
}

"""Data dictionaries for the tests"""
data_dict_valid_java = {
    "code": "print('Hello, World!')",
    "input": "",
    "output": "Hello, World!",
    "time_limit": 5,
    "memory_limit": 256,
    "language": "java11",
}

"""Data dictionaries for the tests"""
data_dict_valid_cpp = {
    "code": "print('Hello, World!')",
    "input": "",
    "output": "Hello, World!",
    "time_limit": 5,
    "memory_limit": 256,
    "language": "cpp14",
}

"""Data dictionaries for the tests"""
data_dict_invalid_empty_code = {
    "code": "",
    "input": "",
    "output": "Hello, World!",
    "time_limit": 5,
    "memory_limit": 256,
    "language": "python3",
}

"""Data dictionaries for the tests"""
data_dict_invalid_long_time_limit = {
    "code": "print('Hello, World!')",
    "input": "",
    "output": "Hello, World!",
    "time_limit": 15,
    "memory_limit": 256,
    "language": "python3",
}

"""Data dictionaries for the tests"""
data_dict_invalid_language = {
    "code": "print('Hello, World!')",
    "input": "",
    "output": "Hello, World!",
    "time_limit": 5,
    "memory_limit": 256,
    "language": "c",
}


def test_validate_code_valid_py():
    """verify validate_code method for valid data"""
    middleware = Middleware(data_dict_valid_python)
    assert middleware.validate_code() is True


def test_validate_code_valid_java():
    """verify validate_code method for valid data"""
    middleware = Middleware(data_dict_valid_java)
    assert middleware.validate_code() is True


def test_validate_code_valid_cpp():
    """verify validate_code method for valid data"""
    middleware = Middleware(data_dict_valid_cpp)
    assert middleware.validate_code() is True


def test_validate_code_empty_code():
    """verify that code is not empty"""
    middleware = Middleware(data_dict_invalid_empty_code)
    assert middleware.validate_code() is False


def test_validate_code_long_time_limit():
    """verify that code execution time doesn't exceed the limit"""
    middleware = Middleware(data_dict_invalid_long_time_limit)
    assert middleware.validate_code() is False


def test_standardize_language_name_valid_py():
    """
    Verify if the standardize_language_name method
    standardized the language correctly
    """
    middleware = Middleware(data_dict_valid_python)
    assert middleware.standardize_language_name() is True


def test_standardize_language_name_valid_java():
    """
    Verify if the standardize_language_name method
    standardized the language correctly
    """
    middleware = Middleware(data_dict_valid_java)
    assert middleware.standardize_language_name() is True


def test_standardize_language_name_valid_cpp():
    """
    Verify if the standardize_language_name method
    standardized the language correctly
    """
    middleware = Middleware(data_dict_valid_cpp)
    assert middleware.standardize_language_name() is True


def test_standardize_language_name_invalid():
    """
    Verify if the standardize_language_name method
    not standardized the language when it doesn´t exist
    """
    middleware = Middleware(data_dict_invalid_language)
    assert middleware.standardize_language_name() is False


def test_standardize_language_cpp():
    """Verify if the language name was standardized correctly"""
    middleware = Middleware(data_dict_valid_cpp)
    middleware.standardize_language_name()
    assert middleware.language == "cpp"


def test_standardize_language_py():
    """Verify if the language name was standardized correctly"""
    middleware = Middleware(data_dict_valid_python)
    middleware.standardize_language_name()
    assert middleware.language == "py"


def test_standardize_language_java():
    """Verify if the language name was standardized correctly"""
    middleware = Middleware(data_dict_valid_java)
    middleware.standardize_language_name()
    assert middleware.language == "java"
