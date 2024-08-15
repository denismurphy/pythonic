# Import the traceback module with an alias 'tb'
import traceback as tb
from typing import Any, Union

def divide(a: float, b: float) -> Union[float, str]:
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid type for division"
    else:
        return result
    finally:
        print("Division operation attempted")


class CustomError(Exception):
    """A custom exception class"""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


def validate_age(age: Any) -> None:
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise CustomError("Age is unrealistically high")


# Function to handle KeyError exceptions
def key_error_except(key_error: KeyError) -> None:
    # Format the exception details into a string
    error: str = "".join(tb.format_exception(None, key_error, key_error.__traceback__))
    # Print the formatted error message
    print(f"key error: {error}")


# Function to handle TypeError exceptions
def type_error_except(type_error: TypeError) -> None:
    # Format the exception details into a string
    error: str = "".join(tb.format_exception(None, type_error, type_error.__traceback__))
    # Print the formatted error message
    print(f"type error: {error}")


# Function to handle generic exceptions
def exception_except(exception: Exception) -> None:
    # Format the exception details into a string
    error: str = "".join(tb.format_exception(None, exception, exception.__traceback__))
    # Print the formatted error message
    print(f"exception error: {error}")


# Dictionary representing a student with various attributes
student: dict[str, any] = {
    "name": "mark",
    "student_id": 15163,
    "feedback": None,
    "last_name": "test"
}

# Try block to handle potential KeyError and TypeError
try:
    # Access the last name from the _student dictionary
    last_name = student["last_name"]
    # Attempt to add an integer to a string, which will raise a TypeError
    numbered_last_name: int = 3 + last_name
except KeyError as _key_error:
    # Handle KeyError using the custom function
    key_error_except(_key_error)
except TypeError as _type_error:
    # Handle TypeError using the custom function
    type_error_except(_type_error)

# Try block to handle generic exceptions
try:
    # Attempt to call a non-existent function, which will raise an AttributeError
    numbered_last_name.function_not_exist()
except Exception as _exception:
    # Handle generic exceptions using the custom function
    exception_except(_exception)

    # Basic error handling
    print(divide(10, 2))
    print(divide(10, 0))
    print(divide("10", 2))

    # Custom exception handling
    try:
        validate_age(25)
        print("Age is valid")
        validate_age("25")
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except CustomError as e:
        print(f"CustomError: {e}")


    # Using assert for debugging
    def calculate_rectangle_area(length: float, width: float) -> float:
        assert length > 0 and width > 0, "Length and width must be positive"
        return length * width
    try:
        area = calculate_rectangle_area(5, -2)
    except AssertionError as e:
        print(f"AssertionError: {e}")

# Print a message indicating that everything is okay
print("everything ok")
