from __future__ import annotations

from typing import TYPE_CHECKING

from nya_extract_error import extract_error, extract_error_to_tuple, extract_traceback, print_exception_with_traceback

if TYPE_CHECKING:
	import pytest


def test_extract_error_to_tuple():
	e = ValueError("Test error")

	result = extract_error_to_tuple(e)
	assert result == ("ValueError", "Test error")


def test_extract_error():
	e = ValueError("Test error")

	result = extract_error(e)
	assert result == "ValueError: Test error"


def test_extract_traceback():
	try:
		msg = "Test error"
		raise ValueError(msg)  # ruff:ignore[raise-within-try]
	except ValueError as e:
		result = extract_traceback(e)
		expected = f"""
  File "{__file__}", line 28, in test_extract_traceback
    raise ValueError(msg)  # ruff:ignore[raise-within-try]
    ^^^^^^^^^^^^^^^^^^^^^

"""[1:-1]

		assert result == expected


def test_print_exception_with_traceback(capsys: pytest.CaptureFixture[str]):
	try:
		msg = "Test error"
		raise ValueError(msg)  # ruff:ignore[raise-within-try]
	except ValueError as e:
		print_exception_with_traceback(e)

	captured = capsys.readouterr()
	expected = f"""
Traceback (most recent call last):
  File "{__file__}", line 44, in test_print_exception_with_traceback
    raise ValueError(msg)  # ruff:ignore[raise-within-try]
    ^^^^^^^^^^^^^^^^^^^^^

ValueError: Test error

"""[1:-1]

	assert captured.out == expected
