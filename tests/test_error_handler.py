import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.error_handler import handle_errors, TaskNotFoundError, InvalidInputError, FileOperationError


def test_handle_errors_decorator():
    @handle_errors
    def func(raise_type):
        if raise_type == "task":
            raise TaskNotFoundError("Test")
        elif raise_type == "input":
            raise InvalidInputError("Test")
        elif raise_type == "file":
            raise FileOperationError("Test")
        else:
            return "ok"

    assert func("task") is None
    assert func("input") is None
    assert func("file") is None
    assert func("ok") == "ok"


def test_handle_errors_unexpected():
    @handle_errors
    def bad():
        raise RuntimeError("Unexpected")

    assert bad() is None  # перехвачено и возвращено None