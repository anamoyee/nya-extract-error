import traceback
from collections.abc import Callable


def extract_error_to_tuple(e: BaseException) -> tuple[str, str]:
	return (
		e.__class__.__name__,
		str(e),
	)


def extract_error(e: BaseException, *, pattern: str = "%s: %s") -> str:
	return pattern % extract_error_to_tuple(e)


def extract_traceback(e: BaseException) -> str:
	traceback_details = traceback.format_tb(e.__traceback__)
	return "".join(traceback_details)


def print_exception_with_traceback(
	e: BaseException,
	*,
	print: Callable[[str], None] = print,  # ruff:ignore[builtin-argument-shadowing]
) -> None:
	"""Re-enact the traceback printing when an exception is raised, without actually raising the exception."""
	print("Traceback (most recent call last):")
	print(extract_traceback(e))
	print(extract_error(e))
